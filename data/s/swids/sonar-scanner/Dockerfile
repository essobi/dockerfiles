FROM openjdk:8-jdk-alpine  
  
ENV SONAR_SCANNER_VERSION 2.8  
  
RUN apk add --no-cache wget && \  
mkdir -p -m 777 /sonar-scanner && \  
wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-$SONAR_SCANNER_VERSION.zip -O /sonar-scanner/sonar-scanner.zip && \  
cd /sonar-scanner && \  
unzip -q sonar-scanner.zip && \  
rm sonar-scanner.zip  
  
ENV SONAR_SCANNER_HOME=/sonar-scanner/sonar-scanner-$SONAR_SCANNER_VERSION  
ENV PATH $PATH:/sonar-scanner/sonar-scanner-$SONAR_SCANNER_VERSION/bin  
  
ENTRYPOINT [ "sonar-scanner" ]  

