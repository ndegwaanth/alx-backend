import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

async function createHolbertonSchoolHash () {
  client.hset('HolbertonSchools', 'Portland', '50', print);
  client.hset('HolbertonSchools', 'Seatttle', '80', print);
  client.hset('HolbertonSchools', 'New York', '20', print);
  client.hset('HolbertonSchools', 'Bogota', '20', print);
  client.hset('HolbertonSchools', 'Cali', '40', print);
  client.hset('HolbertonSchools', 'Paris', '2', print);
}

function displayHolbertonSchoolHash () {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.error(`Error retriving Hash: ${err.message}`);
    } else {
      console.log(reply);
    }
  });
}

createHolbertonSchoolHash();
displayHolbertonSchoolHash();
