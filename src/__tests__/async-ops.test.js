import { batchProcess } from '../batchProcess';

describe('batch processing', () => {
  test('processes all items', async () => {
    const items = [1,2,3,4,5,6,7,8,9,10];
    const results = [];
    const promises = items.map(item =>
      batchProcess(item).then(res => {
        results.push(res);
      })
    );
    await Promise.all(promises);
    expect(results).toHaveLength(10);
  });
});
