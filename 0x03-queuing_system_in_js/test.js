const Redis = require('redis');
const Express = require('express');

const app = new Express();
const client = Redis;
const port = 3000;

app.use(Express.json());

app.get('/', (req, res, err) => {
  try {
    client.hmset('information', {
      name: 'Anthony',
      age: 34,
      course: 'BSIT'
    });

    if (err) {
      return res.status(500).send('Error connecting with Redis');
    } else {
      return res.send(client.hgetall('information'));
    }
  } catch (err) {
    return res.status(500);
  } finally {
    client.quit;
  }
});

app.listen(port, () => {
  console.log(`The application is listening to paort ${port}`);
});
