FROM debian:jessie  
  
MAINTAINER Melon Li <melon198502@gmail.com>  
  
ENV VERSION "1.10"  
RUN set -xe && \  
apt-get update && apt-get install -y curl build-essential \  
&& curl -sL https://github.com/kr/beanstalkd/archive/v$VERSION.tar.gz | tar
-zx -C /tmp \  
&& cd /tmp/beanstalkd-$VERSION && make && cp beanstalkd /usr/local/bin \  
&& apt-get remove --purge -y curl build-essential && apt-get autoclean && apt-
get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/beanstalkd-$VERSION  
  
EXPOSE 11300  
CMD ["beanstalkd", "-p", "11300"]  

