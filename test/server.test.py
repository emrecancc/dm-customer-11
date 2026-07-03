const http = require('http');
const request = require('supertest');

const server = http.createServer((req, res) => {
  res.end('ok');
});
server.listen(3119);

describe('Server', () => {
  it('responds to GET /', async () => {
    const res = await request(server).get('/');
    expect(res.status).toBe(200);
  });
});

afterAll(() => server.close());