FROM openjdk:8  
ENV SONAR_SCANNER_VERSION 2.8  
ENV SONAR_SCANNER_HOME /sonar-scanner-${SONAR_SCANNER_VERSION}  
ENV SONAR_SCANNER_DIST sonar-scanner-${SONAR_SCANNER_VERSION}.zip  
ENV SONAR_SCANNER_DIST_URL https://sonarsource.bintray.com/Distribution/sonar-
scanner-cli/${SONAR_SCANNER_DIST}  
  
RUN useradd -ms /bin/bash sonar  
  
RUN wget ${SONAR_SCANNER_DIST_URL} && unzip ${SONAR_SCANNER_DIST} && rm
${SONAR_SCANNER_DIST}  
  
VOLUME /work  
  
WORKDIR /work  
  
ENV PATH "$SONAR_SCANNER_HOME/bin:$PATH"  
USER sonar  
  
CMD ["sonar-scanner"]  

