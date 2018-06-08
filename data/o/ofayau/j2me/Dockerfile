FROM ofayau/busybox-jvm  
  
MAINTAINER Olivier Fayau  
  
# Unzip Oracle Java Micro Edition Embedded Client 1.1.1  
# Official depo (need login) :
http://www.oracle.com/technetwork/java/embedded/javame/embedded-
client/downloads/index.html  
  
ADD ojec1.1.1/ /usr/lib/jvm/ojec1.1.1/  
RUN ln -s /usr/lib/jvm/ojec1.1.1 /usr/lib/jvm/jre  
  
CMD ["cvm", "-version"]  
  

