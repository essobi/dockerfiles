FROM openjdk:8-jre-alpine  
  
ARG SONAR_SCANNER_VERSION  
ENV SONAR_SCANNER_VERSION=${SONAR_SCANNER_VERSION:-3.0.1.733}  
  
ADD "https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-${SONAR_SCANNER_VERSION}.zip" /  
  
RUN unzip "sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip" \  
&& rm /sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \  
&& mkdir -p /app  
  
ENV PATH "/sonar-scanner-${SONAR_SCANNER_VERSION}/bin:${PATH}"  
WORKDIR /app  
  
ENTRYPOINT ["sonar-scanner"]  
  
CMD ["--help"]

