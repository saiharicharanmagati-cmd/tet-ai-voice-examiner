# 🎓 TET Master - Strict AI Voice Examiner Platform (Paper 1A)

> A voice-interactive MCQ examination and revision platform for Teacher Eligibility Test (TET) Paper 1A aspirants across all five core subjects: **English**, **తెలుగు (Telugu)**, **EVS (Environmental Studies)**, **Mathematics**, and **CDP (Child Development & Pedagogy)**.

---

## 🌟 Key Highlights

- **100% Multiple Choice Questions (MCQs)**: No descriptive or open-ended questions. Every question adheres strictly to the official TET Paper 1A syllabus with 4 options.
- **Strict Voice Examiner (Zero Hints Policy)**:
  - The talkative AI Examiner speaks each question and its 4 options out loud with a measured, authoritative cadence.
  - Zero hints, clues, or second chances.
  - As soon as you answer, the system delivers a firm verdict:
    - **Correct**: Validates your choice with a harmonic chime and immediate positive confirmation.
    - **Wrong**: Issues an error buzzer, firmly states that your choice is incorrect, reveals the exact correct option, and explains the rationale.
- **Hands-Free Speech-to-Text (Voice Input)**:
  - Real-time interim speech recognition catches your spoken option (`Option 1`, `Two`, `Three`, `Four`, `A`, `B`, `C`, `D`, `ఒకటి`, `రెండు`, `మూడు`, `నాలుగు`, or direct answer keywords like `"Coins"` or `"Iodine"`).
  - Built-in **Live Microphone Level (VU) Meter** so you can visually verify that your microphone is receiving your voice clearly.
- **All 5 Official Subjects Included**:
  1. **🔤 English Language**: Synonyms, Antonyms, Spellings, Idioms, Phrasal Verbs, Tenses, Figures of Speech, Direct/Indirect Speech, Prepositions, and English Pedagogy (LAD, TPR, GTM, Skimming/Scanning, ZPD).
  2. **📜 తెలుగు (Telugu Language)**: అపరిచిత పద్యాలు, గద్యాలు, కవులు-బిరుదులు (నన్నయ, తిక్కన, అన్నమయ్య, శ్రీశ్రీ), సంధులు, సమాసాలు, విభక్తులు, ఛందస్సు, వర్ణోత్పత్తి, మరియు బోధనా పద్ధతులు.
  3. **🌿 EVS (Environmental Studies)**: Plant & Animal Biology, Human Physiology, Vitamins & Minerals, Physics (Optics, Mechanics, Electricity), Chemistry (Acids & Bases, Metals), Indian Constitution & History, and EVS Pedagogy.
  4. **📐 Mathematics**: Divisibility rules, Number Systems, HCF/LCM, Squares & Cubes, Ratios, Percentages, Simple & Compound Interest, Geometry & Mensuration, and Maths Pedagogy.
  5. **🧠 CDP (Child Development & Pedagogy)**: Piaget's Cognitive Development, Kohlberg's Moral Development, Vygotsky, Chomsky's LAD, Gardner's Multiple Intelligences, Defense Mechanisms, Learning Disabilities (Dyslexia, Dysgraphia, Dyscalculia), NEP 2020, and CCE.
- **Mistake Revision Vault**:
  - Automatically captures any question you get wrong into a dedicated revision vault so you can re-test yourself until you achieve 100% firm mastery.
- **Multi-Device Support (Laptop & Mobile Phone)**:
  - Dual HTTP (`:8080`) and HTTPS (`:8443`) server allows you to test on both your laptop browser and your mobile phone over Wi-Fi with an instant QR code.

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8+ (or any modern web browser with HTML5 Web Speech support like Google Chrome or Microsoft Edge).

### Running Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/tet-voice-examiner.git
   cd tet-voice-examiner
   ```

2. **Start the local server**:
   ```bash
   python server.py
   ```

3. **Open in Browser**:
   - **Laptop / PC**: Open [http://localhost:8080](http://localhost:8080)
   - **Mobile Phone (Same Wi-Fi)**: Open `https://<YOUR_LOCAL_IP>:8443` (or scan the on-screen QR Code).
     *(Mobile browsers require HTTPS to allow microphone permissions).*

---

## 🎙️ How to Answer Questions

1. Select a subject (**English**, **Telugu**, **EVS**, **Maths**, or **CDP**).
2. Click on any question in the left Question Browser list.
3. The AI Voice Examiner will speak the question and its 4 options out loud.
4. **Answer by Voice**:
   - Tap **"Speak Your Answer"** (or let auto-listen engage).
   - Say: *"Option 1"*, *"Option 2"*, *"Option 3"*, or *"Option 4"*.
   - Or say the letter: *"A"*, *"B"*, *"C"*, or *"D"*.
   - Or in Telugu: *"ఒకటి"*, *"రెండు"*, *"మూడు"*, *"నాలుగు"*.
   - Or say the keyword (e.g. *"Coins"* or *"Iodine"*).
5. **Answer by Click**:
   - Alternatively, tap any of the 4 option cards on the screen for instant strict evaluation.

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
| :--- | :--- |
| `1` / `2` / `3` / `4` or `A` / `B` / `C` / `D` | Choose Option 1, 2, 3, or 4 |
| `R` | Repeat / Speak Question |
| `V` | Start Microphone Voice Answer |
| `Space` or `→` | Next Question |
| `←` | Previous Question |

---

## 📁 Repository Structure

```
├── index.html                 # Main single-page application
├── css/
│   └── style.css              # Modern glassmorphism UI & responsive styling
├── js/
│   ├── app.js                 # Application controller & UI management
│   ├── speech.js              # Strict voice examiner, TTS & Speech Recognition
│   ├── audio.js               # Web Audio API procedural sound effects & VU meter
│   └── data.js                # Question bank repository loader
├── data/
│   ├── english.json           # English Language MCQs
│   ├── telugu.json            # Telugu Language MCQs
│   ├── evs.json               # Environmental Studies MCQs
│   ├── maths.json             # Mathematics MCQs
│   ├── cdp.json               # Child Development & Pedagogy MCQs
│   └── all_subjects.json      # Combined question catalog
├── server.py                  # Dual HTTP/HTTPS server with LAN IP & SSL support
└── README.md                  # Project documentation
```

---

## 📜 License

MIT License. Open for educational and test preparation use.
