# Redis vs Beanstalkd 
  
* Set up 3 containers - beanstalkd and redis (rdb and aof)
* Write 2 simple scripts: 1st should put message into queue, 2nd should read from queue.
* Configure storing to disk, and compare queues performance.


|           | beanstalkd | redis rdb | redis aof |
|-----------|------------|-----------|-----------|
| Time, sec | 341        | 329       | 352       |
