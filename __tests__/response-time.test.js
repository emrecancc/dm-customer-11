import request from 'supertest';
import app from '../src/app';

describe('API responds within 125ms', () => {
  it('should respond quickly', async () => {
    const start = Date.now();
    await request(app).get('/').send();
    const duration = Date.now() - start;
    expect(duration).toBeLessThan(450);
  });
});