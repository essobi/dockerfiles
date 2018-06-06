  
FROM dockerfile/java:oracle-java7  
RUN apt-get update  
RUN apt-get upgrade -y  
MAINTAINER Mark Smithson mark@carsnip.com  
ENV REFRESHED_AT 2014-10-13  
RUN mkdir /opt/heritrix  
RUN wget -O /tmp/heritrix.tar.gz
http://builds.archive.org/maven2/org/archive/heritrix/heritrix/3.2.0/heritrix-3.2.0-dist.tar.gz  
RUN tar -C /opt -xvf /tmp/heritrix.tar.gz  
  
ADD heritrix-start.sh /usr/local/bin/heritrix-start.sh  
  
EXPOSE 8443  
CMD /usr/local/bin/heritrix-start.sh  

