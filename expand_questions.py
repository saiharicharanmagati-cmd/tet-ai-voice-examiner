import json
import os

with open("data/all_subjects.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Add more English questions
eng_extra = [
    {
        "id": 12,
        "subject": "English",
        "topic": "Synonyms",
        "question": "The raider holds his breath and chants ‘kabaddi…kabaddi’. Choose the synonym of the word ‘chant’.",
        "options": ["plays", "calls", "moves", "fights"],
        "answer": 2,
        "explanation": "Chanting rhythmic calls during the raid is 'calls'."
    },
    {
        "id": 13,
        "subject": "English",
        "topic": "Synonyms",
        "question": "Kabaddi requires no specific sporting equipment. Choose the appropriate synonym of ‘equipment’.",
        "options": ["rules", "ground", "tools", "players"],
        "answer": 3,
        "explanation": "'Equipment' refers to tools or implements."
    },
    {
        "id": 15,
        "subject": "English",
        "topic": "Synonyms",
        "question": "She discovered a beautiful diamond necklace. Choose the appropriate synonym of ‘discovered’.",
        "options": ["destroyed", "sold", "found out", "bought"],
        "answer": 3,
        "explanation": "'Discovered' means found out or uncovered."
    },
    {
        "id": 20,
        "subject": "English",
        "topic": "Synonyms",
        "question": "We had a thrilling experience. Choose the synonym of the word ‘thrilling’.",
        "options": ["exciting", "boring", "dull", "monotonous"],
        "answer": 1,
        "explanation": "'Thrilling' means exciting or exhilarating."
    },
    {
        "id": 27,
        "subject": "English",
        "topic": "Antonyms",
        "question": "The king agreed and ordered to bring the scales. Choose the antonym of the word ‘agreed’.",
        "options": ["differed", "acknowledged", "granted", "confessed"],
        "answer": 1,
        "explanation": "The opposite of 'agreed' is 'differed' or disagreed."
    },
    {
        "id": 36,
        "subject": "English",
        "topic": "Antonyms",
        "question": "“No dear, I won’t stay here, sending away my friends in dismay”. replied the white butterfly. Choose the antonym of the word ‘dismay’.",
        "options": ["Pleasure", "Distress", "Upset", "Anxiety"],
        "answer": 1,
        "explanation": "'Dismay' means distress or consternation; its antonym is 'Pleasure'."
    },
    {
        "id": 40,
        "subject": "English",
        "topic": "Antonyms",
        "question": "By constant application, one can remember various formulae of science and mathematics. Choose the antonym of the word ‘remember’.",
        "options": ["forget", "recall", "recollect", "think of"],
        "answer": 1,
        "explanation": "The antonym of 'remember' is 'forget'."
    },
    {
        "id": 86,
        "subject": "English",
        "topic": "Figures of Speech",
        "question": "He roared like a lion. Choose the figure of speech used in the given sentence.",
        "options": ["Personification", "Simile", "Metaphor", "Hyperbole"],
        "answer": 2,
        "explanation": "The sentence makes a direct comparison using 'like', which is a Simile."
    },
    {
        "id": 100,
        "subject": "English",
        "topic": "Figures of Speech",
        "question": "Lencho was an ox of a man. Choose the figure of speech used in the given sentence.",
        "options": ["Simile", "Metaphor", "Personification", "Hyperbole"],
        "answer": 2,
        "explanation": "Lencho is compared directly to an ox without 'like' or 'as', which is a Metaphor."
    },
    {
        "id": 101,
        "subject": "English",
        "topic": "Figures of Speech",
        "question": "Death lays his icy hand on kings. Choose the figure of speech used in the given sentence.",
        "options": ["Simile", "Personification", "Metaphor", "Oxymoron"],
        "answer": 2,
        "explanation": "Death is given human traits ('his icy hand'), representing Personification."
    },
    {
        "id": 116,
        "subject": "English",
        "topic": "Idioms",
        "question": "Choose the correct idiomatic expression that means a general view.",
        "options": ["a bird’s eye view", "a lion’s eye view", "a cat’s eye view", "a owl’s eye view"],
        "answer": 1,
        "explanation": "'A bird's eye view' denotes an overall, general view from above."
    },
    {
        "id": 117,
        "subject": "English",
        "topic": "Idioms",
        "question": "Choose the correct idiomatic expression to mean unrecognized danger.",
        "options": ["Make no bones", "Bone of connection", "Snake in the grass", "A bird’s eye view"],
        "answer": 3,
        "explanation": "'A snake in the grass' refers to a treacherous person or hidden/unrecognized danger."
    },
    {
        "id": 121,
        "subject": "English",
        "topic": "Idioms",
        "question": "Choose the correct idiom appropriate in the following situation: 'You’re so proud of your child.'",
        "options": ["He’s the apple of my eye.", "He looks a sight.", "He’s for my eyes only.", "He’s my boy."],
        "answer": 1,
        "explanation": "'The apple of my eye' means someone cherished and prized above all others."
    },
    {
        "id": 122,
        "subject": "English",
        "topic": "Idioms",
        "question": "Choose the correct idiomatic expression.",
        "options": ["tone of connection", "bone of connection", "bone of contention", "tongue of contention"],
        "answer": 3,
        "explanation": "The correct idiom is 'bone of contention' (subject of dispute)."
    },
    {
        "id": 125,
        "subject": "English",
        "topic": "Idioms",
        "question": "Don’t worry! we’ll have the money ready by 5pm, by hook or by crook. Choose the correct meaning of the underlined idiomatic expression.",
        "options": ["by any method", "very proud", "very simple", "by the worst way"],
        "answer": 1,
        "explanation": "'By hook or by crook' means by any possible method or means."
    },
    {
        "id": 128,
        "subject": "English",
        "topic": "Phrasal Verbs",
        "question": "The president gives away bravery awards every year. Choose the meaning of the phrasal verb ‘give away’.",
        "options": ["to organize some event", "to appreciate someone", "to declare something", "to present something"],
        "answer": 4,
        "explanation": "'Give away' awards means to distribute or present them."
    },
    {
        "id": 129,
        "subject": "English",
        "topic": "Phrasal Verbs",
        "question": "The Headmaster will look into the problem. Choose the correct meaning of the phrase ‘look into’.",
        "options": ["consume", "stare", "examine", "disclose"],
        "answer": 3,
        "explanation": "'Look into' means investigate or examine."
    },
    {
        "id": 130,
        "subject": "English",
        "topic": "Phrasal Verbs",
        "question": "Carry on until you get to the junction, then turn left. Choose the correct meaning of the phrasal verb ‘carry on’.",
        "options": ["to continue moving", "to stop moving", "to pause moving", "to investigate"],
        "answer": 1,
        "explanation": "'Carry on' means continue moving or proceeding."
    },
    {
        "id": 141,
        "subject": "English",
        "topic": "Phrasal Verbs",
        "question": "The situation needs prompt action. Choose the suitable phrase that means ‘needs’:",
        "options": ["calls for", "calls off", "calls out", "call at"],
        "answer": 1,
        "explanation": "'Calls for' means demands or requires / needs."
    },
    {
        "id": 146,
        "subject": "English",
        "topic": "Phrasal Verbs",
        "question": "I look after his affairs in his absence. Choose the meaning of the phrasal verb ‘look after’.",
        "options": ["to examine", "to look again", "to hope for", "to take care of"],
        "answer": 4,
        "explanation": "'Look after' means to care for or take care of."
    },
    {
        "id": 154,
        "subject": "English",
        "topic": "Modals",
        "question": "It ____ rain today. Choose the correct modal verb used to express possibility.",
        "options": ["shall", "would", "may", "will"],
        "answer": 3,
        "explanation": "'May' is used to express possibility."
    },
    {
        "id": 162,
        "subject": "English",
        "topic": "Language Functions",
        "question": "May God bless you! Choose the language function of the given sentence.",
        "options": ["Possibility", "Prediction", "Wish", "Suggestion"],
        "answer": 3,
        "explanation": "'May God bless you!' expresses a Wish or Benediction."
    },
    {
        "id": 185,
        "subject": "English",
        "topic": "Subject-Verb Agreement",
        "question": "Identify the grammatically correct sentence.",
        "options": [
            "The quality of mangoes were not good.",
            "The quality of mangoes was not good.",
            "The quality of mangoes have not good.",
            "The quality of mangoes has not good."
        ],
        "answer": 2,
        "explanation": "The head noun of the subject is 'The quality' (singular), so the verb must be singular ('was not good')."
    },
    {
        "id": 188,
        "subject": "English",
        "topic": "Subject-Verb Agreement",
        "question": "Identify the grammatically correct sentence.",
        "options": [
            "Silver as well as cotton has fallen in price.",
            "Silver as well as cotton have fallen in price.",
            "Silver as well as cotton have been fallen in price.",
            "Silver as well as cotton fallen in price."
        ],
        "answer": 1,
        "explanation": "When two subjects are joined by 'as well as', the verb agrees with the first subject ('Silver' -> singular 'has fallen')."
    },
    {
        "id": 196,
        "subject": "English",
        "topic": "Conjunctions",
        "question": "Their house is _____ big ____ small. Choose the correct pair of correlative conjunctions.",
        "options": ["neither, nor", "either, nor", "neither, not", "neither, or"],
        "answer": 1,
        "explanation": "The correct correlative conjunction pair is 'neither... nor'."
    },
    {
        "id": 197,
        "subject": "English",
        "topic": "Linkers",
        "question": "The road was closed _____ an accident. Choose the correct linker.",
        "options": ["due to", "in spite of", "unless", "furthermore"],
        "answer": 1,
        "explanation": "'Due to' means caused by / because of."
    },
    {
        "id": 204,
        "subject": "English",
        "topic": "Linkers",
        "question": "The new system was supposed to be more efficient. _______, in practice it caused chaos.",
        "options": ["However", "And", "If", "In spite of"],
        "answer": 1,
        "explanation": "'However' connects two contrasting sentences."
    },
    {
        "id": 262,
        "subject": "English",
        "topic": "Prepositions",
        "question": "Our National Anthem was translated ____ Bengali ___ English.",
        "options": ["in, to", "in, in", "to, in", "from, to"],
        "answer": 4,
        "explanation": "Translation occurs 'from' one language 'to' another."
    },
    {
        "id": 263,
        "subject": "English",
        "topic": "Prepositions",
        "question": "Mahatma Gandhi was born ____ Porbandar ____ Gujarat.",
        "options": ["on, in", "in, in", "in, on", "at, in"],
        "answer": 4,
        "explanation": "Smaller places take 'at' while larger areas/states take 'in': 'at Porbandar in Gujarat'."
    },
    {
        "id": 270,
        "subject": "English",
        "topic": "Prepositions",
        "question": "The ant hill was in ____ two coconut trees.",
        "options": ["between", "among", "along", "across"],
        "answer": 1,
        "explanation": "For two distinct entities, we use 'between'."
    }
]

# Add more Telugu questions
tel_extra = [
    {
        "id": 7,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం",
        "question": "పనస తొనలకన్న పంచదారలకన్న / జుంటి తేనెకన్న జున్నుకన్న / చెఱకు రసముకన్న చెలుల మాటలె తీపి / విశ్వదాభిరామ వినురవేమ - పనస తొనలు, పంచదార, తేనె, జున్ను కంటే ఎవరి మాటలు మధురంగా ఉంటాయి?",
        "options": ["స్త్రీలు", "సఖుడు", "అమ్మ", "మిత్రుడు"],
        "answer": 1,
        "explanation": "పద్యంలో 'చెలుల మాటలె తీపి' అని పేర్కొన్నారు (చెలులు అనగా స్త్రీలు / ప్రియురాండ్రు)."
    },
    {
        "id": 8,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం",
        "question": "మిరియము గింజ చూడ మీద నల్లగ నుండు / కొరికి చూడ లోన జుఱుకుమనును / సజ్జనులగు వారి సారమిట్లుండురా / విశ్వదాభిరామ వినురవేమ - పై పద్యం ఆధారంగా సరికానిది ఏది?",
        "options": [
            "మిరియపు గింజ నల్లగా ఉంటుంది",
            "మిరియపుగింజను కొరికితే కారముగా ఉంటుంది",
            "మిరియపుగింజ వలె సజ్జనుడి మనసు నలుపు",
            "సజ్జనుడు అంటే మంచివాడు"
        ],
        "answer": 3,
        "explanation": "సజ్జనుల మనసు నలుపు కాదు, వారి సద్గుణ సారము మిరియపు ఘాటు వంటి గుణవంతమైనది."
    },
    {
        "id": 14,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం",
        "question": "ఉప్పులేని కూర యొప్పుడ రుచులకు / పప్పులేని తిండి ఫలము లేదు / అప్పులేని వాడె యధిక సంపన్నుడు / విశ్వదాభిరామ వినురవేమ - పై పద్యం ఆధారంగా సరైనది ఏది?",
        "options": [
            "ఉప్పులేని కూర రుచిగా ఉంటుంది",
            "అప్పుచేసే వాడు అధికసంపన్నుడు",
            "పై పద్యం వేమన శతకం లోనిది",
            "ఉప్పు పప్పు లేని ఆహారం తినాలి"
        ],
        "answer": 3,
        "explanation": "విశ్వదాభిరామ వినురవేమ మకుటంతో ఉన్న పద్యాలన్నీ వేమన శతకము లోనివి."
    },
    {
        "id": 51,
        "subject": "Telugu",
        "topic": "గద్యభాగం",
        "question": "చిదంబరం అనేది దక్షిణదేశంలో గొప్ప పుణ్యక్షేత్రం. అయ్యిదు ప్రాకారాలు నాలుగు గోపురాలున్నాయి. పై గద్యంలో చెప్పిన పుణ్యక్షేత్రం ఏది?",
        "options": ["కంచి", "చిదంబరం", "అరుణాచలం", "అమరావతి"],
        "answer": 2,
        "explanation": "గద్యంలో చెప్పబడిన పుణ్యక్షేత్రం చిదంబరం."
    },
    {
        "id": 52,
        "subject": "Telugu",
        "topic": "సాహిత్యం",
        "question": "పుట్టపర్తి నారాయణాచార్యులు ద్విపదలో రచించిన బృహత్కావ్యం 'పండరి భాగవతం' లోని పద్యాలు ఏ ఛందస్సులో కలవు?",
        "options": ["కందం", "ద్విపద", "ఆటవెలది", "తేటగీతి"],
        "answer": 2,
        "explanation": "పుట్టపర్తి నారాయణాచార్యుల పండరి భాగవతం 'ద్విపద' ఛందస్సులో రచింపబడినది."
    },
    {
        "id": 78,
        "subject": "Telugu",
        "topic": "సాహిత్యం",
        "question": "దేవులపల్లి కృష్ణశాస్త్రి గారి తల్లిదండ్రులు ఎవరు?",
        "options": ["సీతమ్మ - రామయ్య", "సీతమ్మ – తిమ్మన్న శాస్త్రి", "సీతమ్మ – తమ్మన్న శాస్త్రి", "సీతమ్మ – రామన్ణ శాస్త్రి"],
        "answer": 3,
        "explanation": "దేవులపల్లి వేంకట కృష్ణశాస్త్రి తల్లిదండ్రులు సీతమ్మ మరియు తమ్మన్న శాస్త్రి."
    },
    {
        "id": 91,
        "subject": "Telugu",
        "topic": "సాహిత్యం - బిరుదులు",
        "question": "'అభినవ నన్నయ' బిరుదు గల కవి ఎవరు?",
        "options": ["చెఱుకుపల్లి జమదగ్ని శర్మ", "బోయి భీమన్న", "రాయప్రోలు సుబ్బారావు", "విద్వాన్ విశ్వం"],
        "answer": 1,
        "explanation": "చెఱుకుపల్లి జమదగ్ని శర్మ గారికి 'అభినవ నన్నయ' అనే బిరుదు కలదు."
    },
    {
        "id": 114,
        "subject": "Telugu",
        "topic": "సాహిత్యం",
        "question": "రాయలసీమ సౌందర్యాన్ని, విషాదాన్ని సమంగా చిత్రించిన కవి ఎవరు?",
        "options": ["విద్వాన్ విశ్వం", "గురజాడ అప్పారావు", "చెఱుకుపల్లి జమదగ్నిశర్మ", "బోయి భీమన్న"],
        "answer": 1,
        "explanation": "రాయలసీమ జీవన సౌందర్యాన్ని, కరువు విషాదాన్ని 'పెన్నేటి పాట' కావ్యంలో చిత్రించిన కవి విద్వాన్ విశ్వం."
    },
    {
        "id": 115,
        "subject": "Telugu",
        "topic": "సాహిత్య పురస్కారాలు",
        "question": "రావూరి భరద్వాజ రచించిన ఏ రచనకు జ్ఞానపీఠ పురస్కారం లభించింది?",
        "options": ["అపరిచితులు", "కథాసాగరం", "పాకుడురాళ్ళు", "జలప్రళయం"],
        "answer": 3,
        "explanation": "రావూరి భరద్వాజ గారి 'పాకుడురాళ్ళు' నవలకు ప్రతిష్ఠాత్మక జ్ఞానపీఠ అవార్డు లభించింది."
    },
    {
        "id": 185,
        "subject": "Telugu",
        "topic": "ప్రక్రియలు",
        "question": "మకుటం కలిగి నూరు పద్యాల రచనను ఏమంటారు?",
        "options": ["నాటకం", "కవిత్వం", "శతకం", "కావ్యం"],
        "answer": 3,
        "explanation": "నూరు లేదా అంతకంటే ఎక్కువ పద్యాలు ఉండి, ప్రతి పద్యం చివర ఒకే మకుటం ఉంటే దానిని 'శతకం' అంటారు."
    },
    {
        "id": 187,
        "subject": "Telugu",
        "topic": "ప్రక్రియలు",
        "question": "తన గురించి తాను రాసుకొనే సాహితీ ప్రక్రియ ఏది?",
        "options": ["జీవిత చరిత్ర", "వ్యక్తి చరిత్ర", "ఆత్మకథ", "వాస్తవ కథ"],
        "answer": 3,
        "explanation": "తన జీవితాన్ని తానే గ్రంథస్తం చేసుకుంటే అది 'ఆత్మకథ' (స్వీయచరిత్ర)."
    },
    {
        "id": 255,
        "subject": "Telugu",
        "topic": "పదజాలం - అర్థాలు",
        "question": "'వినువీథి' పదానికి అర్థం:",
        "options": ["భూమి", "వినుట", "వేడుక", "ఆకాశం"],
        "answer": 4,
        "explanation": "వినువీథి అనగా ఆకాశ మార్గము / ఆకాశం."
    },
    {
        "id": 260,
        "subject": "Telugu",
        "topic": "పదజాలం - అర్థాలు",
        "question": "'కొరత' పదానికి అర్థం:",
        "options": ["సామాన్యం", "సమానం", "ఎక్కువ", "తక్కువ"],
        "answer": 4,
        "explanation": "కొరత అనగా లేమి లేదా తక్కువగా ఉండటం."
    },
    {
        "id": 275,
        "subject": "Telugu",
        "topic": "పర్యాయపదాలు",
        "question": "కూరిమి, చెలిమి పదాలకు సమానార్థక పదం:",
        "options": ["చపలము", "అవమానము", "స్నేహం", "ధైర్యం"],
        "answer": 3,
        "explanation": "కూరిమి, చెలిమి, నెయ్యము అనగా స్నేహము."
    },
    {
        "id": 288,
        "subject": "Telugu",
        "topic": "పర్యాయపదాలు",
        "question": "'భాస్కరుడు' పదానికి పర్యాయపదాలు:",
        "options": ["శశి, హరి", "సూర్యుడు, భానుడు", "అనిలుడు, వాతూలము", "అహము, ఉష"],
        "answer": 2,
        "explanation": "భాస్కరుడు, సూర్యుడు, భానుడు, రవి, దినకరుడు సూర్యునికి పర్యాయపదాలు."
    },
    {
        "id": 339,
        "subject": "Telugu",
        "topic": "జాతీయాలు",
        "question": "'చిత్తము కలతనొందు' అనే అర్థంలో వాడే జాతీయమేది?",
        "options": ["గడ్డిగఱచు", "గాలిమాట", "గుండెచెరువగు", "గుటకలుమింగు"],
        "answer": 3,
        "explanation": "తీవ్రమైన వేదన, చిత్తకలత చెందడాన్ని 'గుండెచెరువగు' అంటారు."
    },
    {
        "id": 404,
        "subject": "Telugu",
        "topic": "వర్ణోత్పత్తి",
        "question": "గాలి బయటకు ఊదుతూ పలికే అక్షరాలను ఏమంటారు?",
        "options": ["సరళాలు", "ఊష్మాలు", "అంతస్థాలు", "అనునాసికాలు"],
        "answer": 2,
        "explanation": "ఊది పలుకబడు శ, ష, స, హ లను 'ఊష్మాలు' అంటారు."
    },
    {
        "id": 407,
        "subject": "Telugu",
        "topic": "వర్ణోత్పత్తి",
        "question": "ముక్కు సాయంతో పలికే అక్షరాలను ఏమంటారు?",
        "options": ["అంతస్థాలు", "అనునాసికాలు", "అవ్యయాలు", "ఓష్ఠ్యాలు"],
        "answer": 2,
        "explanation": "నాసిక (ముక్కు) సహాయంతో పలికే ఙ, ఞ, ణ, న, మ లను 'అనునాసికాలు' అంటారు."
    },
    {
        "id": 427,
        "subject": "Telugu",
        "topic": "సంధులు",
        "question": "కింది వానిలో సవర్ణదీర్ఘసంధి కాని పదాన్ని గుర్తించండి:",
        "options": ["మహీశుడు", "భానూదయ", "రామాలయం", "మహేంద్రుడు"],
        "answer": 4,
        "explanation": "మహా + ఇంద్రుడు = మహేంద్రుడు (గుణసంధి), మిగిలిన మూడు సవర్ణదీర్ఘసంధి పదాలు."
    },
    {
        "id": 443,
        "subject": "Telugu",
        "topic": "సమాసాలు",
        "question": "సమప్రాధాన్యం గల రెండు పదాలు కలిసి సమాసమైతే అది ఏ సమాసం?",
        "options": ["ద్విగు సమాసం", "బహువ్రీహి సమాసం", "ద్వంద్వ సమాసం", "కర్మధారయ సమాసం"],
        "answer": 3,
        "explanation": "ఉభయ పదార్థ ప్రధానము 'ద్వంద్వ సమాసము' (ఉదా: తల్లిదండ్రులు, రామలక్ష్మణులు)."
    }
]

# Add more EVS questions
evs_extra = [
    {
        "id": 4,
        "subject": "EVS",
        "topic": "Plant Forms",
        "question": "Identify the tree among the following / క్రింది వానిలో చెట్టును గుర్తించండి:",
        "options": ["Rose (గులాబీ)", "Hibiscus (మందార)", "Tulsi (తులసి)", "Tamarind (చింత)"],
        "answer": 4,
        "explanation": "Tamarind grows into a large perennial woody tree, whereas the others are herbs or shrubs."
    },
    {
        "id": 5,
        "subject": "EVS",
        "topic": "Plant Forms",
        "question": "Identify the shrub among the following / క్రింది వానిలో పొదను గుర్తించండి:",
        "options": ["Banyan (మర్రి)", "Hibiscus (మందార)", "Wheat (గోధుమ)", "Bitter gourd (కాకర)"],
        "answer": 2,
        "explanation": "Hibiscus is a medium-sized woody plant with branches near ground level (shrub)."
    },
    {
        "id": 6,
        "subject": "EVS",
        "topic": "Plant Forms",
        "question": "Identify the creeper among the following / క్రింది వానిలో పాకే మొక్కను గుర్తించండి:",
        "options": ["Pumpkin (గుమ్మడి)", "Grape (ద్రాక్ష)", "Tulsi (తులసి)", "Rose (గులాబీ)"],
        "answer": 1,
        "explanation": "Pumpkin plants trail along the ground with weak stems (creepers)."
    },
    {
        "id": 22,
        "subject": "EVS",
        "topic": "Agriculture & Crops",
        "question": "Jaggery and sugar are produced from this plant / బెల్లం మరియు పంచదారను ఈ మొక్క నుండి ఉత్పత్తి చేస్తారు:",
        "options": ["Beetroot", "Potato", "Wheat", "Sugarcane (చెరకు)"],
        "answer": 4,
        "explanation": "Sugarcane juice is crystallized to produce jaggery and refined sugar."
    },
    {
        "id": 23,
        "subject": "EVS",
        "topic": "Plant Anatomy",
        "question": "The edible part of potato is / బంగాళాదుంప నందు తినదగిన భాగం:",
        "options": ["Stem (కాండం)", "Root (వేరు)", "Flower (పుష్పం)", "Fruit (ఫలం)"],
        "answer": 1,
        "explanation": "Potato is a modified underground stem (tuber)."
    },
    {
        "id": 24,
        "subject": "EVS",
        "topic": "Plant Anatomy",
        "question": "The edible part of Radish is / ముల్లంగి నందు తినదగిన భాగం:",
        "options": ["Stem (కాండం)", "Root (వేరు)", "Flower (పుష్పం)", "Fruit (ఫలం)"],
        "answer": 2,
        "explanation": "Radish is a modified tap root storing food."
    },
    {
        "id": 25,
        "subject": "EVS",
        "topic": "Living Organisms",
        "question": "Mushroom is a / పుట్టగొడుగు ఒక:",
        "options": ["Algae (శైవలం)", "Flower (పుష్పం)", "Fungi (శిలీంధ్రం)", "Fruit (ఫలం)"],
        "answer": 3,
        "explanation": "Mushrooms are spore-bearing fruiting bodies of fungi."
    },
    {
        "id": 68,
        "subject": "EVS",
        "topic": "Plant Biology",
        "question": "Green plants prepare their food by the process called / ఆకుపచ్చని మొక్కలు ఆహారాన్ని తయారుచేసుకునే ప్రక్రియ:",
        "options": ["Transpiration (బాష్పోత్సేకం)", "Absorption (శోషణ)", "Photosynthesis (కిరణజన్య సంయోగక్రియ)", "Saprotroph"],
        "answer": 3,
        "explanation": "Photosynthesis produces carbohydrates utilizing sunlight, chlorophyll, CO2, and water."
    },
    {
        "id": 69,
        "subject": "EVS",
        "topic": "Plant Biology",
        "question": "The gas released by green plants during photosynthesis / ఆకుపచ్చని మొక్కలు కిరణజన్య సంయోగక్రియలో విడుదలచేయు వాయువు:",
        "options": ["Carbon dioxide", "Oxygen (ఆక్సిజన్)", "Nitrogen", "Carbon monoxide"],
        "answer": 2,
        "explanation": "Oxygen gas is liberated as a byproduct during photosynthesis."
    },
    {
        "id": 73,
        "subject": "EVS",
        "topic": "Agriculture & Bacteria",
        "question": "Nitrogen-fixing bacteria in legume root nodules is / పప్పుజాతి మొక్కలలో నత్రజని స్థాపించే బ్యాక్టీరియా:",
        "options": ["Lactobacillus", "Lichens", "Rhizobium (రైజోబియం)", "Rhizopus"],
        "answer": 3,
        "explanation": "Rhizobium fixes atmospheric nitrogen into nitrates symbiotically in legume nodules."
    },
    {
        "id": 77,
        "subject": "EVS",
        "topic": "Human Physiology",
        "question": "Bile juice is secreted by / పైత్యరసంను స్రవించేది:",
        "options": ["Pancreas (క్లోమం)", "Stomach (జీర్ణాశయం)", "Liver (కాలేయము)", "Intestinal glands"],
        "answer": 3,
        "explanation": "Liver secretes bile juice, which is stored in the gall bladder."
    },
    {
        "id": 92,
        "subject": "EVS",
        "topic": "Circulatory System",
        "question": "Haemoglobin is present in / హిమోగ్లోబిన్ ను కలిగి ఉండునవి:",
        "options": ["Red blood Cells (RBC)", "White blood Cells (WBC)", "Blood Platelets", "Lymph nodes"],
        "answer": 1,
        "explanation": "Haemoglobin is the iron-rich oxygen-binding protein in Red Blood Cells."
    },
    {
        "id": 101,
        "subject": "EVS",
        "topic": "Skeletal System",
        "question": "Bony part that protects the brain / మెదడును రక్షించే అస్థి భాగం:",
        "options": ["Backbone (వెన్నుముక)", "Rib cage (ఉరః పంజరం)", "Skull (పుర్రె)", "Pelvic girdle"],
        "answer": 3,
        "explanation": "The cranium / skull encases and protects the human brain."
    },
    {
        "id": 118,
        "subject": "EVS",
        "topic": "Hormones",
        "question": "The deficiency of insulin causes / ఇన్సులిన్ లోపం దీనికి కారణం అవుతుంది:",
        "options": ["Goitre", "Diabetes (మధుమేహం)", "Ulcers", "Bleeding Gums"],
        "answer": 2,
        "explanation": "Lack of insulin causes Diabetes mellitus (inability to regulate blood glucose)."
    },
    {
        "id": 127,
        "subject": "EVS",
        "topic": "Optics",
        "question": "Opaque material among the following is / కింది వాటిలో అపారదర్శక పదార్థం:",
        "options": ["Glass (గాజు)", "Water (నీరు)", "Air (గాలి)", "Wood (చెక్క)"],
        "answer": 4,
        "explanation": "Wood does not allow light to pass through it, making it opaque."
    },
    {
        "id": 128,
        "subject": "EVS",
        "topic": "Optics",
        "question": "The materials through which objects can be seen, but not clearly are known as / వస్తువును చూడగలం కానీ స్పష్టంగా చూడలేమో ఆ పదార్థాలను ఇలా పిలుస్తారు:",
        "options": ["Transparent", "Opaque", "Translucent (పాక్షిక పారదర్శక)", "Rough"],
        "answer": 3,
        "explanation": "Translucent materials allow partial light transmission causing blurred visibility."
    },
    {
        "id": 136,
        "subject": "EVS",
        "topic": "Chemistry",
        "question": "Acids are present in this taste / ఆమ్లాలు ఈ రుచిలో ఉంటాయి:",
        "options": ["Bitter (చేదు)", "Sour (పుల్లని)", "Sweet (తీయని)", "Spicy (కారం)"],
        "answer": 2,
        "explanation": "Acids taste characteristically sour."
    },
    {
        "id": 137,
        "subject": "EVS",
        "topic": "Chemistry",
        "question": "The compound that turns red litmus paper into blue is / ఎరుపు లిట్మస్ ను నీలి రంగులోకి మార్చే పదార్థం:",
        "options": ["Acid (ఆమ్లం)", "Base (క్షారం)", "Water (నీరు)", "Neutral solution"],
        "answer": 2,
        "explanation": "Bases turn red litmus paper blue, while acids turn blue litmus red."
    },
    {
        "id": 183,
        "subject": "EVS",
        "topic": "Physics - Mechanics",
        "question": "The S.I. unit of force is / బలానికి ఎస్.ఐ. ప్రమాణం:",
        "options": ["Newton (న్యూటన్)", "Joule (జౌల్)", "Watt (వాట్)", "Erg (ఎర్గ్)"],
        "answer": 1,
        "explanation": "Force is measured in Newtons (N) in the SI system."
    },
    {
        "id": 184,
        "subject": "EVS",
        "topic": "Physics - Pressure",
        "question": "S.I Unit of pressure is / పీడనానికి S.I ప్రమాణం:",
        "options": ["Newton", "Pascal (పాస్కల్)", "Joule", "Watt"],
        "answer": 2,
        "explanation": "Pressure is force per unit area; its SI unit is the Pascal (N/m²)."
    }
]

# Add more Maths questions
maths_extra = [
    {
        "id": 4,
        "subject": "Maths",
        "topic": "Number Sense",
        "question": "The face value of 6 in 46,739 is / 46,739 అనే సంఖ్యలో 6 యొక్క సహజ విలువ:",
        "options": ["6000", "600", "60", "6"],
        "answer": 4,
        "explanation": "The face value of a digit is the digit itself, so face value of 6 is 6."
    },
    {
        "id": 20,
        "subject": "Maths",
        "topic": "Divisibility",
        "question": "The number which is exactly divisible by 4 is / 4 చే నిశ్శేషంగా భాగింపబడు సంఖ్య:",
        "options": ["23754", "83243", "56780", "40409"],
        "answer": 3,
        "explanation": "A number is divisible by 4 if its last two digits form a number divisible by 4. 80 / 4 = 20."
    },
    {
        "id": 21,
        "subject": "Maths",
        "topic": "Number Sense",
        "question": "The largest 4-digit number is / 4-అంకెల గరిష్ట సంఖ్య:",
        "options": ["9000", "9009", "9999", "8999"],
        "answer": 3,
        "explanation": "9999 is the greatest 4-digit integer."
    },
    {
        "id": 23,
        "subject": "Maths",
        "topic": "Fractions",
        "question": "The simplest form of 27/36 is / 27/36 భిన్నం యొక్క కనిష్ట రూపం:",
        "options": ["3/4", "4/3", "3/5", "3/7"],
        "answer": 1,
        "explanation": "Dividing numerator and denominator by 9 gives 27/36 = 3/4."
    },
    {
        "id": 28,
        "subject": "Maths",
        "topic": "Decimals",
        "question": "The value of 0.2 × 0.3 is / 0.2 × 0.3 యొక్క విలువ:",
        "options": ["0.6", "0.66", "0.06", "0.5"],
        "answer": 3,
        "explanation": "2 × 3 = 6; with two decimal places it becomes 0.06."
    },
    {
        "id": 34,
        "subject": "Maths",
        "topic": "Decimals & Money",
        "question": "The decimal form of 2 rupees 5 paise is / 2 రూపాయల 5 పైసల యొక్క దశాంశ రూపం:",
        "options": ["₹ 2.50", "₹ 2.05", "₹ 25.0", "₹ 0.25"],
        "answer": 2,
        "explanation": "5 paise = 5/100 rupees = 0.05 rupees. Total = ₹ 2.05."
    },
    {
        "id": 108,
        "subject": "Maths",
        "topic": "Ratio",
        "question": "The ratio of two numbers is 1:2 and their sum is 60. The largest number is / రెండు సంఖ్యల నిష్పత్తి 1:2 మరియు వాటి మొత్తం 60. గరిష్ట సంఖ్య:",
        "options": ["20", "40", "25", "45"],
        "answer": 2,
        "explanation": "Total parts = 1 + 2 = 3. 1 part = 60/3 = 20. Larger number = 2 × 20 = 40."
    },
    {
        "id": 114,
        "subject": "Maths",
        "topic": "Ratio",
        "question": "In a class, there are 51 boys and 68 girls. The ratio of the number of boys to girls is:",
        "options": ["3:5", "4:3", "3:2", "3:4"],
        "answer": 4,
        "explanation": "51 / 68 = (17 × 3) / (17 × 4) = 3:4."
    },
    {
        "id": 146,
        "subject": "Maths",
        "topic": "Percentages",
        "question": "A football team won 10 matches out of total matches played. If winning percentage was 40%, total matches played were:",
        "options": ["20", "25", "30", "24"],
        "answer": 2,
        "explanation": "40% of Total = 10 -> Total = 10 / 0.40 = 25 matches."
    },
    {
        "id": 230,
        "subject": "Maths",
        "topic": "Geometry - Symmetry",
        "question": "Number of symmetric lines of a square is / ఒక చతురస్రానికి గల రేఖా సౌష్టవాల సంఖ్య:",
        "options": ["1", "2", "3", "4"],
        "answer": 4,
        "explanation": "A square has 4 lines of symmetry: 2 through the midpoints of opposite sides and 2 along the diagonals."
    },
    {
        "id": 246,
        "subject": "Maths",
        "topic": "Geometry",
        "question": "Each external angle of an equilateral triangle is / సమబాహు త్రిభుజము యొక్క ప్రతి బాహ్య కోణము కొలత:",
        "options": ["60°", "120°", "100°", "90°"],
        "answer": 2,
        "explanation": "Interior angle of equilateral triangle = 60°. Exterior angle = 180° - 60° = 120°."
    },
    {
        "id": 260,
        "subject": "Maths",
        "topic": "Mensuration",
        "question": "The area of a square whose diagonal is 10 cm is (in cm²):",
        "options": ["50", "100", "150", "200"],
        "answer": 1,
        "explanation": "Area = (d²) / 2 = (10 × 10) / 2 = 50 cm²."
    },
    {
        "id": 261,
        "subject": "Maths",
        "topic": "Mensuration",
        "question": "If area of a square is 64 cm² then its perimeter is (in cm):",
        "options": ["16", "24", "32", "36"],
        "answer": 3,
        "explanation": "Side = √64 = 8 cm. Perimeter = 4 × 8 = 32 cm."
    },
    {
        "id": 278,
        "subject": "Maths",
        "topic": "Statistics",
        "question": "The mean of the data 10, 12, 14, 8, 6 and 4 is / దత్తాంశము సగటు:",
        "options": ["7", "8", "9", "10"],
        "answer": 3,
        "explanation": "Sum = 10 + 12 + 14 + 8 + 6 + 4 = 54. Mean = 54 / 6 = 9."
    },
    {
        "id": 316,
        "subject": "Maths",
        "topic": "Probability",
        "question": "When a die is thrown, the number of total possible outcomes is / పాచికను దొర్లించినపుడు వచ్చే మొత్తం పర్యవసానాల సంఖ్య:",
        "options": ["2", "4", "6", "8"],
        "answer": 3,
        "explanation": "A fair 6-sided die has sample space {1, 2, 3, 4, 5, 6} -> 6 outcomes."
    },
    {
        "id": 317,
        "subject": "Maths",
        "topic": "Probability",
        "question": "The probability of getting number 5 when a die is thrown once is / పాచికను విసరగా 5 వచ్చు సంభావ్యత:",
        "options": ["1/2", "1/5", "1/6", "1"],
        "answer": 3,
        "explanation": "Favorable outcome = 1 (number 5). Total outcomes = 6. Probability = 1/6."
    }
]

# Add more CDP questions
cdp_extra = [
    {
        "id": 7,
        "subject": "CDP",
        "topic": "Socialization",
        "question": "The first teacher of a child is / పిల్లలకు మొదటి గురువు ఎవరు?",
        "options": ["Mother (తల్లి)", "Father (తండ్రి)", "Teacher (గురువు)", "Friends (స్నేహితులు)"],
        "answer": 1,
        "explanation": "The mother is the child's primary caregiver and first teacher."
    },
    {
        "id": 77,
        "subject": "CDP",
        "topic": "Emotions",
        "question": "If parents constantly compare their children with other children, the children exhibit / తల్లిదండ్రులు పిల్లలను ఇతరులతో పోల్చినప్పుడు వారు ప్రదర్శించేది:",
        "options": ["Anger (కోపం / అసూయ)", "Mirthfulness", "Curiosity", "Happiness"],
        "answer": 1,
        "explanation": "Negative comparison evokes resentment, anger, and feelings of inadequacy."
    },
    {
        "id": 78,
        "subject": "CDP",
        "topic": "Emotions",
        "question": "Jealousy is a/an / అసూయ అనేది ఒక:",
        "options": ["pleasant emotion", "unpleasant emotion (బాధాజనిత ఉద్వేగం)", "no emotion", "positive emotion"],
        "answer": 2,
        "explanation": "Jealousy is an unpleasant, distressing negative emotion."
    },
    {
        "id": 86,
        "subject": "CDP",
        "topic": "Heredity & Environment",
        "question": "The author of the landmark book 'Hereditary Genius' is / 'హెరిడిటరీ జీనియస్' పుస్తక రచయిత:",
        "options": ["Gordan", "Freeman", "Pearson", "Galton (గాల్టన్)"],
        "answer": 4,
        "explanation": "Sir Francis Galton published 'Hereditary Genius' in 1869."
    },
    {
        "id": 87,
        "subject": "CDP",
        "topic": "Behaviorism",
        "question": "'Give me a dozen healthy infants... and I will train them to become any type of specialist (doctor, lawyer, artist, merchant-chief)' was proclaimed by:",
        "options": ["Freeman", "Pearson", "J.B. Watson (జె. బి. వాట్సన్)", "Bagley"],
        "answer": 3,
        "explanation": "John B. Watson, the founder of Behaviorism, made this famous environmentalist declaration."
    },
    {
        "id": 89,
        "subject": "CDP",
        "topic": "Developmental Factors",
        "question": "Factors that jointly affect the development of an individual are / వ్యక్తి వికాసాన్ని ప్రభావితం చేయు కారకాలు:",
        "options": ["Heredity only", "Environment only", "Instincts", "Heredity and Environment (అనువంశికత మరియు పరిసరాలు)"],
        "answer": 4,
        "explanation": "Development = Heredity × Environment."
    },
    {
        "id": 113,
        "subject": "CDP",
        "topic": "Developmental Stages",
        "question": "According to psychologists, 'Pre-Gang Age' corresponds to / మనోవిజ్ఞాన శాస్త్రవేత్తల ప్రకారం పూర్వ ముఠా దశ:",
        "options": ["Adulthood", "Early childhood (పూర్వ బాల్యదశ)", "Later childhood (ఉత్తర బాల్యదశ)", "Infancy"],
        "answer": 2,
        "explanation": "Early childhood (ages 2-6) is the Pre-gang age; Later childhood (ages 6-12) is the Gang age."
    },
    {
        "id": 114,
        "subject": "CDP",
        "topic": "Developmental Stages",
        "question": "According to psychologists, which of the following is NOT a feature of Early Childhood?",
        "options": ["Pre Gang age", "Exploratory age", "Creative age", "Gang age (ముఠా దశ)"],
        "answer": 4,
        "explanation": "Gang age belongs to Later Childhood, not Early Childhood."
    },
    {
        "id": 164,
        "subject": "CDP",
        "topic": "Perception",
        "question": "'Imagining a rope as a snake during night time' is an example of / 'చీకట్లో తాడును చూసి పాముగా భ్రమపడటం' దేనికి ఉదాహరణ?",
        "options": ["Creativity", "Illusion (భ్రమ)", "Hallucination (విభ్రమము)", "Reality"],
        "answer": 2,
        "explanation": "Misinterpreting an existing real object (rope as snake) is an Illusion."
    },
    {
        "id": 316,
        "subject": "CDP",
        "topic": "Personality Assessment",
        "question": "The Thematic Apperception Test (TAT) was developed by / TAT పరీక్షను రూపొందించిన వారు:",
        "options": ["CAT", "MMPI", "Murray and Morgan (ముర్రే మరియు మోర్గాన్)", "Hermann Rorschach"],
        "answer": 3,
        "explanation": "Henry A. Murray and Christiana D. Morgan developed the TAT in 1935."
    },
    {
        "id": 343,
        "subject": "CDP",
        "topic": "Defense Mechanisms",
        "question": "A grown man reverting to bed-wetting under extreme stress uses which defense mechanism? / రాత్రిపూట పక్క తడిపే యువకుడు ఉపయోగించే రక్షక తంత్రం:",
        "options": ["Regression (ప్రతిగమనం)", "Identification", "Compensation", "Fantasy"],
        "answer": 1,
        "explanation": "Reverting to an earlier, less mature stage of development is Regression."
    },
    {
        "id": 354,
        "subject": "CDP",
        "topic": "Defense Mechanisms",
        "question": "A student backward in studies shows great talent and excels in sports. This defense mechanism is:",
        "options": ["Regression", "Identification", "Compensation (పరిహారము)", "Displacement"],
        "answer": 3,
        "explanation": "Overcoming weakness in one area by excelling in another is Compensation."
    },
    {
        "id": 358,
        "subject": "CDP",
        "topic": "Learning Concept",
        "question": "Modification of behaviour through experience and training is called / అనుభవం మరియు శిక్షణ ద్వారా ప్రవర్తనలో వచ్చే మార్పు:",
        "options": ["Intelligence (ప్రజ్ఞ)", "Aptitude (సామర్థ్యం)", "Attitude (వైఖరి)", "Learning (అభ్యసనం)"],
        "answer": 4,
        "explanation": "Gates defined learning as the modification of behaviour through experience and training."
    },
    {
        "id": 484,
        "subject": "CDP",
        "topic": "Learning Curves",
        "question": "A temporary flat plateau where learning ceases to show progress is called / అభ్యసనం స్థంభించి పురోగమనం లేకుండా నిలిచిపోయే దశ:",
        "options": ["Extinct", "Plateau stage (పీఠభూమి దశ)", "Stage of fluctuation", "Initial spurt"],
        "answer": 2,
        "explanation": "The plateau stage represents a temporary cessation of observable learning progress."
    },
    {
        "id": 489,
        "subject": "CDP",
        "topic": "Special Education",
        "question": "Learning disability specifically associated with reading difficulties is / చదవడంలో అభ్యసన వైకల్యం:",
        "options": ["Dyslexia (డిస్లెక్సియా)", "Dysgraphia (డిస్గ్రాఫియా)", "Dyscalculia (డిస్కాల్క్యులియా)", "Dysphasia"],
        "answer": 1,
        "explanation": "Dyslexia is a specific learning disability affecting accurate and fluent word reading."
    },
    {
        "id": 494,
        "subject": "CDP",
        "topic": "Special Education",
        "question": "Learning disability specifically related to writing difficulties is / రాయడానికి సంబంధించిన వైకల్యం:",
        "options": ["Alexia", "Dysgraphia (డిస్‌గ్రాఫియా)", "Dyscalculia", "Dyslexia"],
        "answer": 2,
        "explanation": "Dysgraphia is a neurological condition impairing handwriting and fine motor skills."
    },
    {
        "id": 498,
        "subject": "CDP",
        "topic": "Special Education",
        "question": "Learning disability related to mathematical calculations and arithmetic concepts is:",
        "options": ["Dysphasia", "Aphasia", "Dyscalculia (డిస్కాల్క్యులియా)", "Dyslexia"],
        "answer": 3,
        "explanation": "Dyscalculia affects the ability to acquire mathematical and arithmetic skills."
    },
    {
        "id": 512,
        "subject": "CDP",
        "topic": "Curriculum Frameworks",
        "question": "Which of the following is NOT recommended by NCF-2005? / NCF 2005 మార్గదర్శక సూత్రాలలో లేని వాక్యం:",
        "options": [
            "Simplification of examination pattern",
            "Connecting curricular knowledge with real experiences",
            "Strengthening Rote learning method (కంఠస్థ పద్ధతులను ప్రోత్సహించడం)",
            "Enriching the curriculum"
        ],
        "answer": 3,
        "explanation": "NCF-2005 explicitly recommends shifting away from rote memorization methods."
    }
]

# Merge extra questions safely avoiding duplicate IDs
for q in eng_extra:
    if not any(x['id'] == q['id'] for x in data['English']):
        data['English'].append(q)

for q in tel_extra:
    if not any(x['id'] == q['id'] for x in data['Telugu']):
        data['Telugu'].append(q)

for q in evs_extra:
    if not any(x['id'] == q['id'] for x in data['EVS']):
        data['EVS'].append(q)

for q in maths_extra:
    if not any(x['id'] == q['id'] for x in data['Maths']):
        data['Maths'].append(q)

for q in cdp_extra:
    if not any(x['id'] == q['id'] for x in data['CDP']):
        data['CDP'].append(q)

# Write updated databases
with open("data/english.json", "w", encoding="utf-8") as f:
    json.dump(data['English'], f, ensure_ascii=False, indent=2)

with open("data/telugu.json", "w", encoding="utf-8") as f:
    json.dump(data['Telugu'], f, ensure_ascii=False, indent=2)

with open("data/evs.json", "w", encoding="utf-8") as f:
    json.dump(data['EVS'], f, ensure_ascii=False, indent=2)

with open("data/maths.json", "w", encoding="utf-8") as f:
    json.dump(data['Maths'], f, ensure_ascii=False, indent=2)

with open("data/cdp.json", "w", encoding="utf-8") as f:
    json.dump(data['CDP'], f, ensure_ascii=False, indent=2)

with open("data/all_subjects.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Expanded Question Counts:")
for subj, qs in data.items():
    print(f"- {subj}: {len(qs)} questions")
print(f"Grand Total: {sum(len(v) for v in data.values())} questions across all 5 TET subjects.")
