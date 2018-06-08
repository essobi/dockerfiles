FROM java:alpine  
  
MAINTAINER Guilherme Oliveira <gwoliveira@gmail.com>  
  
ENV SONAR_SCANNER_VERSION 3.1.0.1141  
RUN apk add --no-cache wget git && \  
wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-${SONAR_SCANNER_VERSION}.zip && \  
unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION} && \  
cd /usr/bin && ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-scanner
sonar-scanner && \  
apk del wget  
CMD sonar-scanner  

