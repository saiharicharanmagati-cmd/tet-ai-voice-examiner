import json
import os

# We will read existing and append high-value questions from the OCR for all 5 subjects
with open("data/all_subjects.json", "r", encoding="utf-8") as f:
    db = json.load(f)

# Extra Telugu Questions from OCR
more_telugu = [
    {
        "id": 11,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం",
        "question": "ఎప్పుడు సంపద గలిగిన / అప్పుడు బంధువులు వత్తురది యెట్లన్నన్ / తెప్పలుగా చెరువు నిండిన / కప్పలు పదివేలు చేరు కదరా సుమతీ! - పై పద్యం ఆధారంగా సరైనది ఏది?",
        "options": [
            "సంపదలు కలిగినప్పుడు బంధువులు వస్తారు",
            "సంపదలు లేనప్పుడు బంధువులు వస్తారు",
            "బంధువులు వచ్చినప్పుడు సంపదలు కలుగును",
            "సంపదలు కలగాలంటే బంధువులు రావాలి"
        ],
        "answer": 1,
        "explanation": "చెరువులో నీరు నిండితే కప్పలు చేరినట్లే, సంపదలు ఉన్నప్పుడు మాత్రమే బంధువులు వస్తారు."
    },
    {
        "id": 13,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం",
        "question": "ఆత్మశుద్ధి లేని ఆచారమది యేల / భాండశుద్ధిలేని పాకమేల / చిత్తశుద్ధి లేని శివపూజలేలరా - పై పద్యం ఆధారంగా వంట చేయడానికి దేని శుద్ధి అవసరం?",
        "options": ["ఆత్మశుద్ధి", "భాండశుద్ధి", "చిత్తశుద్ధి", "పైవన్నీ"],
        "answer": 2,
        "explanation": "భాండశుద్ధి (పాత్రల శుద్ధి) లేకుండా వంట చేయడం వ్యర్థం."
    },
    {
        "id": 15,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం",
        "question": "చదివించిరి నను గురువులు / చదివితి ధర్మార్థ ముఖ్య శాస్త్రమ్ములు నే - పై పద్యం ఆధారంగా చదివించిన వారు ఎవరు?",
        "options": ["మిత్రులు", "తల్లిదండ్రులు", "గురువులు", "అన్నదమ్ములు"],
        "answer": 3,
        "explanation": "పద్యంలో 'చదివించిరి నను గురువులు' అని స్పష్టంగా పేర్కొనబడింది."
    },
    {
        "id": 17,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం",
        "question": "చదువనివా డజ్ఞుండగు / జదివిన సదసద్వివేక చతురత గలుగున్ - పై పద్యం ఆధారంగా సరైనది ఏది?",
        "options": [
            "చదువుకొననిచో మంచి చెడుల విచక్షణ కలుగును",
            "చదవని వాడు జ్ఞాని అగును",
            "చదువుకొన్నచో మంచి చెడుల విచక్షణ కలుగును",
            "శ్రేష్ఠులకు చదువు చెప్పు"
        ],
        "answer": 3,
        "explanation": "చదువుకోవడం వల్ల మాత్రమే మంచి చెడులను వివేచించే చతురత కలుగుతుంది."
    },
    {
        "id": 19,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం",
        "question": "క్రోధము తపముం జెఱచును / గ్రోధము యణిమాదులైన గుణముల బాపుం - తపమును పాడు చేయునది ఏది?",
        "options": ["శాంతం", "భయం", "గాంభీర్యం", "క్రోధము"],
        "answer": 4,
        "explanation": "క్రోధము (కోపము) తపస్సును, మంచి గుణములను పాడుచేస్తుంది."
    },
    {
        "id": 20,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం",
        "question": "చదలమీద సూర్యచంద్రులుండెడి దాక / ఉర్విమీద కొండలుండువరకు - ఆకాశంలో వీరు ఉంటారు:",
        "options": ["సూర్యచంద్రులు", "ఉర్వి", "పర్వతాలు", "పైవన్నీ"],
        "answer": 1,
        "explanation": "'చదల' అనగా ఆకాశం. ఆకాశంలో సూర్యచంద్రులు ఉంటారు."
    },
    {
        "id": 21,
        "subject": "Telugu",
        "topic": "అపరిచిత పద్యం",
        "question": "పద్యమన్నది వేయేండ్ల పసిడి పంట / పద్యమన్నది తెలుగింటి పాడిపంట - పద్యం అనేది ఎన్నిసంవత్సరాల బంగారుపంట?",
        "options": ["వంద", "వెయ్యి", "లక్ష", "రెండువందలు"],
        "answer": 2,
        "explanation": "'పద్యమన్నది వేయేండ్ల పసిడి పంట' - వేయి సంవత్సరాల బంగారు పంట."
    },
    {
        "id": 34,
        "subject": "Telugu",
        "topic": "పద్య భావాలు",
        "question": "చిత్తశుద్ధి లేని శివపూజ ఎలాంటిది?",
        "options": ["వ్యర్థం", "ప్రయోజన కరం", "అవసరం", "మోక్షదాయకం"],
        "answer": 1,
        "explanation": "మనసులో భక్తి లేని పూజ నిరర్థకము / వ్యర్థం."
    },
    {
        "id": 35,
        "subject": "Telugu",
        "topic": "పద్య భావాలు",
        "question": "ఈ లోకంలో ఎవరు అత్యంత అధిక సంపన్నుడు?",
        "options": ["అప్పులు ఇచ్చేవాడు", "అప్పు ఇవ్వని వాడు", "అప్పుచేసే వాడు", "అప్పులేని వాడు"],
        "answer": 4,
        "explanation": "అప్పులేని వాడే ఈ లోకంలో నిజమైన ధనవంతుడు."
    },
    {
        "id": 57,
        "subject": "Telugu",
        "topic": "సాహిత్యం",
        "question": "భారత ప్రభుత్వం దేవులపల్లి కృష్ణశాస్త్రి గారిని ఈ బిరుదుతో సత్కరించింది:",
        "options": ["ఆంధ్రా షెల్లీ", "పద్మభూషణ్", "పద్మవిభూషణ్", "కళాప్రపూర్ణ"],
        "answer": 2,
        "explanation": "భారత ప్రభుత్వం దేవులపల్లి కృష్ణశాస్త్రి గారికి 'పద్మభూషణ్' పురస్కారాన్ని ఇచ్చింది."
    },
    {
        "id": 61,
        "subject": "Telugu",
        "topic": "పురాణేతిహాసాలు",
        "question": "కురుక్షేత్రయుద్ధంలో విజయం సాధించిన ధర్మరాజు పాలించిన ప్రాంతం ఏది?",
        "options": ["అయోధ్య", "హస్తినాపురం", "అవంతిపురం", "రామాపురం"],
        "answer": 2,
        "explanation": "ధర్మరాజు పాండవుల రాజధాని హస్తినాపురాన్ని పాలించాడు."
    },
    {
        "id": 96,
        "subject": "Telugu",
        "topic": "సాహిత్య బిరుదులు",
        "question": "'గద్యతిక్కన' గా బిరుదు పొందిన వారు ఎవరు?",
        "options": ["గరిమెళ్ళ సత్యనారాయణ", "కందుకూరి వీరేశలింగం", "చిలుకూరి దేవపుత్ర", "బి.వి. నరసింహారావు"],
        "answer": 2,
        "explanation": "తెలుగు వచన రచనా పితామహుడు కందుకూరి వీరేశలింగం గారికి 'గద్యతిక్కన' అనే బిరుదు కలదు."
    },
    {
        "id": 101,
        "subject": "Telugu",
        "topic": "సాహిత్య బిరుదులు",
        "question": "'కవిసార్వభౌముడు' అనే బిరుదు కలిగిన ప్రాచీన కవి ఎవరు?",
        "options": ["పోతన", "శ్రీనాథుడు", "నన్నయ", "ఎర్రన"],
        "answer": 2,
        "explanation": "శ్రీనాథ మహాకవికి 'కవిసార్వభౌమ' బిరుదు కలదు."
    },
    {
        "id": 102,
        "subject": "Telugu",
        "topic": "నవలలు - రచయితలు",
        "question": "'బారిష్టర్ పార్వతీశం' హాస్య నవల రచయిత ఎవరు?",
        "options": ["రాయప్రోలు సుబ్బారావు", "కందుకూరి వీరేశలింగం", "మొక్కపాటి నరసింహశాస్త్రి", "గరిమెళ్ళ సత్యనారాయణ"],
        "answer": 3,
        "explanation": "'బారిష్టర్ పార్వతీశం' ప్రసిద్ధ హాస్య నవల మొక్కపాటి నరసింహశాస్త్రి గారి రచన."
    },
    {
        "id": 131,
        "subject": "Telugu",
        "topic": "దేశభక్తి గేయాలు",
        "question": "'దేశమును ప్రేమించుమన్నా....' గేయంలో ఎలాంటి మాటలు కట్టిపెట్టమన్నాడు గురజాడ?",
        "options": ["పరుషపు మాటలు", "చెడ్డ మాటలు", "ఒట్టి మాటలు", "గట్టి మాటలు"],
        "answer": 3,
        "explanation": "'పాడిపంటలు పొంగిపొర్లే దారిలో నువు పాటుపడవోయ్, తిండి కలిగితే కండ కలదోయ్, కండ కలవాడేను మనిషోయ్, దేశమంటే మట్టి కాదోయ్ దేశమంటే మనుషులోయ్, ఒట్టి మాటలు కట్టిపెట్టోయ్ గట్టిమేల్ తలపెట్టవోయ్'."
    },
    {
        "id": 281,
        "subject": "Telugu",
        "topic": "పర్యాయపదాలు",
        "question": "'దుగ్ధము' పదానికి పర్యాయపదాలు:",
        "options": ["సుధ, అమృతం", "జలము, నీరు", "పాలు, క్షీరము", "నెయ్యి, ఘృతము"],
        "answer": 3,
        "explanation": "దుగ్ధము అనగా పాలు, క్షీరము."
    },
    {
        "id": 361,
        "subject": "Telugu",
        "topic": "సామెతలు",
        "question": "కింది వానిలో సామెతను గుర్తించండి:",
        "options": [
            "రోట్లో తలదూర్చి రోకటి పోటుకు వెరచినట్లు",
            "అక్షయపాత్ర",
            "కుంభకర్ణ నిద్ర",
            "కలి కాని కలి"
        ],
        "answer": 1,
        "explanation": "'రోట్లో తలదూర్చి రోకటి పోటుకు వెరచినట్లు' అనేది ఒక ప్రసిద్ధ సామెత."
    },
    {
        "id": 380,
        "subject": "Telugu",
        "topic": "వ్యాకరణం",
        "question": "ఒకటి కంటే ఎక్కువ విషయాలను తెలిపే వచనం ఏది?",
        "options": ["సరళవచనం", "బహువచనం", "ఏకైక వచనం", "ఏకవచనం"],
        "answer": 2,
        "explanation": "ఒకదానిని తెలిపితే ఏకవచనం, అంతకంటే ఎక్కువను తెలిపితే బహువచనం."
    },
    {
        "id": 406,
        "subject": "Telugu",
        "topic": "వర్ణమాల",
        "question": "క నుండి మ వరకు గల అక్షరాలను ఎన్ని వర్గాలుగా విభజించారు?",
        "options": ["4", "6", "7", "5"],
        "answer": 4,
        "explanation": "క వర్గము, చ వర్గము, ట వర్గము, త వర్గము, ప వర్గము - మొత్తం 5 వర్గాలు."
    },
    {
        "id": 416,
        "subject": "Telugu",
        "topic": "ఛందస్సు",
        "question": "రెండు మాత్రల కాలంలో ఉచ్ఛరించే అక్షరాలను ఏమంటారు?",
        "options": ["దీర్ఘాలు", "హ్రస్వాలు", "అంతస్థాలు", "ఊష్మాలు"],
        "answer": 1,
        "explanation": "ఒక మాత్ర కాలంలో పలికేవి హ్రస్వాలు (లఘువులు), రెండు మాత్రల కాలంలో పలికేవి దీర్ఘాలు (గురువులు)."
    },
    {
        "id": 444,
        "subject": "Telugu",
        "topic": "సమాసాలు",
        "question": "కింది పదాలలో ద్వంద్వసమాస పదాన్ని గుర్తించండి:",
        "options": ["అన్నదమ్ములు", "రెండురోజులు", "చెట్లనీడలు", "పాలపుంతలు"],
        "answer": 1,
        "explanation": "అన్నయును, తమ్ముడును = అన్నదమ్ములు (ద్వంద్వ సమాసము)."
    },
    {
        "id": 470,
        "subject": "Telugu",
        "topic": "ఛందస్సు",
        "question": "మూడు అక్షరాల గణాలు మొత్తం ఎన్ని?",
        "options": ["6", "8", "9", "12"],
        "answer": 2,
        "explanation": "భ, జ, స, య, ర, త, మ, న - మొత్తం 8 మూడు అక్షరాల గణాలు (యమాతారాజభానసలగం)."
    },
    {
        "id": 478,
        "subject": "Telugu",
        "topic": "ఛందస్సు",
        "question": "చంపకమాల పద్యపాదంలో వచ్చే గణాలు ఏవి?",
        "options": [
            "భ ర న భ భ ర వ",
            "మ స జ స త త గ",
            "స భ ర న మ య వ",
            "న జ భ జ జ జ ర"
        ],
        "answer": 4,
        "explanation": "చంపకమాల పద్యపాదంలో 'న-జ-భ-జ-జ-జ-ర' అనే గణాలు వరుసగా వస్తాయి (21 అక్షరాలు, 11వ అక్షరం యతి)."
    },
    {
        "id": 484,
        "subject": "Telugu",
        "topic": "అలంకారాలు",
        "question": "ఉపమేయ, ఉపమానాలకు మనోహరమైన పోలిక చెప్పడాన్ని ఏ అలంకారం అంటారు?",
        "options": ["రూపకాలంకారం", "ఉపమాలంకారం", "అతిశయోక్తి అలంకారం", "ఉత్ప్రేక్షాలంకారం"],
        "answer": 2,
        "explanation": "ఉపమేయానికి ఉపమానంతో అందమైన పోలిక చెబితే అది ఉపమాలంకారం."
    },
    {
        "id": 499,
        "subject": "Telugu",
        "topic": "అలంకారాలు",
        "question": "గోరంతను కొండంతలుగా చేసి వర్ణించే అలంకారం ఏది?",
        "options": ["ఉపమాలంకారం", "రూపకాలంకారం", "అతిశయోక్తి అలంకారం", "స్వభావోక్తి అలంకారం"],
        "answer": 3,
        "explanation": "ఉన్నదాని కంటే ఎక్కువ చేసి ఆశ్చర్యం కలిగించేలా చెప్పడం 'అతిశయోక్తి అలంకారం'."
    },
    {
        "id": 534,
        "subject": "Telugu",
        "topic": "బోధనా పద్ధతులు",
        "question": "భాష నేర్చుకోవడానికి ప్రథమ సోపానం ఏది?",
        "options": ["భాషణం", "లేఖనం", "పఠనం", "శ్రవణం"],
        "answer": 4,
        "explanation": "భాషా నైపుణ్యాలలో మొదటిది శ్రవణం (వినడం), తరువాత భాషణం (మాట్లాడటం), పఠనం (చదవడం), లేఖనం (రాయడం)."
    }
]

# Extra Maths Questions from OCR
more_maths = [
    {
        "id": 5,
        "subject": "Maths",
        "topic": "Place Value & Face Value",
        "question": "The difference between place value and face value of 5 in 65,349 is / 65,349 అనే సంఖ్యలో 5 యొక్క స్థాన విలువ, ముఖ విలువల మధ్య తేడా:",
        "options": ["5000", "4995", "5005", "5"],
        "answer": 2,
        "explanation": "Place value of 5 = 5,000; Face value of 5 = 5. Difference = 5000 - 5 = 4995."
    },
    {
        "id": 6,
        "subject": "Maths",
        "topic": "Number Formation",
        "question": "The greatest 7-digit number formed by using the digits 0, 7, 4, 1, 3, 6 and 2 is / 0,7,4,1,3,6 మరియు 2 లచే ఏర్పడే 7-అంకెల పెద్ద సంఖ్య:",
        "options": ["76,43,102", "76,42,310", "76,43,210", "74,32,106"],
        "answer": 3,
        "explanation": "Arranging digits in descending order: 7, 6, 4, 3, 2, 1, 0 -> 76,43,210."
    },
    {
        "id": 16,
        "subject": "Maths",
        "topic": "Unitary Method",
        "question": "The cost of 63 erasers is ₹315. The cost of 42 erasers is / 63 రబ్బరుల వెల ₹315 అయిన 42 రబ్బరుల వెల:",
        "options": ["₹105", "₹210", "₹240", "₹270"],
        "answer": 2,
        "explanation": "Cost of 1 eraser = 315 / 63 = ₹5. Cost of 42 erasers = 42 × 5 = ₹210."
    },
    {
        "id": 18,
        "subject": "Maths",
        "topic": "Integers",
        "question": "The number of integers lying strictly between -3 and +3 is / -3 మరియు +3 ల మధ్య గల పూర్ణసంఖ్యల సంఖ్య:",
        "options": ["0", "5", "3", "8"],
        "answer": 2,
        "explanation": "Integers between -3 and +3 are: -2, -1, 0, 1, 2. Count = 5."
    },
    {
        "id": 32,
        "subject": "Maths",
        "topic": "Fractions",
        "question": "What fraction of a day is 8 hours? / ఒక రోజులో 8 గంటలు ఎన్నవ భాగం?",
        "options": ["1/8", "24/8", "8/24 (1/3)", "8"],
        "answer": 3,
        "explanation": "A full day has 24 hours. Fraction = 8 / 24 = 1/3."
    },
    {
        "id": 33,
        "subject": "Maths",
        "topic": "Averages",
        "question": "The average of 4.2, 3.8, and 7.6 is / 4.2, 3.8, 7.6 యొక్క సగటు:",
        "options": ["4.8", "5.2", "6.3", "3.8"],
        "answer": 2,
        "explanation": "Sum = 4.2 + 3.8 + 7.6 = 15.6. Average = 15.6 / 3 = 5.2."
    },
    {
        "id": 41,
        "subject": "Maths",
        "topic": "Word Problems - Age",
        "question": "Ravi is 14 years old. His mother is 23 years older than Ravi. His mother’s age is: / రవి వయస్సు 14 సంవత్సరాలు. తల్లి వయస్సు రవి కంటే 23 సంవత్సరాలు ఎక్కువ. తల్లి వయస్సు:",
        "options": ["37 years", "38 years", "47 years", "49 years"],
        "answer": 1,
        "explanation": "Mother's age = 14 + 23 = 37 years."
    },
    {
        "id": 43,
        "subject": "Maths",
        "topic": "LCM",
        "question": "The least common multiple (LCM) of 24, 32 and 48 is / 24, 32 మరియు 48 ల కనిష్ట సామాన్య గుణిజం:",
        "options": ["48", "96", "72", "64"],
        "answer": 2,
        "explanation": "48 = 2^4 * 3, 32 = 2^5, 24 = 2^3 * 3. LCM = 2^5 * 3 = 32 * 3 = 96."
    },
    {
        "id": 55,
        "subject": "Maths",
        "topic": "LCM & Number Sense",
        "question": "The smallest 3-digit number which is exactly divisible by 6, 8 and 12 is:",
        "options": ["100", "120", "180", "240"],
        "answer": 2,
        "explanation": "LCM(6, 8, 12) = 24. Multiples of 24: 24, 48, 72, 96, 120. Smallest 3-digit is 120."
    },
    {
        "id": 59,
        "subject": "Maths",
        "topic": "HCF",
        "question": "HCF of any two consecutive even numbers is / రెండు వరుస సరి సంఖ్యల గ.సా.కా. విలువ:",
        "options": ["1", "2", "3", "4"],
        "answer": 2,
        "explanation": "Any two consecutive even numbers (e.g. 2n and 2n+2) always have a greatest common divisor of 2."
    },
    {
        "id": 71,
        "subject": "Maths",
        "topic": "Squares",
        "question": "The number of natural numbers lying between 9² and 10² is:",
        "options": ["18", "20", "24", "16"],
        "answer": 1,
        "explanation": "Between n² and (n+1)², there are 2n non-perfect square numbers: 2 × 9 = 18."
    },
    {
        "id": 92,
        "subject": "Maths",
        "topic": "Squares and Cubes",
        "question": "Which of the following numbers is both a perfect square and a perfect cube? / ఖచ్చిత వర్గం మరియు ఖచ్చిత ఘనం రెండూ అయ్యే సంఖ్య:",
        "options": ["27", "64", "36", "48"],
        "answer": 2,
        "explanation": "64 = 8² and 64 = 4³."
    },
    {
        "id": 131,
        "subject": "Maths",
        "topic": "Percentages",
        "question": "There are 120 voters, 90 of them voted 'YES'. The percentage of voted 'YES' is:",
        "options": ["80%", "60%", "70%", "75%"],
        "answer": 4,
        "explanation": "(90 / 120) × 100% = (3 / 4) × 100% = 75%."
    },
    {
        "id": 178,
        "subject": "Maths",
        "topic": "Compound Interest",
        "question": "The compound interest on ₹12,600 for 2 years at 10% per annum compounded annually is:",
        "options": ["₹2,646", "₹2,676", "₹2,466", "₹2,546"],
        "answer": 1,
        "explanation": "A = 12600 × (1.1)² = 12600 × 1.21 = ₹15,246. CI = 15246 - 12600 = ₹2,646."
    },
    {
        "id": 226,
        "subject": "Maths",
        "topic": "Geometry - Lines & Angles",
        "question": "If a transversal intersects two parallel lines and one co-interior angle is 60°, the other co-interior angle is:",
        "options": ["60°", "120°", "30°", "40°"],
        "answer": 2,
        "explanation": "Consecutive interior (co-interior) angles are supplementary: 180° - 60° = 120°."
    },
    {
        "id": 236,
        "subject": "Maths",
        "topic": "Geometry - Triangles",
        "question": "If angles of a triangle are in the ratio 2:3:4, then the largest angle is:",
        "options": ["20°", "40°", "60°", "80°"],
        "answer": 4,
        "explanation": "Total parts = 2 + 3 + 4 = 9. 1 part = 180° / 9 = 20°. Largest angle = 4 × 20° = 80°."
    },
    {
        "id": 254,
        "subject": "Maths",
        "topic": "Geometry - Polygons",
        "question": "Each external angle of a regular octagon is / ఒక క్రమ అష్టభుజి యొక్క ప్రతి బాహ్య కోణము విలువ:",
        "options": ["30°", "36°", "45°", "72°"],
        "answer": 3,
        "explanation": "External angle = 360° / n = 360° / 8 = 45°."
    },
    {
        "id": 267,
        "subject": "Maths",
        "topic": "Geometry - Polygons",
        "question": "Number of diagonals in a regular hexagon is / ఒక షడ్భుజి యందు కల కర్ణముల సంఖ్య:",
        "options": ["6", "9", "10", "12"],
        "answer": 2,
        "explanation": "Number of diagonals in an n-gon = n(n-3)/2 = 6 × 3 / 2 = 9."
    },
    {
        "id": 274,
        "subject": "Maths",
        "topic": "Statistics History",
        "question": "The founder of the Indian Statistical Institute (ISI) in Kolkata was:",
        "options": ["P. C. Manohar", "P. C. Sirkar", "P. C. Mahalanobis (మహల్ నోబిస్)", "P. C. Madhava Iyer"],
        "answer": 3,
        "explanation": "Professor Prasanta Chandra Mahalanobis founded the Indian Statistical Institute in 1931."
    },
    {
        "id": 319,
        "subject": "Maths",
        "topic": "Probability",
        "question": "A bag has 4 red balls and 2 yellow balls. What is the probability of drawing a red ball randomly?",
        "options": ["1/2", "1/3", "2/3", "1/6"],
        "answer": 3,
        "explanation": "Total balls = 4 + 2 = 6. Favorable = 4. P(Red) = 4 / 6 = 2/3."
    },
    {
        "id": 470,
        "subject": "Maths",
        "topic": "Solid Geometry",
        "question": "Number of edges in a cube is / ఒక సమఘనం యొక్క అంచుల సంఖ్య:",
        "options": ["6", "3", "10", "12"],
        "answer": 4,
        "explanation": "A cube has 6 faces, 8 vertices, and 12 straight edges."
    },
    {
        "id": 514,
        "subject": "Maths",
        "topic": "Maths Pedagogy",
        "question": "Who wrote the landmark treatise 'Ganitha Saara Sangraham'?",
        "options": ["Boudhayana", "Mahaveeracharya (మహావీరాచార్యులు)", "Aryabhata", "Bhaskaracharya"],
        "answer": 2,
        "explanation": "Mahāvīrācārya (9th century Jain mathematician) authored 'Ganita Sara Sangraha'."
    }
]

# Extra EVS Questions from OCR
more_evs = [
    {
        "id": 9,
        "subject": "EVS",
        "topic": "Plant Biology",
        "question": "The leaves of this plant look like our open palm / ఈ మొక్క యొక్క పత్రాలు మన హస్తాకారంలో కనిపిస్తాయి:",
        "options": ["Banana (అరటి)", "Hibiscus (మందార)", "Pudina (పుదీనా)", "Papaya (బొప్పాయి)"],
        "answer": 4,
        "explanation": "Papaya leaves have deeply palmately lobed venation resembling a human hand/palm."
    },
    {
        "id": 14,
        "subject": "EVS",
        "topic": "Food Habits",
        "question": "Identify the Herbivore among the following / క్రింది వానిలో శాఖాహారిని గుర్తించండి:",
        "options": ["Wolf (తోడేలు)", "Giraffe (జిరాఫీ)", "Rat (ఎలుక)", "Bear (ఎలుగుబంటి)"],
        "answer": 2,
        "explanation": "Giraffes are strictly herbivorous browsers feeding exclusively on tree canopies and leaves."
    },
    {
        "id": 16,
        "subject": "EVS",
        "topic": "Food Habits",
        "question": "Identify the Omnivore among the following / క్రింది వానిలో ఉభయాహారిని గుర్తించండి:",
        "options": ["Hen (కోడి)", "Wolf (తోడేలు)", "Zebra (జీబ్రా)", "Giraffe (జిరాఫీ)"],
        "answer": 1,
        "explanation": "Chickens/hens consume both plant grains and worms/insects, making them omnivorous."
    },
    {
        "id": 37,
        "subject": "EVS",
        "topic": "Community Health",
        "question": "The toll-free phone number for free health advice and assistance is / ఉచిత వైద్య సలహాలను అందించే టోల్ ఫ్రీ నంబరు:",
        "options": ["100", "104", "116", "101"],
        "answer": 2,
        "explanation": "104 is the state toll-free health helpline service."
    },
    {
        "id": 41,
        "subject": "EVS",
        "topic": "Birds",
        "question": "This bird makes big holes in the trunk of trees / ఈ పక్షి చెట్ల కాండానికి పెద్ద తొర్రలు చేయును:",
        "options": ["Sparrow (పిచ్చుక)", "Weaver bird (గిజిగాడు)", "Woodpecker (వడ్రంగి పిట్ట)", "Crow (కాకి)"],
        "answer": 3,
        "explanation": "Woodpeckers chisel holes into tree bark using their strong, pointed beaks."
    },
    {
        "id": 65,
        "subject": "EVS",
        "topic": "Ecology",
        "question": "The organisms that prepare their own food are / తమ ఆహారాన్ని తామే తయారు చేసుకొనే జీవులు:",
        "options": ["Heterotrophs (పర పోషకాలు)", "Saprotrophs (పూతికహారులు)", "Parasites (పరాన్నజీవులు)", "Autotrophs (స్వయంపోషకాలు)"],
        "answer": 4,
        "explanation": "Autotrophs (green plants) produce their own nourishment from inorganic substances."
    },
    {
        "id": 78,
        "subject": "EVS",
        "topic": "Human Body",
        "question": "The length of the small intestine in adult humans is approximately:",
        "options": ["8 meters", "10 meters", "2 meters", "6 meters"],
        "answer": 4,
        "explanation": "The human small intestine measures approximately 6 meters (around 20 feet) in length."
    },
    {
        "id": 81,
        "subject": "EVS",
        "topic": "Microbiology",
        "question": "The unicellular organism that moves and captures food using pseudopodia is:",
        "options": ["Amoeba (అమీబా)", "Paramecium (పారామీషియం)", "Euglena (యూగ్లీనా)", "Diatom"],
        "answer": 1,
        "explanation": "Amoeba uses pseudopodia (false feet) for locomotion and engulfing prey via phagocytosis."
    },
    {
        "id": 82,
        "subject": "EVS",
        "topic": "Dentition",
        "question": "The human teeth used for cutting and biting food are / కత్తిరించడానికి మరియు కొరకడానికి ఉపయోగపడే దంతాలు:",
        "options": ["Canines (రదనికలు)", "Premolars (అగ్రచర్వణకాలు)", "Incisors (కుంతకాలు)", "Molars (చర్వణకాలు)"],
        "answer": 3,
        "explanation": "Incisors are flat, chisel-edged front teeth specialized for cutting and biting food."
    },
    {
        "id": 91,
        "subject": "EVS",
        "topic": "Circulatory System",
        "question": "Blood vessels that transport oxygenated blood away from the heart to all body parts are:",
        "options": ["Arteries (ధమనులు)", "Veins (సిరలు)", "Lymph vessels", "Capillaries"],
        "answer": 1,
        "explanation": "Arteries carry blood away from the pumping chambers of the heart to the body."
    },
    {
        "id": 155,
        "subject": "EVS",
        "topic": "Optics - Mirrors",
        "question": "The curved mirrors used by dentists to see magnified images of teeth are:",
        "options": ["Convex mirrors", "Concave mirrors (పుటాకార దర్పణాలు)", "Plane mirrors", "Coloured mirrors"],
        "answer": 2,
        "explanation": "Concave mirrors produce an upright, magnified virtual image when the object is inside the focal point."
    },
    {
        "id": 156,
        "subject": "EVS",
        "topic": "Optics - Mirrors",
        "question": "These mirrors provide a wide field of view and are used as rear-view mirrors in vehicles:",
        "options": ["Concave mirrors", "Convex mirrors (కుంభాకార దర్పణాలు)", "Plane mirrors", "Cylindrical mirrors"],
        "answer": 2,
        "explanation": "Convex mirrors always form diminished, erect virtual images with an expansive field of view."
    },
    {
        "id": 265,
        "subject": "EVS",
        "topic": "Geography of Andhra Pradesh",
        "question": "Lambasingi in Visakhapatnam Agency is famously known as:",
        "options": ["Andhra Jaipur", "Andhra Kashmir (ఆంధ్రా కాశ్మీర్)", "Andhra Cherrapunji", "Andhra Desert"],
        "answer": 2,
        "explanation": "Due to its sub-zero winter temperatures and misty hills, Lambasingi is called 'Andhra Kashmir'."
    },
    {
        "id": 279,
        "subject": "EVS",
        "topic": "Solar System",
        "question": "Identify the 'Blue Planet' in our solar system / నీలి గ్రహంను గుర్తించండి:",
        "options": ["Mars (అంగారకుడు)", "Uranus (వరుణుడు)", "Earth (భూమి)", "Saturn (శని)"],
        "answer": 3,
        "explanation": "Earth is termed the Blue Planet because over 71% of its surface is covered by oceans."
    },
    {
        "id": 338,
        "subject": "EVS",
        "topic": "Indian History",
        "question": "The last sultan of the Delhi Sultanate was / ఢిల్లీ సుల్తానులలో చివరి పాలకుడు ఎవరు?",
        "options": ["Iltutmish", "Ibrahim Lodi (ఇబ్రహీం లోడీ)", "Alauddin Khilji", "Firoz Shah Tughlaq"],
        "answer": 2,
        "explanation": "Ibrahim Lodi was defeated by Babur in the First Battle of Panipat (1526), ending the Delhi Sultanate."
    },
    {
        "id": 389,
        "subject": "EVS",
        "topic": "Political Science",
        "question": "This country is recognized as the historical birthplace of Democracy:",
        "options": ["Denmark", "Greece (గ్రీసు)", "France", "Russia"],
        "answer": 2,
        "explanation": "Ancient Athens, Greece, is the birthplace of direct democratic governance."
    },
    {
        "id": 390,
        "subject": "EVS",
        "topic": "Political Science",
        "question": "Democracy is 'Government of the people, by the people, for the people' was stated by:",
        "options": ["Jaya Prakash Narayana", "Aravind Ghosh", "Abraham Lincoln (అబ్రహం లింకన్)", "Annie Besant"],
        "answer": 3,
        "explanation": "Abraham Lincoln delivered this famous definition in his 1863 Gettysburg Address."
    },
    {
        "id": 430,
        "subject": "EVS",
        "topic": "History of Religions",
        "question": "Gautama Buddha's birth place 'Lumbini' is located in / బుద్ధుడు జన్మించిన 'లుంబినీవనం' ఏ దేశంలో కలదు?",
        "options": ["Bangladesh", "Myanmar", "Nepal (నేపాల్)", "Sri Lanka"],
        "answer": 3,
        "explanation": "Lumbini, the sacred birthplace of Gautama Buddha, is located in modern-day Nepal."
    }
]

# Merge into database
for q in more_telugu:
    if not any(x['id'] == q['id'] for x in db['Telugu']):
        db['Telugu'].append(q)

for q in more_maths:
    if not any(x['id'] == q['id'] for x in db['Maths']):
        db['Maths'].append(q)

for q in more_evs:
    if not any(x['id'] == q['id'] for x in db['EVS']):
        db['EVS'].append(q)

# Write updated databases
with open("data/telugu.json", "w", encoding="utf-8") as f:
    json.dump(db['Telugu'], f, ensure_ascii=False, indent=2)

with open("data/maths.json", "w", encoding="utf-8") as f:
    json.dump(db['Maths'], f, ensure_ascii=False, indent=2)

with open("data/evs.json", "w", encoding="utf-8") as f:
    json.dump(db['EVS'], f, ensure_ascii=False, indent=2)

with open("data/all_subjects.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Final Comprehensive Question Counts:")
for subj, qs in db.items():
    print(f"- {subj}: {len(qs)} MCQs")
print(f"Total: {sum(len(v) for v in db.values())} authentic MCQs loaded.")
