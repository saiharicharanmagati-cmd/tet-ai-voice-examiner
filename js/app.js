// TET Master - Strict AI Voice Examiner Application Controller
import { questionRepo } from './data.js';
import { voiceExaminer } from './speech.js';
import { soundFX } from './audio.js';

class AppController {
  constructor() {
    this.currentSubject = 'English';
    this.currentMode = 'viva'; // 'viva' | 'practice' | 'vault'
    this.currentTopic = 'all';
    this.searchQuery = '';
    this.currentIndex = 0;
    this.currentQuestionList = [];
    this.userAnswers = {}; // { questionKey: { selectedOption, isCorrect, timestamp } }
    this.mistakeVault = JSON.parse(localStorage.getItem('tet_mistake_vault') || '[]');
    this.bookmarks = JSON.parse(localStorage.getItem('tet_bookmarks') || '[]');
    this.isAnswerEvaluated = false;
    this.autoAdvance = true;
    this.autoViva = true;

    // DOM Elements Cache
    this.dom = {};
  }

  async init() {
    this.cacheDom();
    this.bindEvents();
    this.setupVoiceCallbacks();

    // Load question repository
    await questionRepo.loadAll();
    this.updateSubjectCounts();
    this.updateTopicDropdown();
    this.loadQuestionSet();
    this.initQRCode();
    this.populateVoiceSelect();

    console.log("🎓 TET Strict AI Voice Examiner ready!");
  }

  cacheDom() {
    this.dom = {
      modeViva: document.getElementById('modeViva'),
      modePractice: document.getElementById('modePractice'),
      modeVault: document.getElementById('modeVault'),
      vaultBadge: document.getElementById('vaultBadge'),
      subjectPills: document.querySelectorAll('.sub-tab, .subject-pill'),
      userSpeechRow: document.getElementById('userSpeechRow'),
      topicSelect: document.getElementById('topicSelect'),
      searchInput: document.getElementById('searchInput'),
      browserSubjectTitle: document.getElementById('browserSubjectTitle'),
      browserCountBadge: document.getElementById('browserCountBadge'),
      questionsScrollList: document.getElementById('questionsScrollList'),
      currentSubjectTag: document.getElementById('currentSubjectTag'),
      currentTopicTag: document.getElementById('currentTopicTag'),
      questionCounter: document.getElementById('questionCounter'),
      questionProgressFill: document.getElementById('questionProgressFill'),
      questionText: document.getElementById('questionText'),
      optionsGrid: document.getElementById('optionsGrid'),
      feedbackPanel: document.getElementById('feedbackPanel'),
      feedbackHeader: document.getElementById('feedbackHeader'),
      feedbackIcon: document.getElementById('feedbackIcon'),
      feedbackTitle: document.getElementById('feedbackTitle'),
      feedbackCorrectAnswer: document.getElementById('feedbackCorrectAnswer'),
      feedbackExplanation: document.getElementById('feedbackExplanation'),
      btnPrev: document.getElementById('btnPrev'),
      btnNext: document.getElementById('btnNext'),
      btnAutoViva: document.getElementById('btnAutoViva'),
      btnAskVoice: document.getElementById('btnAskVoice'),
      btnVoiceAnswer: document.getElementById('btnVoiceAnswer'),
      btnRepeatVoice: document.getElementById('btnRepeatVoice'),
      btnStopVoice: document.getElementById('btnStopVoice'),
      examinerOrb: document.getElementById('examinerOrb'),
      examinerStatus: document.getElementById('examinerStatus'),
      voiceStatusBadge: document.getElementById('voiceStatusBadge'),
      visualizer: document.querySelector('.visualizer-container'),
      aiSpeechText: document.getElementById('aiSpeechText'),
      userSpeechText: document.getElementById('userSpeechText'),
      statAccuracy: document.getElementById('statAccuracy'),
      statCorrect: document.getElementById('statCorrect'),
      statWrong: document.getElementById('statWrong'),
      statAnswered: document.getElementById('statAnswered'),
      btnPhoneConnect: document.getElementById('btnPhoneConnect'),
      phoneModal: document.getElementById('phoneModal'),
      btnClosePhoneModal: document.getElementById('btnClosePhoneModal'),
      btnCopyPhoneUrl: document.getElementById('btnCopyPhoneUrl'),
      phoneUrlInput: document.getElementById('phoneUrlInput'),
      btnVoiceSettings: document.getElementById('btnVoiceSettings'),
      settingsModal: document.getElementById('settingsModal'),
      btnCloseSettings: document.getElementById('btnCloseSettings'),
      voiceSelect: document.getElementById('voiceSelect'),
      voiceRate: document.getElementById('voiceRate'),
      rateVal: document.getElementById('rateVal'),
      voicePitch: document.getElementById('voicePitch'),
      pitchVal: document.getElementById('pitchVal'),
      checkAutoListen: document.getElementById('checkAutoListen'),
      checkAutoAdvance: document.getElementById('checkAutoAdvance'),
      checkSoundFX: document.getElementById('checkSoundFX'),
      btnBookmark: document.getElementById('btnBookmark'),
      btnRandomQuestion: document.getElementById('btnRandomQuestion')
    };
  }

  bindEvents() {
    // Mode tabs
    [this.dom.modeViva, this.dom.modePractice, this.dom.modeVault].forEach(tab => {
      tab.addEventListener('click', () => {
        [this.dom.modeViva, this.dom.modePractice, this.dom.modeVault].forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        this.currentMode = tab.dataset.mode;
        this.loadQuestionSet();
      });
    });

    // Subject pills
    this.dom.subjectPills.forEach(pill => {
      pill.addEventListener('click', () => {
        this.dom.subjectPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        this.currentSubject = pill.dataset.subject;
        this.dom.browserSubjectTitle.textContent = this.currentSubject;
        voiceExaminer.setLanguage(this.currentSubject === 'Telugu' ? 'te' : 'en');
        this.updateTopicDropdown();
        this.loadQuestionSet();
      });
    });

    // Search input
    this.dom.searchInput.addEventListener('input', (e) => {
      this.searchQuery = e.target.value.toLowerCase().trim();
      this.loadQuestionSet();
    });

    // Topic filter
    this.dom.topicSelect.addEventListener('change', (e) => {
      this.currentTopic = e.target.value;
      this.loadQuestionSet();
    });

    // Navigation buttons
    this.dom.btnNext.addEventListener('click', () => this.nextQuestion());
    this.dom.btnPrev.addEventListener('click', () => this.prevQuestion());

    // Auto-advance viva toggle
    this.dom.btnAutoViva.addEventListener('click', () => {
      this.autoViva = !this.autoViva;
      this.dom.btnAutoViva.classList.toggle('active', this.autoViva);
      this.dom.btnAutoViva.innerHTML = this.autoViva ? 
        `<i class="fa-solid fa-pause"></i><span>Pause Viva</span>` :
        `<i class="fa-solid fa-play"></i><span>Auto-Advance Viva</span>`;
      
      if (this.autoViva && !this.isAnswerEvaluated) {
        this.speakCurrentQuestion();
      }
    });

    // Voice action buttons
    this.dom.btnAskVoice.addEventListener('click', () => this.speakCurrentQuestion());
    this.dom.btnVoiceAnswer.addEventListener('click', () => {
      soundFX.init();
      voiceExaminer.startListening();
    });
    this.dom.btnRepeatVoice.addEventListener('click', () => this.speakCurrentQuestion());
    this.dom.btnStopVoice.addEventListener('click', () => voiceExaminer.stopAll());

    // Mobile testing modal
    this.dom.btnPhoneConnect.addEventListener('click', () => {
      this.dom.phoneModal.classList.add('open');
    });
    this.dom.btnClosePhoneModal.addEventListener('click', () => {
      this.dom.phoneModal.classList.remove('open');
    });
    this.dom.phoneModal.addEventListener('click', (e) => {
      if (e.target === this.dom.phoneModal) this.dom.phoneModal.classList.remove('open');
    });

    this.dom.btnCopyPhoneUrl.addEventListener('click', () => {
      navigator.clipboard.writeText(this.dom.phoneUrlInput.value);
      this.dom.btnCopyPhoneUrl.innerHTML = `<i class="fa-solid fa-check"></i> Copied!`;
      setTimeout(() => {
        this.dom.btnCopyPhoneUrl.innerHTML = `<i class="fa-regular fa-copy"></i> Copy`;
      }, 2000);
    });

    // Settings modal
    this.dom.btnVoiceSettings.addEventListener('click', () => {
      this.dom.settingsModal.classList.add('open');
    });
    this.dom.btnCloseSettings.addEventListener('click', () => {
      this.dom.settingsModal.classList.remove('open');
    });
    this.dom.settingsModal.addEventListener('click', (e) => {
      if (e.target === this.dom.settingsModal) this.dom.settingsModal.classList.remove('open');
    });

    // Voice parameter inputs
    this.dom.voiceRate.addEventListener('input', (e) => {
      const val = parseFloat(e.target.value);
      voiceExaminer.rate = val;
      this.dom.rateVal.textContent = `${val.toFixed(2)}x`;
    });

    this.dom.voicePitch.addEventListener('input', (e) => {
      const val = parseFloat(e.target.value);
      voiceExaminer.pitch = val;
      this.dom.pitchVal.textContent = val.toFixed(2);
    });

    this.dom.checkAutoListen.addEventListener('change', (e) => {
      voiceExaminer.autoListen = e.target.checked;
    });

    this.dom.checkAutoAdvance.addEventListener('change', (e) => {
      this.autoAdvance = e.target.checked;
    });

    this.dom.checkSoundFX.addEventListener('change', (e) => {
      soundFX.enabled = e.target.checked;
    });

    this.dom.btnBookmark.addEventListener('click', () => this.toggleBookmark());
    this.dom.btnRandomQuestion.addEventListener('click', () => this.jumpToRandomQuestion());

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if (['INPUT', 'SELECT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;

      const key = e.key.toUpperCase();
      if (['1', 'A'].includes(key)) this.selectOption(1);
      else if (['2', 'B'].includes(key)) this.selectOption(2);
      else if (['3', 'C'].includes(key)) this.selectOption(3);
      else if (['4', 'D'].includes(key)) this.selectOption(4);
      else if (key === 'ARROWLEFT') this.prevQuestion();
      else if (key === 'ARROWRIGHT' || key === ' ') {
        e.preventDefault();
        this.nextQuestion();
      }
      else if (key === 'R') this.speakCurrentQuestion();
      else if (key === 'V') voiceExaminer.startListening();
    });
  }

  setupVoiceCallbacks() {
    voiceExaminer.onStateChange = (state) => {
      if (this.dom.examinerOrb) this.dom.examinerOrb.className = `examiner-avatar-box ${state}`;
      if (this.dom.voiceStatusBadge) this.dom.voiceStatusBadge.className = `voice-badge ${state}`;
      if (this.dom.btnVoiceAnswer) this.dom.btnVoiceAnswer.classList.toggle('listening', state === 'listening');

      if (state === 'speaking') {
        if (this.dom.examinerStatus) this.dom.examinerStatus.textContent = "Examiner reading question and options...";
        if (this.dom.voiceStatusBadge) this.dom.voiceStatusBadge.querySelector('.status-label').textContent = "Speaking";
        if (this.dom.visualizer) this.dom.visualizer.className = "visualizer-container active-speaking";
        if (this.dom.micLevelContainer) this.dom.micLevelContainer.style.display = 'none';
        if (this.dom.userSpeechRow) this.dom.userSpeechRow.style.display = 'none';
      } else if (state === 'listening') {
        if (this.dom.examinerStatus) this.dom.examinerStatus.textContent = "Strict Examiner listening... Speak Option 1, 2, 3, or 4";
        if (this.dom.voiceStatusBadge) this.dom.voiceStatusBadge.querySelector('.status-label').textContent = "Listening";
        if (this.dom.visualizer) this.dom.visualizer.className = "visualizer-container active-listening";
        if (this.dom.micLevelContainer) this.dom.micLevelContainer.style.display = 'flex';
        if (this.dom.userSpeechRow) this.dom.userSpeechRow.style.display = 'flex';
        if (this.dom.userSpeechText) this.dom.userSpeechText.textContent = "(Listening... say 'Option 1', 'Option 2', or your answer)";
      } else {
        if (this.dom.examinerStatus) this.dom.examinerStatus.textContent = "Examiner ready to test";
        if (this.dom.voiceStatusBadge) this.dom.voiceStatusBadge.querySelector('.status-label').textContent = "Standby";
        if (this.dom.visualizer) this.dom.visualizer.className = "visualizer-container";
        if (this.dom.micLevelContainer) this.dom.micLevelContainer.style.display = 'none';
      }
    };

    voiceExaminer.onMicLevel = (lvl) => {
      if (this.dom.micLevelFill) {
        this.dom.micLevelFill.style.width = `${Math.min(100, Math.max(5, lvl * 1.6))}%`;
      }
      if (this.dom.micLevelVal) {
        this.dom.micLevelVal.textContent = `${lvl}%`;
      }
    };

    voiceExaminer.onSpeechInterim = (text) => {
      this.dom.userSpeechText.textContent = `"${text}" (listening...)`;

      // Check option content matching in real-time
      const q = this.getCurrentQuestion();
      if (q && !this.isAnswerEvaluated) {
        const lower = text.toLowerCase();
        for (let i = 0; i < q.options.length; i++) {
          const optLower = q.options[i].toLowerCase();
          const cleanOpt = optLower.replace(/\(.*\)/, '').trim();
          if (cleanOpt.length >= 3 && lower.includes(cleanOpt)) {
            console.log(`🎯 Real-time match on interim speech: "${cleanOpt}" -> Option ${i + 1}`);
            voiceExaminer.stopListening();
            this.selectOption(i + 1);
            return;
          }
        }
      }
    };

    voiceExaminer.onSpeechRecognized = (transcript) => {
      this.dom.userSpeechText.textContent = `"${transcript}"`;

      const q = this.getCurrentQuestion();
      if (q && !this.isAnswerEvaluated) {
        const lower = transcript.toLowerCase();
        for (let i = 0; i < q.options.length; i++) {
          const optLower = q.options[i].toLowerCase();
          const cleanOpt = optLower.replace(/\(.*\)/, '').trim();
          if (cleanOpt.length >= 3 && lower.includes(cleanOpt)) {
            voiceExaminer.stopListening();
            this.selectOption(i + 1);
            return;
          }
        }
      }
    };

    voiceExaminer.onAnswerDetected = (optionIndex) => {
      console.log(`🎙️ Voice answer detected: Option ${optionIndex}`);
      this.selectOption(optionIndex);
    };

    voiceExaminer.onCommandDetected = (command) => {
      if (command === 'repeat') this.speakCurrentQuestion();
      else if (command === 'next' || command === 'skip') this.nextQuestion();
      else if (command === 'stop') voiceExaminer.stopAll();
    };

    voiceExaminer.onPermissionError = (msg) => {
      if (this.dom.micAlertBanner) {
        this.dom.micAlertBanner.style.display = 'flex';
        const txtEl = document.getElementById('micAlertText');
        if (txtEl) txtEl.textContent = msg;
      }
    };
  }

  populateVoiceSelect() {
    const voices = window.speechSynthesis.getVoices();
    this.dom.voiceSelect.innerHTML = '';
    voices.forEach((v, i) => {
      const opt = document.createElement('option');
      opt.value = i;
      opt.textContent = `${v.name} (${v.lang})`;
      if (voiceExaminer.selectedVoice && v.name === voiceExaminer.selectedVoice.name) {
        opt.selected = true;
      }
      this.dom.voiceSelect.appendChild(opt);
    });

    this.dom.voiceSelect.addEventListener('change', (e) => {
      const idx = parseInt(e.target.value);
      voiceExaminer.selectedVoice = voices[idx];
    });
  }

  updateSubjectCounts() {
    document.getElementById('countEnglish').textContent = `${questionRepo.getBySubject('English').length} Qs`;
    document.getElementById('countTelugu').textContent = `${questionRepo.getBySubject('Telugu').length} Qs`;
    document.getElementById('countEVS').textContent = `${questionRepo.getBySubject('EVS').length} Qs`;
    document.getElementById('countMaths').textContent = `${questionRepo.getBySubject('Maths').length} Qs`;
    document.getElementById('countCDP').textContent = `${questionRepo.getBySubject('CDP').length} Qs`;
    this.dom.vaultBadge.textContent = this.mistakeVault.length;
  }

  updateTopicDropdown() {
    const topics = questionRepo.getTopics(this.currentSubject);
    this.dom.topicSelect.innerHTML = '<option value="all">All Topics</option>';
    topics.forEach(t => {
      const opt = document.createElement('option');
      opt.value = t;
      opt.textContent = t;
      this.dom.topicSelect.appendChild(opt);
    });
  }

  loadQuestionSet() {
    if (this.currentMode === 'vault') {
      this.currentQuestionList = [...this.mistakeVault];
      this.dom.browserSubjectTitle.textContent = "Mistake Vault";
      if (this.currentQuestionList.length === 0) {
        this.dom.browserCountBadge.textContent = "0 Questions";
        this.dom.questionsScrollList.innerHTML = '<div style="padding: 20px; text-align: center; color: var(--text-muted);">No wrong questions yet! Practice questions to review mistakes here.</div>';
        this.dom.questionText.textContent = "Your Mistake Vault is clear! You have no pending mistakes to revise.";
        this.dom.optionsGrid.innerHTML = '';
        this.dom.feedbackPanel.style.display = 'none';
        return;
      }
    } else {
      let list = questionRepo.getBySubject(this.currentSubject);
      if (this.currentTopic !== 'all') {
        list = list.filter(q => q.topic === this.currentTopic);
      }
      if (this.searchQuery) {
        list = list.filter(q => 
          q.question.toLowerCase().includes(this.searchQuery) ||
          q.options.some(opt => opt.toLowerCase().includes(this.searchQuery))
        );
      }
      this.currentQuestionList = list;
      this.dom.browserSubjectTitle.textContent = this.currentSubject;
    }

    this.dom.browserCountBadge.textContent = `${this.currentQuestionList.length} Questions`;
    this.currentIndex = 0;
    this.renderQuestionsBrowserList();
    this.renderQuestion();
    this.updateStats();

    if (this.currentMode === 'viva' || this.autoViva) {
      setTimeout(() => this.speakCurrentQuestion(), 400);
    }
  }

  getCurrentQuestion() {
    return this.currentQuestionList[this.currentIndex];
  }

  // Render the left Questions Browser List
  renderQuestionsBrowserList() {
    this.dom.questionsScrollList.innerHTML = '';
    if (this.currentQuestionList.length === 0) {
      this.dom.questionsScrollList.innerHTML = '<div style="padding: 20px; text-align: center; color: var(--text-muted);">No matching MCQs found.</div>';
      return;
    }

    this.currentQuestionList.forEach((q, idx) => {
      const item = document.createElement('div');
      item.className = `q-list-item ${idx === this.currentIndex ? 'active' : ''}`;
      
      const key = `${q.subject || this.currentSubject}_${q.id}`;
      let statusClass = '';
      if (this.userAnswers[key]) {
        statusClass = this.userAnswers[key].isCorrect ? 'correct' : 'wrong';
      }

      item.innerHTML = `
        <div class="q-item-num">${idx + 1}</div>
        <div class="q-item-content">
          <div class="q-item-title">${q.question}</div>
          <div class="q-item-meta">
            <span class="q-item-topic">${q.topic || 'General'}</span>
            <span>4 Options</span>
          </div>
        </div>
        <div class="q-status-tag ${statusClass}"></div>
      `;

      item.addEventListener('click', () => {
        voiceExaminer.stopAll();
        this.currentIndex = idx;
        this.updateActiveListItem();
        this.renderQuestion();
        if (this.currentMode === 'viva' || this.autoViva) {
          setTimeout(() => this.speakCurrentQuestion(), 300);
        }
      });

      this.dom.questionsScrollList.appendChild(item);
    });
  }

  updateActiveListItem() {
    const items = this.dom.questionsScrollList.querySelectorAll('.q-list-item');
    items.forEach((item, idx) => {
      item.classList.toggle('active', idx === this.currentIndex);
    });

    // Ensure active item is scrolled into view
    const activeItem = items[this.currentIndex];
    if (activeItem) {
      activeItem.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }

  renderQuestion() {
    const q = this.getCurrentQuestion();
    if (!q) return;

    this.isAnswerEvaluated = false;
    this.dom.feedbackPanel.style.display = 'none';

    // Tags and headers
    this.dom.currentSubjectTag.textContent = q.subject || this.currentSubject;
    this.dom.currentTopicTag.textContent = q.topic || 'General';
    this.dom.questionCounter.textContent = `Question ${this.currentIndex + 1} of ${this.currentQuestionList.length}`;
    
    const progressPct = ((this.currentIndex + 1) / this.currentQuestionList.length) * 100;
    this.dom.questionProgressFill.style.width = `${progressPct}%`;

    // Question Text
    this.dom.questionText.textContent = q.question;
    document.body.classList.toggle('lang-telugu', (q.subject === 'Telugu' || this.currentSubject === 'Telugu'));

    // Check if already bookmarked
    const isBookmarked = this.bookmarks.some(b => b.subject === q.subject && b.id === q.id);
    this.dom.btnBookmark.classList.toggle('active', isBookmarked);

    // Populate options
    this.dom.optionsGrid.innerHTML = '';
    q.options.forEach((optText, index) => {
      const optBtn = document.createElement('button');
      optBtn.className = 'option-btn';
      optBtn.dataset.index = index + 1;

      optBtn.innerHTML = `
        <span class="opt-number">${index + 1}</span>
        <span class="opt-text">${optText}</span>
      `;

      optBtn.addEventListener('click', () => {
        this.selectOption(index + 1);
      });

      this.dom.optionsGrid.appendChild(optBtn);
    });

    // Check if previously answered
    const qKey = `${q.subject || this.currentSubject}_${q.id}`;
    if (this.userAnswers[qKey]) {
      this.displayAnswerEvaluation(this.userAnswers[qKey].selectedOption, false);
    }
  }

  selectOption(optionIndex) {
    if (this.isAnswerEvaluated) return;
    const q = this.getCurrentQuestion();
    if (!q) return;

    this.isAnswerEvaluated = true;
    const isCorrect = optionIndex === q.answer;
    const qKey = `${q.subject || this.currentSubject}_${q.id}`;

    // Store user answer
    this.userAnswers[qKey] = {
      selectedOption: optionIndex,
      isCorrect: isCorrect,
      timestamp: Date.now()
    };

    // Update mistake vault
    if (!isCorrect) {
      if (!this.mistakeVault.some(m => m.subject === q.subject && m.id === q.id)) {
        this.mistakeVault.push(q);
        localStorage.setItem('tet_mistake_vault', JSON.stringify(this.mistakeVault));
        this.dom.vaultBadge.textContent = this.mistakeVault.length;
      }
    } else {
      // If answered correctly in vault mode, remove it
      if (this.currentMode === 'vault') {
        this.mistakeVault = this.mistakeVault.filter(m => !(m.subject === q.subject && m.id === q.id));
        localStorage.setItem('tet_mistake_vault', JSON.stringify(this.mistakeVault));
        this.dom.vaultBadge.textContent = this.mistakeVault.length;
      }
    }

    this.displayAnswerEvaluation(optionIndex, true);
    this.updateStats();
    this.updateQuestionListItemStatus(this.currentIndex, isCorrect);
  }

  displayAnswerEvaluation(selectedOption, triggerVoice = true) {
    const q = this.getCurrentQuestion();
    const isCorrect = selectedOption === q.answer;

    // Visual button states
    const optButtons = this.dom.optionsGrid.querySelectorAll('.option-btn');
    optButtons.forEach(btn => {
      btn.classList.add('disabled');
      const idx = parseInt(btn.dataset.index);
      if (idx === q.answer) {
        btn.classList.add('correct');
      } else if (idx === selectedOption && !isCorrect) {
        btn.classList.add('wrong');
      }
    });

    // Feedback Panel
    this.dom.feedbackPanel.style.display = 'flex';
    this.dom.feedbackPanel.className = `feedback-panel ${isCorrect ? 'correct-panel' : 'wrong-panel'}`;

    if (isCorrect) {
      this.dom.feedbackIcon.innerHTML = `<i class="fa-solid fa-circle-check"></i>`;
      this.dom.feedbackTitle.textContent = "STRICT EVALUATION: CORRECT!";
      this.dom.feedbackCorrectAnswer.textContent = `Option ${selectedOption}: "${q.options[selectedOption - 1]}" is right.`;
    } else {
      this.dom.feedbackIcon.innerHTML = `<i class="fa-solid fa-circle-xmark"></i>`;
      this.dom.feedbackTitle.textContent = "STRICT EVALUATION: WRONG!";
      this.dom.feedbackCorrectAnswer.textContent = `Correct Answer: Option ${q.answer} - "${q.options[q.answer - 1]}"`;
    }

    this.dom.feedbackExplanation.textContent = q.explanation || "Official TET key reference.";

    // Strict Voice Response
    if (triggerVoice) {
      voiceExaminer.evaluateAnswer(selectedOption, q.answer, q, () => {
        if ((this.autoAdvance || this.autoViva) && isCorrect) {
          setTimeout(() => {
            if (this.currentIndex < this.currentQuestionList.length - 1) {
              this.nextQuestion();
            }
          }, 800);
        }
      });
    }
  }

  speakCurrentQuestion() {
    const q = this.getCurrentQuestion();
    if (!q) return;

    this.dom.aiSpeechText.textContent = `Question ${this.currentIndex + 1}: ${q.question}`;
    voiceExaminer.askQuestion(q, this.currentIndex + 1, this.currentQuestionList.length);
  }

  nextQuestion() {
    voiceExaminer.stopAll();
    if (this.currentIndex < this.currentQuestionList.length - 1) {
      this.currentIndex++;
      this.updateActiveListItem();
      this.renderQuestion();
      if (this.currentMode === 'viva' || this.autoViva) {
        setTimeout(() => this.speakCurrentQuestion(), 300);
      }
    } else {
      voiceExaminer.speak("You have completed all questions in this session. Excellent revision.");
    }
  }

  prevQuestion() {
    voiceExaminer.stopAll();
    if (this.currentIndex > 0) {
      this.currentIndex--;
      this.updateActiveListItem();
      this.renderQuestion();
      if (this.currentMode === 'viva' || this.autoViva) {
        setTimeout(() => this.speakCurrentQuestion(), 300);
      }
    }
  }

  jumpToRandomQuestion() {
    if (this.currentQuestionList.length <= 1) return;
    const randomIdx = Math.floor(Math.random() * this.currentQuestionList.length);
    this.currentIndex = randomIdx;
    this.updateActiveListItem();
    this.renderQuestion();
    if (this.currentMode === 'viva' || this.autoViva) {
      setTimeout(() => this.speakCurrentQuestion(), 300);
    }
  }

  toggleBookmark() {
    const q = this.getCurrentQuestion();
    if (!q) return;
    const idx = this.bookmarks.findIndex(b => b.subject === q.subject && b.id === q.id);
    if (idx >= 0) {
      this.bookmarks.splice(idx, 1);
      this.dom.btnBookmark.classList.remove('active');
    } else {
      this.bookmarks.push(q);
      this.dom.btnBookmark.classList.add('active');
    }
    localStorage.setItem('tet_bookmarks', JSON.stringify(this.bookmarks));
  }

  updateStats() {
    let correct = 0;
    let wrong = 0;
    let answered = 0;

    this.currentQuestionList.forEach(q => {
      const key = `${q.subject || this.currentSubject}_${q.id}`;
      if (this.userAnswers[key]) {
        answered++;
        if (this.userAnswers[key].isCorrect) correct++;
        else wrong++;
      }
    });

    const acc = answered > 0 ? Math.round((correct / answered) * 100) : 0;
    this.dom.statAccuracy.textContent = `${acc}%`;
    this.dom.statCorrect.textContent = correct;
    this.dom.statWrong.textContent = wrong;
    this.dom.statAnswered.textContent = answered;
  }

  updateQuestionListItemStatus(index, isCorrect) {
    const items = this.dom.questionsScrollList.querySelectorAll('.q-list-item');
    if (items[index]) {
      const statusTag = items[index].querySelector('.q-status-tag');
      if (statusTag) {
        statusTag.className = `q-status-tag ${isCorrect ? 'correct' : 'wrong'}`;
      }
    }
  }

  initQRCode() {
    const hostIp = "192.168.0.102";
    const httpsUrl = `https://${hostIp}:8443`;
    const httpUrl = `http://${hostIp}:8080`;

    if (this.dom.phoneUrlInput) this.dom.phoneUrlInput.value = httpsUrl;
    const httpInput = document.getElementById('phoneHttpUrlInput');
    if (httpInput) httpInput.value = httpUrl;

    const btnCopyHttp = document.getElementById('btnCopyHttpUrl');
    if (btnCopyHttp && httpInput) {
      btnCopyHttp.addEventListener('click', () => {
        navigator.clipboard.writeText(httpInput.value);
        btnCopyHttp.innerHTML = `<i class="fa-solid fa-check"></i> Copied!`;
        setTimeout(() => {
          btnCopyHttp.innerHTML = `<i class="fa-regular fa-copy"></i> Copy`;
        }, 2000);
      });
    }

    const qrContainer = document.getElementById('qrcode');
    if (qrContainer && window.QRCode) {
      qrContainer.innerHTML = '';
      new window.QRCode(qrContainer, {
        text: httpsUrl,
        width: 180,
        height: 180,
        colorDark: "#0b0f19",
        colorLight: "#ffffff",
        correctLevel: window.QRCode.CorrectLevel.H
      });
    }
  }
}

// Instantiate and boot app
document.addEventListener('DOMContentLoaded', () => {
  const app = new AppController();
  app.init();
});
