FROM openjdk:8-jre-alpine  
ENV SONAR_SCANNER_VERSION 3.0.3.778  
ADD "https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-$SONAR_SCANNER_VERSION.zip" /  
RUN unzip "sonar-scanner-cli-$SONAR_SCANNER_VERSION.zip"  
RUN mkdir -p /data  
VOLUME /data  
WORKDIR /data  
ENV PATH "/sonar-scanner-$SONAR_SCANNER_VERSION/bin:$PATH"  
ENTRYPOINT ["sonar-scanner"]  
CMD ["--help"]  

