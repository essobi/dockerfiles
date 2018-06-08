FROM openjdk:8-jdk  
MAINTAINER Christian Meter <meter@cs.uni-duesseldorf.de>  
  
ENV SONAR_VERSION 3.0.3.778  
ENV SONAR_ARCHIVE sonar-scanner-cli-$SONAR_VERSION-linux.zip  
  
WORKDIR /root  
  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/$SONAR_ARCHIVE && \  
unzip $SONAR_ARCHIVE && \  
rm $SONAR_ARCHIVE  
  
ENV PATH $PATH:/root/sonar-scanner-$SONAR_VERSION-linux/bin  
  
CMD sonar-scanner  
  

