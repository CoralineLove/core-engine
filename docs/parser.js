import { console } from 'console';

class Parser {
  constructor(file) {
    this.file = file;
    this.data = [];
    this.index = 0;
  }

  next() {
    if (this.index >= this.data.length) {
      return null;
    }
    return this.data[this.index++];
  }

  skipWhitespace() {
    while (this.index < this.data.length && this.data[this.index].trim() === '') {
      this.index++;
    }
  }

  parse() {
    const data = this.file.toString();
    const lines = data.split('\n');
    this.data = lines.map(line => line.trim());
    this.index = 0;
    return this.data;
  }
}

export default Parser;