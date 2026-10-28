// node tests/signup-typo.test.js : unit tests for the email typo hint in signup.js
const { ukslrSuggest: s } = require('../signup.js');
const cases = { 'jo@gmial.com': 'jo@gmail.com', 'jo@hotmial.co.uk': 'jo@hotmail.co.uk', 'jo@x.con': 'jo@x.com', 'jo@gmail.con': 'jo@gmail.com',
  'jo@yahoo.co.u': 'jo@yahoo.co.uk', 'jo@outlok.com': 'jo@outlook.com', 'jo@icloud.cm': 'jo@icloud.com', 'jo@btinternet.om': 'jo@btinternet.com',
  'jo@gmailcom': 'jo@gmail.com', 'jo@googlemial.com': 'jo@googlemail.com', 'jo@gmaill.com': 'jo@gmail.com', 'jo@virginmedia.co': 'jo@virginmedia.com',
  'Jo.Smith@GMIAL.COM': 'Jo.Smith@gmail.com', 'jo@smithlettings.co.uk': null, 'jo@ukshortletrules.co.uk': null, 'jo@gmail.com': null,
  'jo@hotmail.co.uk': null, 'jo@gmx.com': null, 'jo@mail.com': null, 'jo@ymail.com': null, 'jo@live.com': null, 'jo@hotmail.fr': null,
  'jo@outlook.co.uk': null, 'jo@mac.com': null, 'jo@nhs.net': null, 'jo@talktalk.net': null, 'jo@ntlworld.com': null, 'jo@btopenworld.com': null,
  'jo@me.org': null, 'jo@aol.co.uk': null, 'jo@company.com': null, 'jo@yahoo.ie': null, 'jo': null, 'jo@': null };
let f = 0; for (const [k, v] of Object.entries(cases)) { const r = s(k); if (r !== v) { f++; console.log('FAIL', k, r, 'expected', v); } }
console.log(`${Object.keys(cases).length} cases, ${f} failures`); process.exit(f ? 1 : 0);
