// Strict AI Voice Examiner Engine (Speech Synthesis & High-Accuracy Recognition)
import { soundFX } from './audio.js';

export class VoiceExaminer {
  constructor() {
    this.synth = window.speechSynthesis || null;
    this.recognition = null;
    this.voices = [];
    this.selectedVoice = null;
    this.rate = 0.92; // Clear, measured examiner pace
    this.pitch = 1.0;
    this.isSpeaking = false;
    this.isListening = false;
    this.isStartingRec = false;
    this.enabled = true;
    this.autoListen = true;
    this.currentUtterance = null;
    this.currentLanguage = 'en'; // 'en' | 'te'

    // Callbacks for UI
    this.onStateChange = null;       // (state: 'idle'|'speaking'|'listening'|'evaluating')
    this.onSpeechInterim = null;     // (interimTranscript)
    this.onSpeechRecognized = null;  // (finalTranscript)
    this.onAnswerDetected = null;    // (optionIndex 1-4)
    this.onCommandDetected = null;   // (command: 'repeat'|'next'|'skip'|'stop')
    this.onMicLevel = null;          // (0 - 100 level)
    this.onPermissionError = null;   // (errorMessage)

    this.initVoices();
    this.initRecognition();
  }

  initVoices() {
    if (!this.synth) return;
    const updateVoices = () => {
      this.voices = this.synth.getVoices();
      this.selectBestVoice();
    };

    updateVoices();
    if (this.synth.onvoiceschanged !== undefined) {
      this.synth.onvoiceschanged = updateVoices;
    }
  }

  selectBestVoice() {
    if (!this.voices || this.voices.length === 0) return;

    if (this.currentLanguage === 'te') {
      // Look for Telugu voice
      const telVoice = this.voices.find(v => v.lang.startsWith('te') || v.name.toLowerCase().includes('telugu'));
      if (telVoice) {
        this.selectedVoice = telVoice;
        return;
      }
    }

    // High quality English voices preferred
    const preferredVoices = [
      v => v.lang === 'en-IN' && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Heera') || v.name.includes('Ravi')),
      v => v.lang === 'en-IN',
      v => v.lang.startsWith('en-GB') && (v.name.includes('Natural') || v.name.includes('Female')),
      v => v.lang.startsWith('en-US') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Zira') || v.name.includes('Jenny')),
      v => v.lang.startsWith('en-US'),
      v => v.lang.startsWith('en')
    ];

    for (const matchFn of preferredVoices) {
      const match = this.voices.find(matchFn);
      if (match) {
        this.selectedVoice = match;
        return;
      }
    }

    this.selectedVoice = this.voices[0] || null;
  }

  setLanguage(langCode) {
    this.currentLanguage = langCode;
    this.selectBestVoice();
    if (this.recognition) {
      this.recognition.lang = langCode === 'te' ? 'te-IN' : 'en-IN';
    }
  }

  initRecognition() {
    const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRec) {
      console.warn("Speech Recognition API not supported in this browser.");
      return;
    }

    try {
      this.recognition = new SpeechRec();
      this.recognition.continuous = true;       // Keeps listening until answer is captured
      this.recognition.interimResults = true;    // Instant feedback on words as spoken
      this.recognition.maxAlternatives = 3;
      this.recognition.lang = this.currentLanguage === 'te' ? 'te-IN' : 'en-IN';

      this.recognition.onstart = () => {
        this.isListening = true;
        this.isStartingRec = false;
        soundFX.playMicStart();
        soundFX.startMicLevelMonitor((lvl) => {
          if (this.onMicLevel) this.onMicLevel(lvl);
        });
        if (this.onStateChange) this.onStateChange('listening');
      };

      this.recognition.onresult = (event) => {
        let interimTranscript = '';
        let finalTranscript = '';

        for (let i = event.resultIndex; i < event.results.length; ++i) {
          const res = event.results[i];
          const text = res[0].transcript;
          if (res.isFinal) {
            finalTranscript += text + ' ';
          } else {
            interimTranscript += text + ' ';
          }
        }

        const currentText = (finalTranscript || interimTranscript).trim();
        if (currentText) {
          if (this.onSpeechInterim) this.onSpeechInterim(currentText);

          // Fast intent detection even on interim results
          const detectedOpt = this.parseAnswerFromText(currentText);
          if (detectedOpt) {
            console.log(`🎯 Instant match detected from speech: Option ${detectedOpt}`);
            if (this.onSpeechRecognized) this.onSpeechRecognized(currentText);
            this.stopListening();
            if (this.onAnswerDetected) this.onAnswerDetected(detectedOpt);
            return;
          }

          // Check commands
          const command = this.parseCommandFromText(currentText);
          if (command) {
            this.stopListening();
            if (this.onCommandDetected) this.onCommandDetected(command);
            return;
          }

          if (finalTranscript && this.onSpeechRecognized) {
            this.onSpeechRecognized(finalTranscript.trim());
          }
        }
      };

      this.recognition.onerror = (event) => {
        console.warn("Speech Recognition Event Error:", event.error);
        if (event.error === 'not-allowed') {
          if (this.onPermissionError) {
            this.onPermissionError("Microphone permission was denied. Please allow microphone in browser settings or use HTTPS.");
          }
        }
        if (event.error !== 'no-speech') {
          this.stopListening();
        }
      };

      this.recognition.onend = () => {
        // If user is supposed to be listening and did not deliberately stop
        if (this.isListening && !this.isSpeaking) {
          try {
            this.recognition.start();
          } catch (e) {
            this.isListening = false;
            soundFX.stopMicLevelMonitor();
            if (this.onStateChange) this.onStateChange('idle');
          }
        } else {
          this.isListening = false;
          soundFX.stopMicLevelMonitor();
          if (!this.isSpeaking && this.onStateChange) {
            this.onStateChange('idle');
          }
        }
      };
    } catch (e) {
      console.error("Failed to initialize SpeechRecognition:", e);
    }
  }

  stopAll() {
    this.stopSpeaking();
    this.stopListening();
  }

  stopSpeaking() {
    if (this.synth) {
      this.synth.cancel();
    }
    this.isSpeaking = false;
  }

  stopListening() {
    this.isListening = false;
    this.isStartingRec = false;
    soundFX.stopMicLevelMonitor();
    if (this.recognition) {
      try {
        this.recognition.abort();
      } catch (e) {}
    }
    if (this.onMicLevel) this.onMicLevel(0);
    if (!this.isSpeaking && this.onStateChange) {
      this.onStateChange('idle');
    }
  }

  async startListening() {
    if (!this.recognition) {
      alert("Voice recognition is not supported in this browser. Please use Chrome or Edge.");
      return;
    }

    if (this.isListening || this.isStartingRec) return;
    this.stopSpeaking();

    // Explicitly request microphone access first to trigger browser permissions cleanly
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      try {
        await navigator.mediaDevices.getUserMedia({ audio: true });
      } catch (err) {
        console.warn("Microphone access error:", err);
        if (this.onPermissionError) {
          this.onPermissionError("Microphone access blocked. Please grant microphone permission in your browser.");
        }
        return;
      }
    }

    this.isStartingRec = true;
    try {
      this.recognition.lang = this.currentLanguage === 'te' ? 'te-IN' : 'en-IN';
      this.recognition.start();
    } catch (e) {
      console.warn("Could not start recognition:", e);
      this.isStartingRec = false;
    }
  }

  speak(text, onComplete = null) {
    if (!this.synth || !this.enabled) {
      if (onComplete) onComplete();
      return;
    }

    this.stopAll();
    this.isSpeaking = true;
    if (this.onStateChange) this.onStateChange('speaking');

    // Clean text for natural clear pronunciation
    const cleanText = text
      .replace(/[\/\\]/g, ' or ')
      .replace(/[\(\)]/g, ' ')
      .replace(/_+/g, ' blank ')
      .replace(/₹/g, 'rupees ')
      .replace(/°/g, ' degrees ')
      .replace(/\s+/g, ' ');

    const utterance = new SpeechSynthesisUtterance(cleanText);
    if (this.selectedVoice) {
      utterance.voice = this.selectedVoice;
    }
    utterance.rate = this.rate;
    utterance.pitch = this.pitch;

    utterance.onend = () => {
      this.isSpeaking = false;
      if (this.onStateChange) this.onStateChange('idle');
      if (onComplete) onComplete();
    };

    utterance.onerror = (e) => {
      console.warn("Speech synthesis error:", e);
      this.isSpeaking = false;
      if (this.onStateChange) this.onStateChange('idle');
      if (onComplete) onComplete();
    };

    this.currentUtterance = utterance;
    this.synth.speak(utterance);
  }

  // Ask MCQ question firmly & strictly
  askQuestion(questionObj, questionNumber, totalQuestions) {
    if (!this.enabled) return;

    soundFX.playPing();

    const isTelugu = this.currentLanguage === 'te' || questionObj.subject === 'Telugu';
    const qText = questionObj.question;

    let speechPrompt = "";
    if (isTelugu) {
      speechPrompt = `ప్రశ్న ${questionNumber}: ${qText}. `;
      questionObj.options.forEach((opt, i) => {
        const telNum = ["ఒకటి", "రెండు", "మూడు", "నాలుగు"][i];
        speechPrompt += `ఆప్షన్ ${telNum}: ${opt}. `;
      });
      speechPrompt += "మీ సమాధానం చెప్పండి.";
    } else {
      speechPrompt = `Question ${questionNumber} of ${totalQuestions}. ${qText}. `;
      questionObj.options.forEach((opt, i) => {
        speechPrompt += `Option ${i + 1}: ${opt}. `;
      });
      speechPrompt += "What is your answer?";
    }

    this.speak(speechPrompt, () => {
      if (this.autoListen) {
        setTimeout(() => {
          this.startListening();
        }, 300);
      }
    });
  }

  // Strict Evaluation: No Hints! If wrong, strictly tells the correct answer
  evaluateAnswer(userOptionIndex, correctOptionIndex, questionObj, onFinish = null) {
    const isCorrect = userOptionIndex === correctOptionIndex;
    const correctText = questionObj.options[correctOptionIndex - 1];
    const isTelugu = this.currentLanguage === 'te' || questionObj.subject === 'Telugu';

    let feedbackText = "";
    if (isCorrect) {
      soundFX.playCorrect();
      if (isTelugu) {
        feedbackText = `కరెక్ట్! ఆప్షన్ ${correctOptionIndex}, ${correctText}, సరైన సమాధానం.`;
      } else {
        feedbackText = `Correct! Option ${correctOptionIndex}, ${correctText}, is the right answer.`;
      }
    } else {
      soundFX.playWrong();
      if (isTelugu) {
        feedbackText = `తప్పు! మీరు ఎంచుకున్నది ఆప్షన్ ${userOptionIndex}. సరైన సమాధానం ఆప్షన్ ${correctOptionIndex}: ${correctText}. గట్టిగా గుర్తుంచుకోండి.`;
      } else {
        feedbackText = `Wrong! You selected Option ${userOptionIndex}. The correct answer is Option ${correctOptionIndex}: ${correctText}. Remember this firmly.`;
      }
    }

    this.speak(feedbackText, onFinish);
  }

  // Parse natural spoken answers
  parseAnswerFromText(transcript) {
    const text = transcript.toLowerCase();

    // Option 1 triggers
    if (
      /\b(one|1|first|first option|option one|option 1|option a|a|ay|hey|won|వన్|ఒకటి|మొదటి|ఫస్ట్)\b/i.test(text) &&
      !text.includes("two") && !text.includes("three") && !text.includes("four") && !text.includes("2") && !text.includes("3") && !text.includes("4")
    ) {
      return 1;
    }

    // Option 2 triggers
    if (
      /\b(two|2|second|second option|option two|option 2|option b|b|bee|to|too|టూ|రెండు|రెండవ|సెకండ్)\b/i.test(text) &&
      !text.includes("three") && !text.includes("four") && !text.includes("3") && !text.includes("4")
    ) {
      return 2;
    }

    // Option 3 triggers
    if (
      /\b(three|3|third|third option|option three|option 3|option c|c|see|sea|tree|free|త్రీ|మూడు|మూడవ|థర్డ్)\b/i.test(text) &&
      !text.includes("four") && !text.includes("4")
    ) {
      return 3;
    }

    // Option 4 triggers
    if (
      /\b(four|4|fourth|fourth option|option four|option 4|option d|d|dee|for|fore|ఫోర్|నాలుగు|నాలుగవ)\b/i.test(text)
    ) {
      return 4;
    }

    return null;
  }

  parseCommandFromText(transcript) {
    const text = transcript.toLowerCase();
    if (text.includes("repeat") || text.includes("again") || text.includes("మళ్ళీ") || text.includes("మళ్లీ")) return 'repeat';
    if (text.includes("skip") || text.includes("దాటు") || text.includes("వద్దు")) return 'skip';
    if (text.includes("next") || text.includes("తరువాత") || text.includes("నెక్స్ట్")) return 'next';
    if (text.includes("stop") || text.includes("pause") || text.includes("ఆపు")) return 'stop';
    return null;
  }
}

export const voiceExaminer = new VoiceExaminer();
