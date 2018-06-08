FROM openjdk:8-jre-slim  
  
ENV SONAR_SCANNER_VERSION 3.1.0.1141  
ENV SONAR_OPTS ''  
RUN apt-get update && apt-get install -y wget  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip  
RUN apt-get remove -y wget && apt-get purge  
  
RUN unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux  
  
RUN ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}-linux/bin/sonar-scanner
/usr/bin/sonar-scanner  
RUN chmod +x /usr/bin/sonar-scanner  
  
VOLUME /project  
WORKDIR /project  
  
ADD run-sonar-scanner.sh /usr/bin/run-sonar-scanner  
CMD run-sonar-scanner  

