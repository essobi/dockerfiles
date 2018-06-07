FROM dockerfile/java:oracle-java8  
  
MAINTAINER Dawanda  
  
ENV SBT_VERSION 0.13.7  
RUN wget http://dl.bintray.com/sbt/debian/sbt-${SBT_VERSION}.deb -O
/tmp/sbt.deb && \  
dpkg -i /tmp/sbt.deb && \  
rm -f /tmp/sbt.deb  
RUN sbt  

