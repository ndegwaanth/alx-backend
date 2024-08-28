import kue from 'kue';

const blacklisted = [4153518780, 4153518781];

function sendNotification (phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklisted.includes(phoneNumber)) {
    return (new Error(`phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  done();
}

const queue = kue.createQueue();

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
