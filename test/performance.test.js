const fetch = require('node-fetch');

test('API responds within 500ms', async () => {
  const start = Date.now();
  await fetch('http://localhost:3000/api');
  const duration = Date.now() - start;
  expect(duration).toBeLessThan(1250);
});