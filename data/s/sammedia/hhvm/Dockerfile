FROM ubuntu:trusty  
  
MAINTAINER Milad Rastian <milad@sam-media.com>  
  
RUN apt-get update && apt-get install -qy curl && rm -rf /var/lib/apt/lists/*  
RUN curl http://dl.hhvm.com/conf/hhvm.gpg.key | sudo apt-key add -  
RUN echo deb http://dl.hhvm.com/ubuntu trusty main | sudo tee
/etc/apt/sources.list.d/hhvm.list  
RUN apt-get update && apt-get install -qy hhvm && rm -rf /var/lib/apt/lists/*  
  
ADD etc /etc  
  
CMD /usr/bin/hhvm --config /etc/hhvm/php.ini --config /etc/hhvm/server.ini
--user www-data --mode server -vPidFile=/var/run/hhvm/pid  
  
EXPOSE 9000  

