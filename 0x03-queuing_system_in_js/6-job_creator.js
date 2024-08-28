import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '0784895489',
  message: 'Hello Anthony'
};

const job = queue.createJob('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.log('Error creating job');
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
