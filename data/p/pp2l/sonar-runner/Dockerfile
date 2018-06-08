FROM java:openjdk-8u45-jdk  
  
ENV SONAR_SCANNER_HOME /opt/sonar-scanner  
  
ENV SONAR_SCANNER_VERSION 2.5  
ENV SONAR_LANGUAGE java  
  
RUN set -x \  
&& cd /opt \  
&& curl -o sonar-scanner.zip -fSL
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-$SONAR_SCANNER_VERSION.zip \  
&& curl -o sonar-scanner.zip.asc -fSL
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-$SONAR_SCANNER_VERSION.zip.asc \  
&& unzip sonar-scanner.zip \  
&& mv sonar-scanner-$SONAR_SCANNER_VERSION sonar-scanner \  
&& rm sonar-scanner.zip*  
  
RUN mkdir -p /opt/src  
VOLUME /opt/src  
  
ADD bin/sonar-entry /usr/bin/sonar-entry  
  
WORKDIR /opt/src  
  
CMD ["/usr/bin/sonar-entry"]  

