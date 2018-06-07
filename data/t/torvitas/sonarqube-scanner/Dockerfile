FROM openjdk:8-alpine  
LABEL maintainer="Sascha Marcel Schmidt <mail@saschaschmidt.net>"  
  
ENV SONAR_SCANNER_VERSION 3.1.0.1141  
ENV SONAR_SCANNER_HOME=/opt/sonar-scanner-${SONAR_SCANNER_VERSION}-linux  
ENV PATH $PATH:/opt/sonar-scanner-3.0.3.778-linux/bin  
  
RUN apk add --no-cache curl grep sed unzip  
  
WORKDIR /opt  
  
RUN curl -o ./sonarscanner.zip -L
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-
cli-${SONAR_SCANNER_VERSION}-linux.zip && unzip sonarscanner.zip && rm
sonarscanner.zip  
  
# ensure Sonar uses the provided Java for musl instead of a borked glibc one  
RUN sed -i 's/use_embedded_jre=true/use_embedded_jre=false/g' /opt/sonar-
scanner-${SONAR_SCANNER_VERSION}-linux/bin/sonar-scanner  
  
ENV PATH ${PATH}:/opt/sonar-scanner-${SONAR_SCANNER_VERSION}-linux/bin/  
  
ENTRYPOINT sonar-scanner -Dsonar.projectBaseDir=/src  

