const nock = require('nock');
const { getUser } = require('../src/api');

describe('API client', () => {
  afterEach(() => nock.cleanAll());

  test('fetches user successfully', async () => {
    nock('https://api.example.com')
      .get('/users/1')
      .reply(200, { id: 1, name: 'Alice' });

    const user = await getUser(1);
    expect(user).toEqual({ id: 1, name: 'Alice' });
  });

  test('handles 404', async () => {
    nock('https://api.example.com')
      .get('/users/999')
      .reply(404);

    const user = await getUser(999);
    expect(user).toBeNull();
  });
});