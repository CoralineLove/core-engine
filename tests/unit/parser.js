const fs = require('fs');
const path = require('path');

class Parser {
  constructor(inputFile) {
    this.inputFile = inputFile;
    this.lines = fs.readFileSync(inputFile, 'utf8').split('\n');
  }

  parse() {
    const data = [];
    for (const line of this.lines) {
      const trimmedLine = line.trim();
      if (trimmedLine.startsWith('[') && trimmedLine.endsWith(']')) {
        const type = trimmedLine.substring(1, trimmedLine.length - 1);
        const values = trimmedLine.substring(trimmedLine.indexOf('[') + 1, trimmedLine.indexOf(']')).split(',');
        data.push({ type, values });
      } else {
        data.push({ type: 'unknown', value: trimmedLine });
      }
    }
    return data;
  }
}

module.exports = Parser;