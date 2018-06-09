FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
wget \  
zip \  
openjdk-7-jdk  
  
ENV SQ_VERSION 5.1  
ENV SQ_HOME /usr/local/sonarqube-$SQ_VERSION  
  
#download,unzip  
RUN wget -O /tmp/SQ.zip
http://dist.sonar.codehaus.org/sonarqube-$SQ_VERSION.zip \  
&& unzip -o /tmp/SQ.zip -d /usr/local/ \  
&& rm /tmp/SQ.zip  
  
#copy properties  
COPY ./sonar.properties $SQ_HOME/conf/  
  
VOLUME $SQ_HOME/extensions  
  
#port  
EXPOSE 9000  
CMD ["/usr/local/sonarqube-5.1/bin/linux-x86-64/sonar.sh","console"]  

