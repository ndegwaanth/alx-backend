import { createClient } from 'redis';

const subscriber = createClient();

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
  console.log(`Received message is:${message}`);

  if (message === 'KILL SERVER') {
    subscriber.unsubscribe('holberton school channel');
    subscriber.quit();
  }
});
