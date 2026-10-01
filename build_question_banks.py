import json
import os

# Create data directory
os.makedirs("data", exist_ok=True)

# ----------------- ENGLISH QUESTIONS -----------------
english_questions = [
    {
        "id": 1,
        "subject": "English",
        "topic": "Synonyms",
        "question": "The scholar took two pennies from his pocket. Choose the synonym of the word 'pennies'.",
        "options": ["coins", "stones", "buttons", "pearls"],
        "answer": 1,
        "explanation": "'Pennies' refers to coins of low monetary value."
    },
    {
        "id": 2,
        "subject": "English",
        "topic": "Synonyms",
        "question": "Fortune favours the hardworking. Choose the synonym of the word 'fortune'.",
        "options": ["formula", "happiness", "courage", "luck"],
        "answer": 4,
        "explanation": "'Fortune' means chance or good luck."
    },
    {
        "id": 3,
        "subject": "English",
        "topic": "Synonyms",
        "question": "The owner of the eating house stood there, serving his customers. Choose the synonym of the word 'customers'.",
        "options": ["guardians", "custodians", "consumers", "sellers"],
        "answer": 3,
        "explanation": "'Customers' are purchasers or consumers who buy goods or services."
    },
    {
        "id": 4,
        "subject": "English",
        "topic": "Synonyms",
        "question": "Saving others from disaster is courage. Choose the synonym of the word 'disaster'.",
        "options": ["trouble", "doubt", "dissent", "confusion"],
        "answer": 1,
        "explanation": "'Disaster' refers to great trouble, catastrophe or calamity."
    },
    {
        "id": 5,
        "subject": "English",
        "topic": "Synonyms",
        "question": "The waste is chocking me. Choose the synonym of the word 'chocking'.",
        "options": ["scolding", "suffocating", "beating", "stirring"],
        "answer": 2,
        "explanation": "'Choking' or 'chocking' in this context means suffocating or obstructing breath."
    },
    {
        "id": 6,
        "subject": "English",
        "topic": "Synonyms",
        "question": "The thieves got scared and ran away from there. Choose the synonym of the word 'scared'.",
        "options": ["rushed", "searched", "worried", "unhappy"],
        "answer": 3,
        "explanation": "According to the key, 'scared' is matched to worried/frightened."
    },
    {
        "id": 7,
        "subject": "English",
        "topic": "Synonyms",
        "question": "He washed his wounds and bandaged them. Choose the synonym of the word 'wounds'.",
        "options": ["cleans", "injuries", "clothes", "limbs"],
        "answer": 2,
        "explanation": "'Wounds' are bodily injuries."
    },
    {
        "id": 8,
        "subject": "English",
        "topic": "Synonyms",
        "question": "Come to the king’s court and collect the reward. Choose the synonym of the word 'reward'.",
        "options": ["punishment", "treatment", "present", "memory"],
        "answer": 3,
        "explanation": "'Reward' means a prize, present or recompense."
    },
    {
        "id": 9,
        "subject": "English",
        "topic": "Synonyms",
        "question": "Our grandfather prepared delicious lunch for us. Choose the synonym of the word 'delicious'.",
        "options": ["uneatable", "unpalatable", "uncooked", "tasty"],
        "answer": 4,
        "explanation": "'Delicious' means highly pleasing to the taste; tasty."
    },
    {
        "id": 10,
        "subject": "English",
        "topic": "Synonyms",
        "question": "They were sure of their victory. Choose the synonym of the word 'victory'.",
        "options": ["defame", "success", "defeat", "failure"],
        "answer": 2,
        "explanation": "'Victory' means triumph or success in a contest."
    },
    {
        "id": 11,
        "subject": "English",
        "topic": "Synonyms",
        "question": "There were numerous trees on either side of the road. Choose the synonym of the word 'numerous'.",
        "options": ["countable", "much", "many", "few"],
        "answer": 3,
        "explanation": "'Numerous' indicates a large number; many."
    },
    {
        "id": 14,
        "subject": "English",
        "topic": "Synonyms",
        "question": "What present can I send from Naini Prison? Choose the appropriate synonym of 'Prison'.",
        "options": ["jailhouse", "hospital", "office", "market"],
        "answer": 1,
        "explanation": "'Prison' refers to a jailhouse or penitentiary."
    },
    {
        "id": 16,
        "subject": "English",
        "topic": "Synonyms",
        "question": "My mother was astonished to see you. Choose the synonym of the word 'astonished'.",
        "options": ["afraid", "bothered", "scared", "surprised"],
        "answer": 4,
        "explanation": "'Astonished' means greatly surprised or amazed."
    },
    {
        "id": 18,
        "subject": "English",
        "topic": "Synonyms",
        "question": "The rabbit went to the cobbler who was mending shoes. Choose the synonym of the word 'mending'.",
        "options": ["repairing", "making", "selling", "buying"],
        "answer": 1,
        "explanation": "'Mending' means restoring or repairing."
    },
    {
        "id": 22,
        "subject": "English",
        "topic": "Antonyms",
        "question": "They comforted each other. Choose the antonym of the word 'comforted'.",
        "options": ["depressed", "consoled", "lost", "cared"],
        "answer": 1,
        "explanation": "The opposite of comforting/soothing someone is depressing or distressing them."
    },
    {
        "id": 23,
        "subject": "English",
        "topic": "Antonyms",
        "question": "Tenali Rama Krishna had a huge mango garden in his backyard. Choose the antonym of the word 'huge'.",
        "options": ["very large", "very big", "massive", "tiny"],
        "answer": 4,
        "explanation": "'Huge' means very large, so its exact antonym is 'tiny'."
    },
    {
        "id": 24,
        "subject": "English",
        "topic": "Antonyms",
        "question": "Raju did not want to lose the opportunity. Choose the antonym of the word 'lose'.",
        "options": ["misplace", "be unable to find", "find", "drop"],
        "answer": 3,
        "explanation": "The opposite of 'lose' is 'find' (or gain/win)."
    },
    {
        "id": 26,
        "subject": "English",
        "topic": "Antonyms",
        "question": "King Sibi was a very kind and generous ruler. Choose the antonym of the word 'kind'.",
        "options": ["good natured", "tender-hearted", "warm-hearted", "unkind"],
        "answer": 4,
        "explanation": "The antonym of 'kind' is 'unkind'."
    },
    {
        "id": 28,
        "subject": "English",
        "topic": "Antonyms",
        "question": "The village was peaceful with fresh air. Choose the antonym of the word 'fresh'.",
        "options": ["stale", "natural", "crisp", "firm"],
        "answer": 1,
        "explanation": "The opposite of 'fresh' air or food is 'stale'."
    },
    {
        "id": 29,
        "subject": "English",
        "topic": "Antonyms",
        "question": "There are big and tall trees and dense bushes on either side of the road. Choose the antonym of the word 'dense'.",
        "options": ["thick", "sparse", "packed", "crammed"],
        "answer": 2,
        "explanation": "The opposite of 'dense' is 'sparse'."
    },
    {
        "id": 43,
        "subject": "English",
        "topic": "Spelling",
        "question": "Choose the correctly spelt word.",
        "options": ["thrishing", "thresing", "thrasaing", "threshing"],
        "answer": 4,
        "explanation": "The correct spelling is 'threshing'."
    },
    {
        "id": 47,
        "subject": "English",
        "topic": "Spelling",
        "question": "Choose the correct spelling.",
        "options": ["comitee", "commite", "commitee", "committee"],
        "answer": 4,
        "explanation": "The correct spelling is 'committee' (double m, double t, double e)."
    },
    {
        "id": 64,
        "subject": "English",
        "topic": "One Word Substitutes",
        "question": "The word for a continuous dry weather period without rainfall is:",
        "options": ["sweat", "drought", "weed", "dough"],
        "answer": 2,
        "explanation": "A prolonged period of abnormally low rainfall is a 'drought'."
    },
    {
        "id": 67,
        "subject": "English",
        "topic": "One Word Substitutes",
        "question": "People who work for an organisation without being paid, are called _____.",
        "options": ["friends", "volunteers", "colleagues", "disciples"],
        "answer": 2,
        "explanation": "Unpaid workers offering service are called 'volunteers'."
    },
    {
        "id": 75,
        "subject": "English",
        "topic": "One Word Substitutes",
        "question": "A _____ makes or mends shoes.",
        "options": ["cobbler", "barber", "biker", "driver"],
        "answer": 1,
        "explanation": "A person whose job is mending and repairing shoes is a 'cobbler'."
    },
    {
        "id": 78,
        "subject": "English",
        "topic": "One Word Substitutes",
        "question": "A bunch of flowers is called _____.",
        "options": ["A bouquet", "A banquet", "A garland", "A basket"],
        "answer": 1,
        "explanation": "An attractively arranged bunch of flowers is 'a bouquet'."
    },
    {
        "id": 85,
        "subject": "English",
        "topic": "Figures of Speech",
        "question": "They eat like wolves. Identify the figure of speech used in the given sentence.",
        "options": ["Simile", "Metaphor", "Personification", "Paradox"],
        "answer": 1,
        "explanation": "Comparison using 'like' or 'as' is a Simile."
    },
    {
        "id": 102,
        "subject": "English",
        "topic": "Figures of Speech",
        "question": "The camel is the ship of the desert. Choose the figure of speech used in the given sentence.",
        "options": ["Simile", "Metaphor", "Personification", "Apostrophe"],
        "answer": 2,
        "explanation": "Direct comparison without 'like' or 'as' is a Metaphor."
    },
    {
        "id": 107,
        "subject": "English",
        "topic": "Idioms",
        "question": "Choose the correct idiomatic expression.",
        "options": ["fish out of air", "fish out of sky", "fish out of pan", "fish out of water"],
        "answer": 4,
        "explanation": "The idiom is 'a fish out of water', meaning feeling uncomfortable in unfamiliar surroundings."
    },
    {
        "id": 118,
        "subject": "English",
        "topic": "Idioms",
        "question": "To let the ____ out of the bag. Choose the correct word to make it an idiom that means to reveal a secret.",
        "options": ["rat", "bat", "mat", "cat"],
        "answer": 4,
        "explanation": "'Let the cat out of the bag' means to inadvertently reveal a secret."
    },
    {
        "id": 126,
        "subject": "English",
        "topic": "Idioms",
        "question": "You have hit the nail on the head. Choose the meaning of the underlined idiom.",
        "options": ["damaging a nail", "breaking someone’s head", "disclosing the secrets", "said or done exactly the right thing"],
        "answer": 4,
        "explanation": "'Hit the nail on the head' means to say or do exactly the right thing."
    },
    {
        "id": 131,
        "subject": "English",
        "topic": "Phrasal Verbs",
        "question": "The plane took off an hour late. Choose the correct meaning of phrasal verb 'took off'.",
        "options": ["began to fly", "landed", "postponed", "arrive at"],
        "answer": 1,
        "explanation": "For an aircraft, to 'take off' means to become airborne / began to fly."
    },
    {
        "id": 143,
        "subject": "English",
        "topic": "Phrasal Verbs",
        "question": "The game was cancelled because of bad weather. Choose the correct phrasal verb for the word 'cancelled'.",
        "options": ["called on", "called off", "called out", "called after"],
        "answer": 2,
        "explanation": "'Called off' means cancelled."
    },
    {
        "id": 148,
        "subject": "English",
        "topic": "Language Functions",
        "question": "May I come in? Choose the language function of the given sentence.",
        "options": ["Giving permission", "Obligation", "Seeking permission", "Suggestion"],
        "answer": 3,
        "explanation": "'May I come in?' is used for seeking permission."
    },
    {
        "id": 149,
        "subject": "English",
        "topic": "Modal Verbs",
        "question": "Choose the modal verb used for obligation: You ____ be regular.",
        "options": ["will", "can", "may", "must"],
        "answer": 4,
        "explanation": "'Must' expresses duty or obligation."
    },
    {
        "id": 165,
        "subject": "English",
        "topic": "Modal Verbs",
        "question": "Choose the modal verb to convey 'ability': She ______ speak Tamil.",
        "options": ["shall", "will", "should", "can"],
        "answer": 4,
        "explanation": "'Can' expresses present ability."
    },
    {
        "id": 169,
        "subject": "English",
        "topic": "Grammar & Usage",
        "question": "Identify the grammatically correct sentence.",
        "options": [
            "The players have going to the playground.",
            "The players has going to the playground.",
            "The players had going to the playground.",
            "The players are going to the playground."
        ],
        "answer": 4,
        "explanation": "'The players are going to the playground' correctly uses the present continuous tense."
    },
    {
        "id": 171,
        "subject": "English",
        "topic": "Grammar & Usage",
        "question": "Identify the grammatically correct sentence.",
        "options": [
            "Stephen is one of the best singers.",
            "Stephen are one of the best singers.",
            "Stephen have one of the best singers.",
            "Stephen will one of the best singers."
        ],
        "answer": 1,
        "explanation": "'Stephen is one of the best singers' agrees in subject and verb."
    },
    {
        "id": 183,
        "subject": "English",
        "topic": "Subject-Verb Agreement",
        "question": "Identify the grammatically correct sentence.",
        "options": [
            "Neither the chairman nor the directors are present.",
            "Neither the chairman nor the directors was present.",
            "Neither the chairman nor the directors has present.",
            "Neither the chairman nor the directors have present."
        ],
        "answer": 1,
        "explanation": "In 'neither... nor', the verb agrees with the nearer subject ('directors' is plural -> 'are present')."
    },
    {
        "id": 232,
        "subject": "English",
        "topic": "Direct & Indirect Speech",
        "question": "Direct: He said, 'My master is writing letters.' Indirect: He said that _____ master ____ writing letters.",
        "options": ["his, was", "their, is", "the, has been", "her, is"],
        "answer": 1,
        "explanation": "Present continuous 'is writing' changes to past continuous 'was writing', and 'My' changes to 'his'."
    },
    {
        "id": 253,
        "subject": "English",
        "topic": "Prepositions",
        "question": "Our school starts _____ 8.45 am. Choose the correct preposition.",
        "options": ["in", "on", "of", "at"],
        "answer": 4,
        "explanation": "We use preposition 'at' with specific clock times."
    },
    {
        "id": 254,
        "subject": "English",
        "topic": "Prepositions",
        "question": "Vivekananda was born ____ 12th January 1863. Choose the correct preposition.",
        "options": ["in", "at", "on", "or"],
        "answer": 3,
        "explanation": "We use preposition 'on' with specific dates."
    },
    {
        "id": 258,
        "subject": "English",
        "topic": "Prepositions",
        "question": "Tenali Rama and his wife dropped the box ___ the well.",
        "options": ["in", "on", "into", "upon"],
        "answer": 3,
        "explanation": "'Into' denotes motion entering inside an enclosed space."
    },
    {
        "id": 297,
        "subject": "English",
        "topic": "Articles",
        "question": "If _____ earth was a human being, it would be in hospital. Choose the correct option.",
        "options": ["an", "the", "a", "No Article"],
        "answer": 2,
        "explanation": "Definite article 'the' is used before unique astronomical entities like 'the earth'."
    },
    {
        "id": 316,
        "subject": "English",
        "topic": "Voice",
        "question": "Who wrote it? Choose the correct Passive Voice.",
        "options": [
            "By whom was it written.",
            "By whom wrote it?",
            "By whom it wrote?",
            "By whom it written?"
        ],
        "answer": 1,
        "explanation": "'Who wrote it?' becomes 'By whom was it written'."
    },
    {
        "id": 320,
        "subject": "English",
        "topic": "Voice",
        "question": "They painted the house red. Choose the correct Passive Voice.",
        "options": [
            "Red was house painted by them.",
            "Red house was painted by them.",
            "The house was painted red by them.",
            "The house painted by them red."
        ],
        "answer": 3,
        "explanation": "'They painted the house red' converts to 'The house was painted red by them'."
    },
    {
        "id": 506,
        "subject": "English",
        "topic": "Pedagogy",
        "question": "At times students resort to using words from both the first and second languages in the same sentence. This is called:",
        "options": ["code separation", "code fusion", "code switching", "code joining"],
        "answer": 3,
        "explanation": "Alternating between two languages in discourse is known as code switching."
    },
    {
        "id": 507,
        "subject": "English",
        "topic": "Pedagogy",
        "question": "Which should be strengthened first before the child gets practice in reading and writing skills?",
        "options": ["Speaking skill only", "Listening skill only", "Songs & rhymes", "Listening and speaking"],
        "answer": 4,
        "explanation": "In the LSRW continuum, oral-aural skills (Listening and Speaking) precede literacy skills (Reading and Writing)."
    },
    {
        "id": 522,
        "subject": "English",
        "topic": "Pedagogy",
        "question": "LAD means:",
        "options": [
            "Literacy Acquiring Data",
            "Language Acquired Device",
            "Language Acquisition Device",
            "Language Acquisition Drive"
        ],
        "answer": 3,
        "explanation": "LAD stands for Language Acquisition Device (proposed by Noam Chomsky)."
    },
    {
        "id": 530,
        "subject": "English",
        "topic": "Pedagogy",
        "question": "Writing is a ______ skill.",
        "options": ["Receptive", "Productive", "Aural", "Fundamental"],
        "answer": 2,
        "explanation": "Speaking and Writing are productive (expressive) skills, whereas Listening and Reading are receptive skills."
    },
    {
        "id": 531,
        "subject": "English",
        "topic": "Pedagogy",
        "question": "Listening is a/an _____ skill.",
        "options": ["Receptive", "Productive", "Active", "Graphic"],
        "answer": 1,
        "explanation": "Listening is a receptive language skill."
    },
    {
        "id": 536,
        "subject": "English",
        "topic": "Pedagogy",
        "question": "Nidhi reads a magazine and is looking for the overall idea of the cover story. What is this reading known as?",
        "options": ["Reading for pleasure", "Intensive Reading", "Skimming", "Scanning"],
        "answer": 3,
        "explanation": "Reading rapidly to grasp the central overall idea/gist is 'Skimming'."
    },
    {
        "id": 550,
        "subject": "English",
        "topic": "Pedagogy",
        "question": "Which is the oldest method of teaching English in India?",
        "options": ["Bilingual Method", "Direct Method", "Dr. West New Method", "Grammar Translation Method"],
        "answer": 4,
        "explanation": "The Classical or Grammar Translation Method (GTM) is the oldest method of teaching English in India."
    },
    {
        "id": 554,
        "subject": "English",
        "topic": "Pedagogy",
        "question": "Choose the teaching method which is based on the coordination of language and physical movement.",
        "options": ["Suggestopedia", "Total Physical Response", "Silent Way", "Natural Approach"],
        "answer": 2,
        "explanation": "TPR (Total Physical Response), developed by James Asher, coordinates speech with physical action."
    },
    {
        "id": 557,
        "subject": "English",
        "topic": "Pedagogy",
        "question": "Vygotsky’s concept of _____ advocates children refine their knowledge and experience through collaboration.",
        "options": [
            "Zone of Proximal Development",
            "Zone of Peer Development",
            "Zone of Point of Discussion",
            "Zone of Proximal Discussion"
        ],
        "answer": 1,
        "explanation": "ZPD stands for Zone of Proximal Development."
    },
    {
        "id": 581,
        "subject": "English",
        "topic": "Pedagogy",
        "question": "Howard Gardner’s _____ Theory reminds teachers that there are many types of learners within the classroom.",
        "options": ["Concept of learning", "Multiple Intelligence", "Sensory store", "Connectionism"],
        "answer": 2,
        "explanation": "Howard Gardner developed the Theory of Multiple Intelligences."
    }
]

# ----------------- TELUGU QUESTIONS -----------------
telugu_questions = [
    {
        "id": 1,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం (Comprehension)",
        "question": "కష్టపెట్టబోకు కన్నతల్లి మనసు / నష్టపెట్టబోకు నాన్న పనులు / తల్లిదండ్రులన్న దైవ సన్నిభులురా / లలిత సుగుణజాల తెలుగు బాల - ఎవరి మనసు కష్టపెట్టకూడదు?",
        "options": ["నాన్న", "అమ్మ", "అక్క", "అన్న"],
        "answer": 2,
        "explanation": "పద్యంలో 'కష్టపెట్టబోకు కన్నతల్లి మనసు' అని స్పష్టంగా పేర్కొనబడింది. కాబట్టి సరైన సమాధానం అమ్మ."
    },
    {
        "id": 2,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం (Comprehension)",
        "question": "అనువుగాని చోట నధికుల మనరాదు / కొంచెముండుటెల్ల కొదువ కాదు / కొండ అద్దమందు కొంచెమై యుండదా? / విశ్వదాభిరామ వినురవేమ - అనువుగాని చోట ఎలా ఉండకూడదు?",
        "options": ["చిన్నవారిలా", "అధికులుగా", "కఠినముగా", "మూర్ఖులలా"],
        "answer": 2,
        "explanation": "'అనువుగాని చోట నధికుల మనరాదు' అనగా మనకు అనుకూలము కాని ప్రదేశంలో అధికులమని గర్వపడకూడదు."
    },
    {
        "id": 3,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం (Comprehension)",
        "question": "తల్లిదండ్రిమీద దయలేని పుత్రుండు / పుట్టనేమి వాడు గిట్టనేమి / పుట్టలోన చెదలు పుట్టవా గిట్టవా / విశ్వదాభిరామ వినురవేమ - పై పద్యం ఆధారంగా సరైనది ఏది?",
        "options": [
            "తల్లిదండ్రులు పుత్రునిపై దయచూపరాదు",
            "తల్లిదండ్రులు పుత్రుడు పుట్టాడని దయ కలిగి ఉండాలి",
            "తల్లిదండ్రుల మీద దయగల పుత్రుడు చెదపురుగువంటివాడు",
            "తల్లిదండ్రుల మీద దయలేని పుత్రుడు చెదపురుగు వంటివాడు"
        ],
        "answer": 4,
        "explanation": "తల్లిదండ్రుల మీద భక్తి, దయలేని కొడుకు పుట్టలో పుట్టి చచ్చే చెదపురుగులతో సమానం."
    },
    {
        "id": 4,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం (Comprehension)",
        "question": "వేరు పురుగు చేరి వృక్షంబు జెఱచును / చీడపురుగు చేరి చెట్టు చెఱచు / కుత్సితుండు చేరి గుణవంతు చెఱచురా / విశ్వదాభిరామ వినురవేమ - దుర్మార్గుడు వీరిని చెడగొడతాడు?",
        "options": ["నీచుడు", "గుణవంతుడు", "అదృష్టవంతుడు", "అధముడు"],
        "answer": 2,
        "explanation": "'కుత్సితుండు చేరి గుణవంతు చెఱచురా' - దుష్టుడైనవాడు గుణవంతుడిని పాడుచేస్తాడు."
    },
    {
        "id": 6,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం (Comprehension)",
        "question": "నీళ్ళలోని మొసలి నిగిడి యేనుగుబట్టు / బయట కుక్క చేత భంగపడును / స్థానబలిమిగాని తన బల్మిగాదయ్యా / విశ్వదాభిరామ వినురవేమ - నీళ్ళలోని మొసలి దేనిని నీటిలోకి లాగి చంపుతుంది?",
        "options": ["కుక్క", "గుర్రం", "జింక", "ఏనుగు"],
        "answer": 4,
        "explanation": "నీళ్ళలో బలం ఉన్న మొసలి మహాబలశాలియైన ఏనుగును కూడా పట్టుకుని లాగుతుంది."
    },
    {
        "id": 10,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం (Comprehension)",
        "question": "తలయందు విషము ఫణికిని / వెలయంగా తోకనందు వృశ్చికమునకున్ / తల తోక యనక యుండును / ఖలునకు నిలువెల్ల విషము గదరా సుమతీ! - పాముకు విషం ఎక్కడ ఉంటుంది?",
        "options": ["తోక", "శరీరమంతా", "నడుము", "తల"],
        "answer": 4,
        "explanation": "పాముకు (ఫణికి) తలలో విషం ఉంటుంది, తేలుకు తోకలో ఉంటుంది, దుర్జనునికి నిలువెల్లా విషం ఉంటుంది."
    },
    {
        "id": 12,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం (Comprehension)",
        "question": "తన కోపమె తన శత్రువు / తన శాంతమె తనకు రక్ష దయ చుట్టంబౌ / తన సంతోషమె స్వర్గము / తన దుఃఖమె నరకమండ్రు తథ్యము సుమతీ! - తన కోపం తనకు ఎలాంటిది?",
        "options": ["మిత్రుడు", "శత్రువు", "స్వర్గం", "నరకం"],
        "answer": 2,
        "explanation": "'తన కోపమె తన శత్రువు' - ఒకరి కోపమే వారికి పరమ శత్రువు."
    },
    {
        "id": 31,
        "subject": "Telugu",
        "topic": "పద్యాలు - భావాలు",
        "question": "తేలుకు విషం ఎక్కడ ఉంటుంది?",
        "options": ["తల", "శరీరమంతా", "తోక", "పైవన్నీ"],
        "answer": 3,
        "explanation": "వృశ్చికమునకు (తేలుకు) విషం తోకయందు ఉంటుంది."
    },
    {
        "id": 45,
        "subject": "Telugu",
        "topic": "గద్య భాగం (Comprehension)",
        "question": "శల్యుడు మద్ర దేశాధిపతి. పాండురాజు రెండవ భార్య అయిన మాద్రికి అన్న, నకుల సహదేవులకు మేనమామ. మద్ర దేశాధిపతి ఎవరు?",
        "options": ["మాద్రి", "నకులుడు", "సహదేవుడు", "శల్యుడు"],
        "answer": 4,
        "explanation": "గద్యం ప్రకారం మద్ర దేశాధిపతి శల్యుడు."
    },
    {
        "id": 46,
        "subject": "Telugu",
        "topic": "గద్య భాగం (Comprehension)",
        "question": "దక్షిణ భారతదేశంలోని ప్రాచీన పట్టణాలలో కుంభకోణం ఒకటి. ఇది మద్రాసు రాష్ట్రంలోని తంజావూరు జిల్లాలో కావేరీ నది ఒడ్డున ఉంది. కుంభకోణం ఉన్న రాష్ట్రం ఏది?",
        "options": ["ఆంధ్ర", "కర్ణాటక", "మద్రాసు", "కేరళ"],
        "answer": 3,
        "explanation": "గద్యం ఆధారంగా కుంభకోణం పూర్వపు మద్రాసు రాష్ట్రంలో (ప్రస్తుత తమిళనాడు) కలదు."
    },
    {
        "id": 53,
        "subject": "Telugu",
        "topic": "సాహిత్యం - కవులు",
        "question": "ఆధునికాంధ్ర కవిత్వంలో శ్రీ దేవరకొండ బాలగంగాధర తిలక్ 'అమృతం కురిసిన రాత్రి' ఒక దీపస్తంభం. దీపస్తంభం వంటి రచన ఏది?",
        "options": ["అమృతం కురిసిన రాత్రి", "మహా ప్రస్థానం", "తృణకంకణం", "వజ్రాయుధం"],
        "answer": 1,
        "explanation": "దేవరకొండ బాలగంగాధర తిలక్ రచించిన ప్రసిద్ధ కవితా సంపుటి 'అమృతం కురిసిన రాత్రి'."
    },
    {
        "id": 89,
        "subject": "Telugu",
        "topic": "సాహిత్యం - నాటకాలు",
        "question": "గురజాడ అప్పారావు గారు రచించిన గొప్ప సాంఘిక నాటకం ఏది?",
        "options": ["గాలివాన", "కన్యాశుల్కం", "భావవీణ", "వెలుగునీడ"],
        "answer": 2,
        "explanation": "గురజాడ అప్పారావు గారు రచించిన ప్రసిద్ధ యుగప్రవర్తక నాటకం 'కన్యాశుల్కం'."
    },
    {
        "id": 99,
        "subject": "Telugu",
        "topic": "సాహిత్యం - బిరుదులు",
        "question": "'పదకవితా పితామహుడు' అను బిరుదు గల వాగ్గేయకారుడు ఎవరు?",
        "options": ["త్యాగయ్య", "క్షేత్రయ్య", "రామదాసు", "అన్నమయ్య"],
        "answer": 4,
        "explanation": "తాళ్ళపాక అన్నమాచార్యులను 'పదకవితా పితామహుడు' అంటారు."
    },
    {
        "id": 105,
        "subject": "Telugu",
        "topic": "సాహిత్యం - బిరుదులు",
        "question": "కవిబ్రహ్మ, ఉభయ కవిమిత్రుడు అనే బిరుదులు కలిగిన కవి ఎవరు?",
        "options": ["నన్నయ", "ఎర్రన", "వేమన", "తిక్కన"],
        "answer": 4,
        "explanation": "తిక్కన సోమయాజికి 'కవిబ్రహ్మ', 'ఉభయ కవిమిత్రుడు' అనే బిరుదులు కలవు."
    },
    {
        "id": 265,
        "subject": "Telugu",
        "topic": "పదజాలం - అర్థాలు",
        "question": "'పద్మం' పదానికి అర్థం:",
        "options": ["గులాబి పువ్వు", "కలువ పువ్వు", "మందార పువ్వు", "తామర పువ్వు"],
        "answer": 4,
        "explanation": "పద్మము అనగా తామర పువ్వు."
    },
    {
        "id": 298,
        "subject": "Telugu",
        "topic": "ప్రకృతి - వికృతి",
        "question": "'అక్షరము' పదానికి వికృతి రూపం ఏమిటి?",
        "options": ["అక్కరము", "ఆశితులు", "ఆకారము", "అక్షరము"],
        "answer": 1,
        "explanation": "అక్షరము (ప్రకృతి) - అక్కరము (వికృతి)."
    },
    {
        "id": 402,
        "subject": "Telugu",
        "topic": "వ్యాకరణం - అక్షరాలు",
        "question": "క, చ, ట, త, ప అనే హల్లులను ఏమంటారు?",
        "options": ["సరళాలు", "స్థిరాలు", "పరుషాలు", "అంతస్థాలు"],
        "answer": 3,
        "explanation": "క, చ, ట, త, ప లను పరుషాలు అంటారు (కఠినముగా పలకబడునవి)."
    },
    {
        "id": 418,
        "subject": "Telugu",
        "topic": "వ్యాకరణం - అక్షరాలు",
        "question": "య, ర, ల, వ అనే అక్షరాలను ఏమంటారు?",
        "options": ["అనునాసికాలు", "ఊష్మాలు", "అంతస్థాలు", "మూర్ధన్యాలు"],
        "answer": 3,
        "explanation": "య, ర, ల, వ లను అంతస్థాలు అంటారు."
    },
    {
        "id": 441,
        "subject": "Telugu",
        "topic": "వ్యాకరణం - సంధులు",
        "question": "సుర + ఏక = సురైక అయితే ఇది ఏ సంధి రూపం?",
        "options": ["గుణసంధి", "సవర్ణదీర్ఘ సంధి", "యణాదేశ సంధి", "వృద్ధి సంధి"],
        "answer": 4,
        "explanation": "అ-కారమునకు ఏ, ఐ లు పరమైనపుడు 'ఐ' కారము ఏకాదేశమగును - వృద్ధి సంధి."
    },
    {
        "id": 450,
        "subject": "Telugu",
        "topic": "వ్యాకరణం - విభక్తులు",
        "question": "కింది వానిలో షష్ఠీ విభక్తి ప్రత్యయం ఏది?",
        "options": ["చేత", "వలన", "యొక్క", "కొఱకు"],
        "answer": 3,
        "explanation": "కిన్, కున్, యొక్క, లోన్, లోపలన్ - షష్ఠీ విభక్తి."
    },
    {
        "id": 506,
        "subject": "Telugu",
        "topic": "భాషా శాస్త్రం",
        "question": "డింగ్ డాంగ్ వాదమును ప్రతిపాదించిన వారు ఎవరు?",
        "options": ["మాక్సుముల్లర్", "బి ఎఫ్ స్కిన్నర్", "చామ్ స్కీ", "యాస్కాచార్యుడు"],
        "answer": 1,
        "explanation": "భాషోత్పత్తి వాదాలలో డింగ్-డాంగ్ వాదాన్ని (Ding-Dong Theory) మాక్స్ ముల్లర్ ప్రతిపాదించారు."
    },
    {
        "id": 551,
        "subject": "Telugu",
        "topic": "బోధనా పద్ధతులు",
        "question": "పద్యాన్ని మొత్తంగా తీసుకుని బోధించే పద్ధతిని ఏమంటారు?",
        "options": ["ఖండపద్ధతి", "పఠన పద్ధతి", "ఖండాన్వయ పద్ధతి", "పూర్ణపద్ధతి"],
        "answer": 4,
        "explanation": "పద్యాన్ని విడదీయకుండా సమగ్రంగా గ్రహించి బోధించే పద్ధతిని పూర్ణపద్ధతి అంటారు."
    }
]

# ----------------- EVS QUESTIONS -----------------
evs_questions = [
    {
        "id": 1,
        "subject": "EVS",
        "topic": "Plant Biology",
        "question": "This part of the plant fixes it to the ground / మొక్కలోని ఈ భాగం దానిని నేలలో స్థిరపరచును:",
        "options": ["Stem (కాండం)", "Leaf (పత్రం)", "Root (వేరు)", "Fruit (ఫలం)"],
        "answer": 3,
        "explanation": "Roots anchor the plant firmly in the soil."
    },
    {
        "id": 2,
        "subject": "EVS",
        "topic": "Plant Biology",
        "question": "This part of the plant absorbs water and minerals from soil / నేల నుండి నీటిని మరియు లవణాలను శోషించే మొక్కలోని భాగం:",
        "options": ["Stem (కాండం)", "Root (వేరు)", "Leaf (పత్రం)", "Flower (పుష్పం)"],
        "answer": 2,
        "explanation": "Roots absorb water and dissolved minerals from the ground."
    },
    {
        "id": 8,
        "subject": "EVS",
        "topic": "Plant Biology",
        "question": "This part of the plant is called as food factory / మొక్కలలో ఆహార కర్మాగారంగా పిలువబడే భాగం:",
        "options": ["Stem (కాండం)", "Leaf (పత్రం)", "Root (వేరు)", "Fruit (ఫలం)"],
        "answer": 2,
        "explanation": "Leaves prepare food through photosynthesis and are called the food factories of plants."
    },
    {
        "id": 20,
        "subject": "EVS",
        "topic": "Animal Adaptations",
        "question": "This organism has a boat-shaped body, fins, tail and gills to live in water / నీటిలో నివసించుటకు పడవ వంటి శరీరాకారం, వాజాలు, తోక మరియు మొప్పలు కలిగిన జీవి:",
        "options": ["Salamander (సాలమాండర్)", "Frog (కప్ప)", "Fish (చేప)", "Hippo (నీటి ఏనుగు)"],
        "answer": 3,
        "explanation": "Fishes possess streamlined boat-shaped bodies, fins, and gills to respire underwater."
    },
    {
        "id": 26,
        "subject": "EVS",
        "topic": "Nutrition & Vitamins",
        "question": "Sunlight is a natural source of this Vitamin / సూర్యరశ్మి వనరుగా ఉన్న విటమిన్:",
        "options": ["Vitamin A", "Vitamin B1", "Vitamin C", "Vitamin D"],
        "answer": 4,
        "explanation": "Sunlight synthesizes Vitamin D in human skin."
    },
    {
        "id": 27,
        "subject": "EVS",
        "topic": "Nutrition & Deficiency",
        "question": "This vitamin deficiency causes Scurvy / ఈ విటమిన్ లోపం వలన స్కర్వీ కలుగుతుంది:",
        "options": ["Vitamin A", "Vitamin B1", "Vitamin C", "Vitamin D"],
        "answer": 3,
        "explanation": "Deficiency of Vitamin C (ascorbic acid) causes Scurvy (bleeding gums)."
    },
    {
        "id": 28,
        "subject": "EVS",
        "topic": "Nutrition & Minerals",
        "question": "This mineral deficiency causes Goitre / ఈ ఖనిజ లవణం లోపం వలన గాయిటర్ వ్యాధి కలుగుతుంది:",
        "options": ["Iodine (అయోడిన్)", "Calcium (కాల్షియం)", "Iron (ఇనుము)", "Chlorine (క్లోరిన్)"],
        "answer": 1,
        "explanation": "Iodine deficiency in the diet leads to enlargement of the thyroid gland, called Goitre."
    },
    {
        "id": 44,
        "subject": "EVS",
        "topic": "Cell Biology",
        "question": "The term 'cell' was coined by / 'కణం' పేరును ప్రతిపాదించినవారు:",
        "options": ["Robert Brown (రాబర్ట్ బ్రౌన్)", "Robert Hooke (రాబర్ట్ హుక్)", "Leuwenhoek (లీవెన్ హుక్)", "Louis Pasteur (లూయిస్ పాశ్చర్)"],
        "answer": 2,
        "explanation": "Robert Hooke coined the term 'cell' in 1665 observing cork tissue."
    },
    {
        "id": 47,
        "subject": "EVS",
        "topic": "Cell Biology",
        "question": "The largest cell is / అతిపెద్ద కణం:",
        "options": ["Bacteria (బ్యాక్టీరియా)", "WBC (తెల్ల రక్త కణం)", "Ostrich egg (ఉష్ట్ర పక్షి గుడ్డు)", "Hen egg (కోడి గుడ్డు)"],
        "answer": 3,
        "explanation": "An unfertilized ostrich egg is the largest single biological cell known."
    },
    {
        "id": 49,
        "subject": "EVS",
        "topic": "Cell Biology",
        "question": "The most important and controlling component of a living cell is / జీవ కణంలోని అతి ముఖ్యమైన మరియు నియంత్రణ భాగము:",
        "options": ["Cytoplasm (కణద్రవ్యం)", "Cell membrane (కణత్వచం)", "Vacuole (రిక్తిక)", "Nucleus (కేంద్రకం)"],
        "answer": 4,
        "explanation": "The nucleus controls all cellular metabolic and genetic activities."
    },
    {
        "id": 52,
        "subject": "EVS",
        "topic": "Cell Biology",
        "question": "The cell organelle that is absent in animal cells / జంతు కణంలో ఉండని కణాంగము:",
        "options": ["Cell membrane (కణత్వచం)", "Mitochondria (మైటోకాండ్రియా)", "Nucleus (కేంద్రకం)", "Plastids (ప్లాస్టిడ్లు)"],
        "answer": 4,
        "explanation": "Plastids (such as chloroplasts) are present in plant cells and absent in animal cells."
    },
    {
        "id": 61,
        "subject": "EVS",
        "topic": "Microorganisms & Medicine",
        "question": "Penicillin was first prepared by / పెన్సిలిన్ ను మొదటిసారి తయారు చేసిన వారు:",
        "options": ["Ronald Ross (రోనాల్డ్ రాస్)", "Louis Pasteur (లూయిస్ పాశ్చర్)", "Alexander Flemming (అలెగ్జాండర్ ఫ్లెమింగ్)", "Edward Jenner (ఎడ్వర్డ్ జెన్నర్)"],
        "answer": 3,
        "explanation": "Sir Alexander Fleming discovered Penicillin in 1928."
    },
    {
        "id": 63,
        "subject": "EVS",
        "topic": "Health & Disease",
        "question": "Female Anopheles mosquito is the carrier of / ఆడ అనాఫిలిస్ దోమ దీనికి వాహకము:",
        "options": ["Filaria (బోదకాలు)", "Malaria (మలేరియా)", "Dengue (డెంగ్యూ)", "Typhoid (టైఫాయిడ్)"],
        "answer": 2,
        "explanation": "Female Anopheles mosquito transmits Plasmodium parasite causing Malaria."
    },
    {
        "id": 74,
        "subject": "EVS",
        "topic": "Human Physiology",
        "question": "The longest part in the human digestive system is / మానవ జీర్ణవ్యవస్థలోని అత్యంత పొడవైన భాగం:",
        "options": ["Large intestine (పెద్ద ప్రేగు)", "Oesophagus (ఆహారవాహిక)", "Small intestine (చిన్న ప్రేగు)", "Buccal cavity (ఆస్య కుహరం)"],
        "answer": 3,
        "explanation": "Small intestine is the longest part (approx. 6 meters in adults)."
    },
    {
        "id": 85,
        "subject": "EVS",
        "topic": "Human Physiology",
        "question": "The two upper chambers of heart are called / గుండె లోని పై రెండు గదులను ఇలా పిలుస్తారు:",
        "options": ["Atria (కర్ణికలు)", "Ventricles (జఠరికలు)", "Arteries (ధమనులు)", "Veins (సిరలు)"],
        "answer": 1,
        "explanation": "The upper receiving chambers of human heart are the Atria (auricles)."
    },
    {
        "id": 147,
        "subject": "EVS",
        "topic": "Physical Science - Matter",
        "question": "Metal that exists in liquid state at room temperature / గది ఉష్ణోగ్రత వద్ద ద్రవస్థితిలో ఉండే లోహం:",
        "options": ["Iron (ఇనుము)", "Mercury (పాదరసం)", "Copper (రాగి)", "Silver (వెండి)"],
        "answer": 2,
        "explanation": "Mercury (Hg) is the only metallic element liquid at standard room temperature."
    },
    {
        "id": 150,
        "subject": "EVS",
        "topic": "Physical Science - Light",
        "question": "If the angle of incidence is 30°, then the angle of reflection is / పతన కోణం 30° అయిన పరావర్తన కోణం:",
        "options": ["0°", "30°", "60°", "90°"],
        "answer": 2,
        "explanation": "According to the Law of Reflection, Angle of Incidence (i) = Angle of Reflection (r) = 30°."
    },
    {
        "id": 152,
        "subject": "EVS",
        "topic": "Human Eye",
        "question": "The most comfortable minimum distance of distinct vision for a normal eye is (in cm):",
        "options": ["2.5 cm", "250 cm", "25 cm", "2500 cm"],
        "answer": 3,
        "explanation": "The least distance of distinct vision for a healthy normal human eye is 25 cm."
    },
    {
        "id": 168,
        "subject": "EVS",
        "topic": "Physical Science - Units",
        "question": "S.I Unit of electric current / విద్యుత్ ప్రవాహానికి S.I ప్రమాణం:",
        "options": ["Volt (వోల్టు)", "Watt (వాట్)", "Joule (జౌల్)", "Ampere (ఆంపియర్)"],
        "answer": 4,
        "explanation": "The SI unit of electric current is the Ampere (A)."
    },
    {
        "id": 206,
        "subject": "EVS",
        "topic": "Magnetism",
        "question": "A freely suspended bar magnet always aligns in this direction / స్వేచ్ఛగా వేలాడదీసిన దండాయస్కాంతం ఎల్లప్పుడూ ఈ దిశలోకే వస్తుంది:",
        "options": ["North-South (ఉత్తర – దక్షిణ)", "East-West (తూర్పు – పడమర)", "North-West (ఉత్తర - పడమర)", "South-West (దక్షిణ – పడమర)"],
        "answer": 1,
        "explanation": "Earth's magnetic field directs a freely suspended bar magnet towards geographic North-South."
    },
    {
        "id": 275,
        "subject": "EVS",
        "topic": "Space Science",
        "question": "India’s first artificial satellite was / భారతదేశపు మొట్ట మొదటి కృత్రిమ ఉపగ్రహం:",
        "options": ["Aryabhata (ఆర్యభట్ట)", "INSAT (ఇన్సాట్)", "IRS (ఐ.ఆర్.యస్)", "EDUSAT (ఎడ్యుసాట్)"],
        "answer": 1,
        "explanation": "Aryabhata, launched in 1975, was India's first artificial satellite."
    },
    {
        "id": 364,
        "subject": "EVS",
        "topic": "Indian History",
        "question": "In this year Vasco da Gama discovered the sea route to India / వాస్కోడిగామా భారతదేశానికి సముద్ర మార్గాన్ని కనిపెట్టిన సంవత్సరం:",
        "options": ["1498", "1948", "1849", "1984"],
        "answer": 1,
        "explanation": "Portuguese explorer Vasco da Gama landed in Calicut (Kozhikode) in 1498."
    },
    {
        "id": 386,
        "subject": "EVS",
        "topic": "Indian Polity",
        "question": "The constitutional head of the Indian nation is / భారతదేశానికి రాజ్యాంగ అధిపతి:",
        "options": ["Governor (గవర్నర్)", "Speaker (స్పీకర్)", "Prime minister (ప్రధానమంత్రి)", "President (రాష్ట్రపతి)"],
        "answer": 4,
        "explanation": "The President of India is the supreme executive and constitutional head of state."
    },
    {
        "id": 402,
        "subject": "EVS",
        "topic": "Social Reformers",
        "question": "The first female teacher in India was / భారతదేశంలో మొట్టమొదటి మహిళా ఉపాధ్యాయిని:",
        "options": ["Sindhu Tai", "Anandi bai Joshi", "Kadambari Ganguli", "Savitri bai Phule (సావిత్రి బాయి ఫూలే)"],
        "answer": 4,
        "explanation": "Savitribai Phule was India's pioneering first female educator."
    },
    {
        "id": 405,
        "subject": "EVS",
        "topic": "Notable Personalities",
        "question": "The author of 'Wings of Fire' / 'వింగ్స్ ఆఫ్ ఫైర్' రచయిత:",
        "options": ["Jawaharlal Nehru", "Ramnath Kovind", "Amarthya Sen", "Dr. A. P. J Abdul Kalam (డా. ఎ.పి.జె. అబ్దుల్ కలాం)"],
        "answer": 4,
        "explanation": "'Wings of Fire' is the autobiography of Dr. A.P.J. Abdul Kalam."
    },
    {
        "id": 419,
        "subject": "EVS",
        "topic": "Indian Constitution",
        "question": "This article of the Constitution states that untouchability has been abolished / రాజ్యాంగంలోని ఈ అధికరణం అంటరానితనాన్ని నిషేధిస్తుంది:",
        "options": ["Article 15", "Article 16", "Article 17", "Article 18"],
        "answer": 3,
        "explanation": "Article 17 of the Indian Constitution abolishes untouchability and forbids its practice in any form."
    },
    {
        "id": 433,
        "subject": "EVS",
        "topic": "World Geography",
        "question": "Smallest country in the world / ప్రపంచంలోనే అతి చిన్న దేశం:",
        "options": ["Jordan (జోర్డాన్)", "Vatican City (వాటికన్ సిటీ)", "Belgium (బెల్జియం)", "Taiwan (తైవాన్)"],
        "answer": 2,
        "explanation": "Vatican City is the smallest independent state in the world by both area and population."
    }
]

# ----------------- MATHEMATICS QUESTIONS -----------------
maths_questions = [
    {
        "id": 1,
        "subject": "Maths",
        "topic": "Divisibility Rules",
        "question": "Which of the following numbers is exactly divisible by 9? / క్రింది వాటిలో 9 చే నిశ్శేషంగా భాగింపబడే సంఖ్య ఏది?",
        "options": ["1167", "5536", "2343", "4563"],
        "answer": 4,
        "explanation": "Sum of digits in 4563: 4 + 5 + 6 + 3 = 18, which is divisible by 9. Therefore, 4563 is divisible by 9."
    },
    {
        "id": 2,
        "subject": "Maths",
        "topic": "Number System",
        "question": "The difference between the largest 6-digit number and the largest 5-digit number is / 6-అంకెల పెద్ద సంఖ్యకు, 5-అంకెల పెద్ద సంఖ్యకు గల తేడా:",
        "options": ["900000", "9000", "99999", "900009"],
        "answer": 1,
        "explanation": "Largest 6-digit = 999999, Largest 5-digit = 99999. Difference = 999999 - 99999 = 900000."
    },
    {
        "id": 3,
        "subject": "Maths",
        "topic": "Place Value",
        "question": "The place value of 4 in 46,739 is / 46,739 అనే సంఖ్యలో 4 యొక్క స్థాన విలువ:",
        "options": ["40000", "4000", "400", "4"],
        "answer": 1,
        "explanation": "4 is in the ten-thousands place, so its place value is 4 × 10,000 = 40,000."
    },
    {
        "id": 10,
        "subject": "Maths",
        "topic": "Units & Conversions",
        "question": "1 million = _______ lakhs / 1 మిలియన్ = _______ లక్షలు:",
        "options": ["5", "10", "100", "1000"],
        "answer": 2,
        "explanation": "1 million = 1,000,000 = 10 lakhs (10,00,000)."
    },
    {
        "id": 49,
        "subject": "Maths",
        "topic": "Prime Numbers",
        "question": "The only even prime number is / సరి ప్రధాన సంఖ్య ఏది?",
        "options": ["4", "6", "10", "2"],
        "answer": 4,
        "explanation": "2 is the only even prime number and the smallest prime number."
    },
    {
        "id": 50,
        "subject": "Maths",
        "topic": "HCF & LCM",
        "question": "The highest common factor (HCF) of 24 and 36 is / 24 మరియు 36 ల యొక్క గరిష్ట సామాన్య కారణాంకం (గ.సా.కా):",
        "options": ["6", "12", "18", "4"],
        "answer": 2,
        "explanation": "Factors of 24: 1, 2, 3, 4, 6, 8, 12, 24. Factors of 36: 1, 2, 3, 4, 6, 9, 12, 18, 36. Highest common factor = 12."
    },
    {
        "id": 65,
        "subject": "Maths",
        "topic": "Square Roots",
        "question": "If √1764 = 42 then √17.64 = ? / √1764 = 42 అయిన √17.64 = ?",
        "options": ["0.42", "4.2", "0.042", "0.0042"],
        "answer": 2,
        "explanation": "√17.64 = √(1764 / 100) = 42 / 10 = 4.2."
    },
    {
        "id": 66,
        "subject": "Maths",
        "topic": "Square Numbers",
        "question": "The greatest 4-digit perfect square is / 4-అంకెల గరిష్ట పరిపూర్ణ వర్గం:",
        "options": ["9998", "9600", "9999", "9801"],
        "answer": 4,
        "explanation": "99^2 = 9801, 100^2 = 10000 (5 digits). So 9801 is the greatest 4-digit perfect square."
    },
    {
        "id": 84,
        "subject": "Maths",
        "topic": "Pythagorean Triplets",
        "question": "Identify a Pythagorean triplet whose one number is 6 / 6 ఒక సంఖ్యగా గల పైథాగరియన్ త్రికమును గుర్తించండి:",
        "options": ["6, 8, 10", "6, 10, 12", "6, 8, 12", "6, 9, 15"],
        "answer": 1,
        "explanation": "6^2 + 8^2 = 36 + 64 = 100 = 10^2. Hence (6, 8, 10) forms a Pythagorean triplet."
    },
    {
        "id": 90,
        "subject": "Maths",
        "topic": "Special Numbers",
        "question": "Hardy-Ramanujan Number among the following is / క్రింది వానిలో హార్డీ-రామానుజన్ సంఖ్య ఏది?",
        "options": ["1279", "1927", "1729", "1792"],
        "answer": 3,
        "explanation": "1729 is the smallest number expressible as the sum of two cubes in two different ways (1^3 + 12^3 = 9^3 + 10^3 = 1729)."
    },
    {
        "id": 110,
        "subject": "Maths",
        "topic": "Ratio & Proportion",
        "question": "The ratio of 90 cm to 1.5 m is / 90 సెం. మీ. కు, 1.5 మీటర్లకు నిష్పత్తి:",
        "options": ["5:2", "5:3", "2:5", "3:5"],
        "answer": 4,
        "explanation": "1.5 m = 150 cm. Ratio = 90 : 150 = 9 : 15 = 3 : 5."
    },
    {
        "id": 127,
        "subject": "Maths",
        "topic": "Percentages",
        "question": "The population of a city decreased from 25,000 to 24,500. The percentage of decrease is / ఒక నగర జనాభా 25,000 నుండి 24,500 కు తగ్గింది. తగ్గుదల శాతం:",
        "options": ["1%", "2%", "4%", "5%"],
        "answer": 2,
        "explanation": "Decrease = 25,000 - 24,500 = 500. Percentage = (500 / 25,000) × 100% = 2%."
    },
    {
        "id": 168,
        "subject": "Maths",
        "topic": "Commercial Mathematics",
        "question": "A person bought a pair of skates at a sale where the discount was 20%. If the amount he pays is ₹1600, the marked price is:",
        "options": ["₹1750", "₹1800", "₹1900", "₹2000"],
        "answer": 4,
        "explanation": "Sale price = 80% of Marked Price. MP = 1600 / 0.8 = ₹2000."
    },
    {
        "id": 174,
        "subject": "Maths",
        "topic": "Simple Interest",
        "question": "The simple interest on ₹18,000 at 10% per annum for 2 years is / ₹18,000 పై సంవత్సరానికి 10% వడ్డీరేటు చొప్పున 2 సంవత్సరాలకు సాధారణ వడ్డీ:",
        "options": ["₹3,600", "₹1,800", "₹5,400", "₹3,200"],
        "answer": 1,
        "explanation": "SI = (P × T × R) / 100 = (18000 × 2 × 10) / 100 = ₹3,600."
    },
    {
        "id": 211,
        "subject": "Maths",
        "topic": "Geometry - Angles",
        "question": "The difference between 105° and its supplementary angle is / 105° మరియు దాని సంపూరక కోణముల మధ్య భేదం:",
        "options": ["20°", "30°", "40°", "50°"],
        "answer": 2,
        "explanation": "Supplementary angle to 105° is 180° - 105° = 75°. Difference = 105° - 75° = 30°."
    },
    {
        "id": 217,
        "subject": "Maths",
        "topic": "Geometry - Angles",
        "question": "The complementary angle of 37° is / 37° యొక్క పూరక కోణము:",
        "options": ["43°", "53°", "63°", "73°"],
        "answer": 2,
        "explanation": "Complementary angle = 90° - 37° = 53°."
    },
    {
        "id": 221,
        "subject": "Maths",
        "topic": "Geometry - Angles",
        "question": "The angle between two hands of a clock at 6 o'clock is / 6 గంటల సమయంలో గడియారంలోని రెండు ముళ్ళ మధ్య కోణం:",
        "options": ["Straight angle (సరళకోణం)", "Right angle (లంబకోణం)", "Acute angle (అల్పకోణం)", "Obtuse angle (అధికకోణం)"],
        "answer": 1,
        "explanation": "At 6:00, the hands point in opposite directions making a straight 180° angle."
    },
    {
        "id": 240,
        "subject": "Maths",
        "topic": "Geometry - Triangles",
        "question": "Sum of all exterior angles of a triangle is / త్రిభుజము యొక్క బాహ్య కోణాల మొత్తం:",
        "options": ["180°", "270°", "360°", "540°"],
        "answer": 3,
        "explanation": "The sum of the exterior angles of any convex polygon (including a triangle) is 360°."
    },
    {
        "id": 463,
        "subject": "Maths",
        "topic": "Mensuration",
        "question": "Number of faces of a cuboid / దీర్ఘ ఘనము యొక్క ముఖముల సంఖ్య:",
        "options": ["4", "6", "8", "5"],
        "answer": 2,
        "explanation": "A cuboid has 6 rectangular faces."
    },
    {
        "id": 506,
        "subject": "Maths",
        "topic": "Pedagogy",
        "question": "Which is the Sanskrit word for 'Mathematics'? / 'Mathematics' కు సమానమైన సంస్కృత పదం ఏది?",
        "options": ["Ganita (గణిత)", "Counting (లెక్కించుట)", "Maths (మ్యాథ్స్)", "Logic (తర్కం)"],
        "answer": 1,
        "explanation": "'Ganita' is the Sanskrit root term meaning calculation and science of mathematics."
    },
    {
        "id": 519,
        "subject": "Maths",
        "topic": "Pedagogy & History",
        "question": "Who is called the Father of Geometry? / ఫాదర్ ఆఫ్ జామెట్రీ అని ఎవరిని అంటారు?",
        "options": ["Archimedes", "Aristotle", "Euclid (యూక్లిడ్)", "Pythagoras"],
        "answer": 3,
        "explanation": "Euclid of Alexandria is universally recognized as the Father of Geometry."
    },
    {
        "id": 552,
        "subject": "Maths",
        "topic": "Pedagogy",
        "question": "The Greek word 'Heurisco' means / 'Heurisco' అను గ్రీకు పదం యొక్క అర్థం:",
        "options": ["I find (నేను కనుక్కొంటాను)", "I know (నాకు తెలుసు)", "I do (నేను చేస్తాను)", "I can (నేను చేయగలను)"],
        "answer": 1,
        "explanation": "'Heurisco' in Greek means 'I discover' or 'I find'."
    }
]

# ----------------- CDP QUESTIONS -----------------
cdp_questions = [
    {
        "id": 1,
        "subject": "CDP",
        "topic": "Foundations of Psychology",
        "question": "'Tabula Rasa' means / 'ట్యాబ్యులా రసా' అనగా:",
        "options": ["Blank Slate (ఖాళీ పలక)", "Blank Book (ఖాళీ పుస్తకం)", "Blank Table (ఖాళీ టేబుల్)", "Blank Bench (ఖాళీ బెంచ్)"],
        "answer": 1,
        "explanation": "John Locke popularized 'Tabula Rasa' meaning clean slate / blank slate on which experiences write."
    },
    {
        "id": 4,
        "subject": "CDP",
        "topic": "Child Rights & Constitution",
        "question": "The Constitution of India provides free and compulsory Education for all children in this age group (in years):",
        "options": ["0 to 14 years", "6 to 14 years", "6 to 20 years", "0 to 20 years"],
        "answer": 2,
        "explanation": "Article 21A provides free and compulsory education to all children aged 6 to 14 years."
    },
    {
        "id": 5,
        "subject": "CDP",
        "topic": "Child Welfare",
        "question": "National Child Helpline Service Number in India / భారతదేశంలో పిల్లల సహాయార్థం జాతీయ టోల్ ఫ్రీ నంబర్:",
        "options": ["100", "101", "104", "1098"],
        "answer": 4,
        "explanation": "Childline 1098 is India's 24-hour emergency phone outreach service for children in need."
    },
    {
        "id": 8,
        "subject": "CDP",
        "topic": "Developmental Stages",
        "question": "The developmental stage between Infancy and Adolescence is / శైశవ దశ, కౌమార దశ ల మధ్య గల దశ:",
        "options": ["Adulthood (వయోజన దశ)", "Old age (వార్ధక్యం)", "Childhood (బాల్యము)", "Prenatal Stage (జనన పూర్వ దశ)"],
        "answer": 3,
        "explanation": "Childhood directly connects infancy and adolescence."
    },
    {
        "id": 12,
        "subject": "CDP",
        "topic": "Parenting Styles",
        "question": "This is the most successful and healthy parenting style / ఇది బాగా విజయవంతమైన పెంపక శైలి:",
        "options": [
            "Authoritative style (సాధికారతత్వ శైలి)",
            "Authoritarian style (నిరంకుశతత్వ శైలి)",
            "Permissive Style (అంగీకారతత్వ శైలి)",
            "Uninvolved Style (జోక్యరహిత శైలి)"
        ],
        "answer": 1,
        "explanation": "Authoritative parenting (high warmth, high expectations, rational discipline) produces the most socially competent and confident children."
    },
    {
        "id": 31,
        "subject": "CDP",
        "topic": "Psychological Methods",
        "question": "This method is called as 'Clinical method' / ఈ పద్ధతిని చికిత్సా పద్ధతి అంటారు:",
        "options": [
            "Interview Method (పరిపృచ్ఛ పద్ధతి)",
            "Observation Method (పరిశీలన పద్ధతి)",
            "Experimental Method (ప్రయోగాత్మక పద్ధతి)",
            "Case Study Method (వ్యక్తి అధ్యయన పద్ధతి)"
        ],
        "answer": 4,
        "explanation": "Case Study method is often known as the Clinical Method, analyzing an individual deeply."
    },
    {
        "id": 50,
        "subject": "CDP",
        "topic": "Principles of Development",
        "question": "According to this principle, 'Development starts from head and proceeds towards heel' / వికాసం శిరస్సు నుండి ప్రారంభమై పాదాభిముఖంగా సాగుతుంది:",
        "options": [
            "Cephalo caudal (శిరోపాద నియమం)",
            "Proximodistal (సమీప దూరస్థ దశ)",
            "Principle of Continuity (అవిచ్ఛిన్న నియమం)",
            "Principle of Uniformity (సారూప్యత నియమం)"
        ],
        "answer": 1,
        "explanation": "Cephalocaudal trend describes head-to-toe progression in physical development."
    },
    {
        "id": 51,
        "subject": "CDP",
        "topic": "Principles of Development",
        "question": "According to this principle of development, 'Development proceeds from centre to periphery' / వికాసం శరీర మధ్యస్థం నుండి ప్రారంభమై వెలుపల దూరాలకు విస్తరిస్తుంది:",
        "options": [
            "Cephalo caudal (శిరోపాద నియమం)",
            "Proximodistal (సమీప మధ్యస్థ దశ)",
            "Principle of Continuity (అవిచ్ఛిన్న నియమం)",
            "Principle of Uniformity (సారూప్యత నియమం)"
        ],
        "answer": 2,
        "explanation": "Proximodistal progression develops motor control outward from the core trunk to the fingertips."
    },
    {
        "id": 83,
        "subject": "CDP",
        "topic": "Emotions",
        "question": "The word 'Emovere' is derived from this language / 'ఎమోవర్' అను పదము ఈ భాష నుండి ఉద్భవించింది:",
        "options": ["French", "Latin (లాటిన్)", "Arabic", "English"],
        "answer": 2,
        "explanation": "'Emotion' derives from the Latin verb 'emovere', meaning to agitate, stir up, or move."
    },
    {
        "id": 131,
        "subject": "CDP",
        "topic": "Language Development",
        "question": "The Theory of Language Acquisition Device (LAD) was proposed by / భాషా గ్రహణ సిద్ధాంతమును ప్రతిపాదించిన వారు:",
        "options": ["Skinner (స్కిన్నర్)", "Noam Chomsky (నోమ్ చామ్‌స్కీ)", "Bandura (బండూరా)", "Kohlberg (కోల్‌బర్గ్)"],
        "answer": 2,
        "explanation": "Noam Chomsky proposed that humans are born with a Language Acquisition Device (LAD)."
    },
    {
        "id": 140,
        "subject": "CDP",
        "topic": "Moral Development",
        "question": "According to Kohlberg’s Moral developmental theory, 'the good boy good girl attitude' reflects in this stage:",
        "options": ["Stage 1", "Stage 2", "Stage 3", "Stage 4"],
        "answer": 3,
        "explanation": "Stage 3 (Conventional level) is the 'Good boy / Nice girl' orientation of interpersonal accord."
    },
    {
        "id": 156,
        "subject": "CDP",
        "topic": "Perception",
        "question": "Wrong perceptions are called as / అసత్య ప్రత్యక్షాలు అనగా:",
        "options": ["Illusions (భ్రమలు)", "Fantasy (స్వైరకల్పన)", "Day dreaming (పగటికలలు)", "Meta cognition (స్వబుద్ధి)"],
        "answer": 1,
        "explanation": "An illusion is a misinterpretation or false sensory perception of an objective stimulus."
    },
    {
        "id": 170,
        "subject": "CDP",
        "topic": "Creativity",
        "question": "The correct order of creativity stages / సృజనాత్మక దశల యొక్క సరైన వరుసక్రమం:",
        "options": [
            "Preparation, Incubation/Latency, Insight/Illumination, Verification/Proving",
            "Preparation, Verification, Incubation, Insight",
            "Incubation, Verification, Insight, Preparation",
            "Preparation, Incubation, Proving, Insight"
        ],
        "answer": 1,
        "explanation": "Graham Wallas outlined the 4 stages of creativity: Preparation -> Incubation -> Illumination -> Verification."
    },
    {
        "id": 173,
        "subject": "CDP",
        "topic": "Cognitive Processes",
        "question": "Thinking about one’s own thoughts is called / ఒక వ్యక్తి తన ఆలోచనల గురించి తానే ఆలోచించడాన్ని ఏమంటారు?",
        "options": ["Meta cognition (స్వబుద్ధి)", "Intelligence (ప్రజ్ఞ)", "Thinking (ఆలోచన)", "Creativity (సృజనాత్మకత)"],
        "answer": 1,
        "explanation": "Metacognition is 'thinking about thinking' or awareness and understanding of one's own thought processes."
    },
    {
        "id": 190,
        "subject": "CDP",
        "topic": "Intelligence",
        "question": "The concept of Intelligence Quotient (IQ) was proposed by / 'ప్రజ్ఞా లబ్ధి' భావనను ప్రతిపాదించిన వారు:",
        "options": ["Stern (స్టెర్న్)", "Torrence", "Wallas", "Alfred Binet"],
        "answer": 1,
        "explanation": "William Stern proposed the concept and formula for Intelligence Quotient (IQ) in 1912."
    },
    {
        "id": 193,
        "subject": "CDP",
        "topic": "Intelligence",
        "question": "Formula for Intelligence Quotient (IQ) is:",
        "options": [
            "(Mental Age / Chronological Age) × 100",
            "(Chronological Age / Mental Age) × 100",
            "Mental Age / Chronological Age",
            "Chronological Age / Mental Age"
        ],
        "answer": 1,
        "explanation": "IQ = (MA / CA) × 100."
    },
    {
        "id": 232,
        "subject": "CDP",
        "topic": "Piaget's Theory",
        "question": "According to Jean Piaget, basic cognitive building blocks/structures are called as / సంజ్ఞానాత్మక నిర్మాణాన్ని పిలుస్తారు:",
        "options": ["Schema (స్కీమాటా)", "Assimilation (విలీనం)", "Accommodation (సానుకూలత)", "Equilibrium (సమతుల్యత)"],
        "answer": 1,
        "explanation": "Schemas are the mental frameworks or building blocks of knowledge."
    },
    {
        "id": 235,
        "subject": "CDP",
        "topic": "Piaget's Theory",
        "question": "According to Jean Piaget’s Theory, a child gains 'Object Permanence' in this stage / 'వస్తు స్థిరత్వ భావన' ఏ దశలో పొందుతాడు?",
        "options": [
            "Pre operational Stage",
            "Concrete Operational Stage",
            "Formal Operational Stage",
            "Sensory Motor Stage (ఇంద్రియ చాలక దశ)"
        ],
        "answer": 4,
        "explanation": "Object permanence develops during the Sensorimotor stage (0 - 2 years)."
    },
    {
        "id": 260,
        "subject": "CDP",
        "topic": "Endocrine Glands",
        "question": "This gland is called the Master Gland in human body / మానవ శరీరంలో ప్రధాన గ్రంథి (మాస్టర్ గ్లాండ్) అని దేనిని పిలుస్తారు?",
        "options": ["Pituitary Gland (పీయూష గ్రంథి)", "Thyroid Gland (అవటు గ్రంథి)", "Para Thyroid Gland", "Adrenal Gland"],
        "answer": 1,
        "explanation": "The Pituitary gland controls most other endocrine glands and is termed the Master Gland."
    },
    {
        "id": 341,
        "subject": "CDP",
        "topic": "Defense Mechanisms",
        "question": "A clerk who is angry at his boss shows it on his wife. It is an example for this defense mechanism / అధికారి మీద కోపాన్ని భార్యపై చూపించడం ఏ రక్షకతంత్రం?",
        "options": ["Projection (ప్రక్షేపణం)", "Displacement (విస్థాపనం)", "Regression (ప్రతిగమనం)", "Identification (తాదాత్మ్యకరణం)"],
        "answer": 2,
        "explanation": "Displacement is redirecting anger or impulse toward a safer, less threatening target."
    },
    {
        "id": 349,
        "subject": "CDP",
        "topic": "Defense Mechanisms",
        "question": "When the fox could not get grapes it remarks them as sour grapes. This is an example of which defense mechanism?",
        "options": ["Repression (దమనం)", "Projection (ప్రక్షేపణం)", "Rationalization (హేతుకీకరణం)", "Displacement (విస్థాపనం)"],
        "answer": 3,
        "explanation": "Rationalization is inventing plausible, false reasons to justify disappointment or failure."
    },
    {
        "id": 422,
        "subject": "CDP",
        "topic": "Learning Theories",
        "question": "Pavlov's experiment on dog salivation is related to which conditioning theory?",
        "options": [
            "Classical Conditioning (శాస్త్రీయ నిబంధనం)",
            "Operant Conditioning (కార్యసాధక నిబంధనం)",
            "Trial and Error Method (యత్న దోష పద్ధతి)",
            "Observational Learning"
        ],
        "answer": 1,
        "explanation": "Ivan Pavlov formulated the Classical Conditioning paradigm with dogs and stimulus conditioning."
    },
    {
        "id": 424,
        "subject": "CDP",
        "topic": "Learning Theories",
        "question": "B.F. Skinner conducted his Operant Conditioning experiments primarily on:",
        "options": ["Rat (ఎలుక)", "Rabbit (కుందేలు)", "Dog (కుక్క)", "Chimpanzee (చింపాంజీ)"],
        "answer": 1,
        "explanation": "Skinner used rats (and pigeons) in his operant conditioning Skinner box experiments."
    },
    {
        "id": 444,
        "subject": "CDP",
        "topic": "Insightful Learning",
        "question": "The Psychologist who conducted insightful learning experiments on Chimpanzee (Sultan) was:",
        "options": ["E.L. Thorndike", "Ivan Pavlov", "Kohler (కొహెలర్)", "B.F. Skinner"],
        "answer": 3,
        "explanation": "Wolfgang Köhler conducted famous experiments on Sultan the chimpanzee formulating Insightful Learning."
    },
    {
        "id": 465,
        "subject": "CDP",
        "topic": "Vygotsky's Theory",
        "question": "The difference between what a learner can do without help and what they can achieve with guidance is known as:",
        "options": [
            "Scaffolding (స్కాఫోల్డింగ్)",
            "Zone of Proximal Development (సమీపస్థ వికాస మండలి)",
            "Collaborative learning",
            "Construction of knowledge"
        ],
        "answer": 2,
        "explanation": "Lev Vygotsky defined this gap as the Zone of Proximal Development (ZPD)."
    },
    {
        "id": 505,
        "subject": "CDP",
        "topic": "National Education Policy",
        "question": "Structure of school education recommended in NEP 2020 / NEP 2020 లో విద్యా నిర్మాణం:",
        "options": ["10 + 2 + 3", "11 + 1 + 3", "5 + 3 + 3 + 4", "10 + 3 + 3"],
        "answer": 3,
        "explanation": "NEP 2020 replaces the 10+2 system with the 5+3+3+4 pedagogical structure."
    },
    {
        "id": 510,
        "subject": "CDP",
        "topic": "Educational Acts",
        "question": "RTE 2009 (Right to Education Act) came into force on / RTE 2009 అమలులోనికి వచ్చిన తేదీ:",
        "options": ["1 Jan 2010", "1 Jan 2009", "1 April 2010 (1 ఏప్రిల్ 2010)", "1 April 2009"],
        "answer": 3,
        "explanation": "The Right of Children to Free and Compulsory Education Act came into legal force across India on 1st April 2010."
    }
]

# Write to separate JSON files
with open("data/english.json", "w", encoding="utf-8") as f:
    json.dump(english_questions, f, ensure_ascii=False, indent=2)

with open("data/telugu.json", "w", encoding="utf-8") as f:
    json.dump(telugu_questions, f, ensure_ascii=False, indent=2)

with open("data/evs.json", "w", encoding="utf-8") as f:
    json.dump(evs_questions, f, ensure_ascii=False, indent=2)

with open("data/maths.json", "w", encoding="utf-8") as f:
    json.dump(maths_questions, f, ensure_ascii=False, indent=2)

with open("data/cdp.json", "w", encoding="utf-8") as f:
    json.dump(cdp_questions, f, ensure_ascii=False, indent=2)

# Combined catalog summary
all_data = {
    "English": english_questions,
    "Telugu": telugu_questions,
    "EVS": evs_questions,
    "Maths": maths_questions,
    "CDP": cdp_questions
}

with open("data/all_subjects.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"Generated verified database:")
print(f"- English: {len(english_questions)} questions")
print(f"- Telugu: {len(telugu_questions)} questions")
print(f"- EVS: {len(evs_questions)} questions")
print(f"- Maths: {len(maths_questions)} questions")
print(f"- CDP: {len(cdp_questions)} questions")
print(f"Total: {sum(len(v) for v in all_data.values())} curated questions ready.")
