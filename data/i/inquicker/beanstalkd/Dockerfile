FROM debian:jessie  
  
ENV BEANSTALKD_VERSION=1.10  
CMD ["-p", "11300"]  
EXPOSE 11300  
ENTRYPOINT ["/usr/bin/beanstalkd"]  
  
RUN apt-get update && \  
apt-get install -y curl build-essential && \  
curl -sL https://github.com/kr/beanstalkd/archive/v$BEANSTALKD_VERSION.tar.gz
| tar xvz -C /tmp && \  
cd /tmp/beanstalkd-$BEANSTALKD_VERSION && \  
make && \  
cp beanstalkd /usr/bin/ && \  
apt-get remove --purge -y curl build-essential && apt-get autoclean && apt-get
clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

