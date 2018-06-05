FROM debian:jessie  
  
ENV BEANSTALK_VERSION="1.10"  
RUN apt-get update && apt-get install -y curl build-essential  
  
RUN curl -sL
https://github.com/kr/beanstalkd/archive/v$BEANSTALK_VERSION.tar.gz | tar xvz
-C /tmp  
  
WORKDIR /tmp/beanstalkd-$BEANSTALK_VERSION  
RUN make  
RUN cp beanstalkd /usr/local/bin  
  
WORKDIR /  
RUN apt-get remove --purge -y curl build-essential && apt-get autoclean &&
apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 11300  
CMD ["beanstalkd", "-p", "11300"]  

