FROM dockerfile/java:oracle-java8  
MAINTAINER Stephane Gamard <stephane@gamard.net>  
  
ENV SONARQUBE_VERSION 5.1  
RUN wget -O sonarqube.zip -q
http://dist.sonar.codehaus.org/sonarqube-${SONARQUBE_VERSION}.zip  
RUN unzip sonarqube*.zip  
RUN rm sonarqube*.zip  
RUN mv sonarqube* /usr/local/sonarqube/  
  
ENV SONAR_HOME /usr/local/sonarqube  
ADD ./config/sonar.properties ${SONAR_HOME}/conf/sonar.properties  
RUN ln -sf /dev/stdout ${SONAR_HOME}/logs/sonar.log  
  
EXPOSE 9000  
EXPOSE 9092  
CMD java -jar ${SONAR_HOME}/lib/sonar-application*.jar

