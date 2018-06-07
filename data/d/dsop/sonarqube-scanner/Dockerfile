FROM openjdk:8-alpine  
  
ARG SONAR_SCANNER_VERS=3.0.3.778  
RUN apk --no-cache update && \  
apk add openssl  
  
RUN wget -q
https://dl.bintray.com/sonarsource/SonarQube/org/sonarsource/scanner/cli/sonar-
scanner-cli/$SONAR_SCANNER_VERS/sonar-scanner-cli-$SONAR_SCANNER_VERS.zip -O
/tmp/sonar-scanner.zip  
  
RUN unzip /tmp/sonar-scanner.zip -d /tmp && \  
mv /tmp/sonar-scanner-$SONAR_SCANNER_VERS /var/opt/sonar-scanner  
  
WORKDIR /var/opt/sonar-scanner  
  
ENV SONAR_RUNNER_HOME=/var/opt/sonar-scanner  
ENV PATH $PATH:/var/opt/sonar-scanner/bin  
  
ADD entrypoint.sh /var/opt/sonar-scanner  
  
ENTRYPOINT [ "/var/opt/sonar-scanner/entrypoint.sh" ]  

