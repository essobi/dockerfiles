FROM openjdk:8  
MAINTAINER "Francois Fernandes <f.fernandes@fernandes-it.de>"  
ADD http://ftp-stud.hs-
esslingen.de/pub/Mirrors/ftp.apache.org/dist/qpid/java/6.0.4/binaries/qpid-
broker-6.0.4-bin.tar.gz /opt  
  
WORKDIR /opt  
RUN tar zxf qpid-broker-6.0.4-bin.tar.gz && rm qpid-broker-6.0.4-bin.tar.gz  
  
CMD /opt/qpid-broker/6.0.4/bin/qpid-server  

