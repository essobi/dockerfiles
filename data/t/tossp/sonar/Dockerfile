FROM java:alpine  
ENV SONAR_SCANNER_VERSION 3.1.0.1141  
  
RUN apk add --no-cache wget && \  
wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-${SONAR_SCANNER_VERSION}.zip && \  
unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION} && \  
cd /usr/bin && ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-scanner
sonar-scanner  
  
RUN apk add --no-cache nodejs git && \  
npm i -g npm  
  
COPY files/sonar-scanner-run.sh /usr/bin  
  
RUN chmod 755 /usr/bin/sonar-scanner-run.sh

