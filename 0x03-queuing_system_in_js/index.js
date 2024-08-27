const Redis = require('ioredis');

const r = new Redis();

async function performance (err) {
  try {
    await r.hmset('information', {
      name: 'anthony',
      age: 24,
      course: 'Bsit'
    });
    if (err) {
      console.error(err);
    } else {
      const values = await r.hgetall('information');
      console.log('Elements', values);
    }
  } catch (err) {
    console.error(err);
  } finally {
    r.quit();
  }
}

performance();
