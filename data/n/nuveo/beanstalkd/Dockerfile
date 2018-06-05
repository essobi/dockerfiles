FROM debian:stable  
  
RUN apt-get update && apt-get install -y git build-essential  
  
RUN git clone https://github.com/kr/beanstalkd && mkdir /data  
  
ENV BEANSTALKD_PORT 11300  
ENV BEANSTALKD_ADDR 0.0.0.0  
ENV BEANSTALKD_DIR /data  
ENV BEANSTALKD_MAX_JOB_SIZE 65535  
WORKDIR beanstalkd  
RUN make && make install  
  
EXPOSE $BEANSTALKD_PORT  
  
CMD beanstalkd -b $BEANSTALKD_DIR -l $BEANSTALKD_ADDR -p $BEANSTALKD_PORT -z
$BEANSTALKD_MAX_JOB_SIZE  

