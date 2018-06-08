FROM openjdk:8-jre  
  
ENV SONAR_SCANNER_VERSION 3.0.0.702  
ENV SONAR_SCANNER_HOME /opt/sonar-scanner-${SONAR_SCANNER_VERSION}-linux  
  
WORKDIR /opt  
  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip \  
&& unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip \  
&& rm sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip  
RUN chmod +x ${SONAR_SCANNER_HOME}/bin/* && ln -s
${SONAR_SCANNER_HOME}/bin/sonar-scanner /usr/bin/sonar-scanner  

