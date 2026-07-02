const fs = require('fs');
const path = require('path');

const src = path.join(__dirname, 'server.js');
const dest = path.join(__dirname, 'server.js.bak');

if (!fs.existsSync(src)) {
  console.error('Source file server.js does not exist.');
  process.exit(1);
}

const data = fs.readFileSync(src);
fs.writeFileSync(dest, data);
console.log(`Created backup: ${dest}`);
