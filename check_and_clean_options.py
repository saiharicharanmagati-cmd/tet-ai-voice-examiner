# -*- coding: utf-8 -*-
import json
import re

with open("data/all_subjects.json", "r", encoding="utf-8") as f:
    db = json.load(f)

cleaned_count = 0

for subj in ['English', 'Telugu', 'EVS', 'Maths', 'CDP']:
    for q in db[subj]:
        opts = q.get('options', [])
        new_opts = []
        for i, opt in enumerate(opts):
            s = str(opt).strip()
            # Remove leading (1), 1), 1., (A), A), A. etc.
            s = re.sub(r'^\s*[\(\[]?[1-4A-Da-d][\)\.\:]\s*', '', s)
            # Remove trailing numbers like '2.' or '3' at the end of the last option
            s = re.sub(r'\s+[1-9]\d*[\.\)]*$', '', s)
            s = s.strip()
            if s != opt:
                cleaned_count += 1
            new_opts.append(s)
        q['options'] = new_opts

print(f"Cleaned {cleaned_count} options across all subjects!")

# Also check for empty options or length != 4
for subj in ['English', 'Telugu', 'EVS', 'Maths', 'CDP']:
    for q in db[subj]:
        assert len(q['options']) == 4, f"{subj} Q{q['id']} doesn't have 4 options"
        for i, o in enumerate(q['options']):
            assert len(o) > 0, f"{subj} Q{q['id']} option {i+1} is empty!"
        assert q['answer'] in [1, 2, 3, 4], f"{subj} Q{q['id']} invalid answer {q['answer']}"

# Save back cleaned data
for subj in ['English', 'Telugu', 'EVS', 'Maths', 'CDP']:
    with open(f"data/{subj.lower()}.json", "w", encoding="utf-8") as f:
        json.dump(db[subj], f, ensure_ascii=False, indent=2)

with open("data/all_subjects.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Saved cleaned data successfully!")
