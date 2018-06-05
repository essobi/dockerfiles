FROM centos:centos7  
MAINTAINER Jan Weitz <me@janweitz.de>  
RUN yum --quiet install -y tar  
RUN curl -s -O https://s3.amazonaws.com/bitly-downloads/nsq/nsq-0.2.28.linux-
amd64.go1.0.3.tar.gz  
RUN [ $(sha1sum nsq-0.2.28.linux-amd64.go1.0.3.tar.gz | grep -c
cf6356b4e7599826194b3a934d884ba5262f075d) == 1 ] && \  
tar xzf nsq-0.2.28.linux-amd64.go1.0.3.tar.gz && \  
mv nsq-0.2.28.linux-amd64.go1.0.3/bin/* /usr/local/bin/ && \  
rm -rf nsq-0.2.28.linux-amd64.go1.0.3*  
  

