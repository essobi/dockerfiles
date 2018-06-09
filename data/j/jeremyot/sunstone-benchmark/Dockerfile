FROM debian:wheezy  
MAINTAINER jeremyot@gmail.com  
  
RUN echo 'deb http://http.us.debian.org/debian wheezy main non-free' >>
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y netperf && apt-get -y clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
ADD run.sh /usr/bin/run.sh  
ENTRYPOINT ["/usr/bin/run.sh"]  

