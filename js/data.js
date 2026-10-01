// Question Data Loader and Repository
export class QuestionRepo {
  constructor() {
    this.subjects = ['English', 'Telugu', 'EVS', 'Maths', 'CDP'];
    this.data = {
      English: [],
      Telugu: [],
      EVS: [],
      Maths: [],
      CDP: []
    };
    this.isLoaded = false;
  }

  async loadAll() {
    try {
      const response = await fetch('./data/all_subjects.json');
      if (response.ok) {
        this.data = await response.json();
        this.isLoaded = true;
        return this.data;
      }
    } catch (e) {
      console.warn("Could not load combined JSON, trying individual subject files...", e);
    }

    // Try individual files
    for (const sub of this.subjects) {
      try {
        const res = await fetch(`./data/${sub.toLowerCase()}.json`);
        if (res.ok) {
          this.data[sub] = await res.json();
        }
      } catch (err) {
        console.error(`Error loading subject ${sub}:`, err);
      }
    }
    this.isLoaded = true;
    return this.data;
  }

  getBySubject(subject) {
    return this.data[subject] || [];
  }

  getTopics(subject) {
    const list = this.getBySubject(subject);
    const topics = new Set(list.map(q => q.topic).filter(Boolean));
    return Array.from(topics);
  }

  getQuestionById(subject, id) {
    const list = this.getBySubject(subject);
    return list.find(q => q.id === id);
  }

  getRandomSample(subject, count = 30) {
    const list = [...this.getBySubject(subject)];
    for (let i = list.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [list[i], list[j]] = [list[j], list[i]];
    }
    return list.slice(0, count);
  }
}

export const questionRepo = new QuestionRepo();
