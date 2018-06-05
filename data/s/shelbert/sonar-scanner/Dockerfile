FROM openjdk:8-alpine  
  
LABEL maintainer="Sébastien HELBERT <sebastien.helbert@gmail.com>"  
  
RUN apk add --no-cache curl gzip  
  
WORKDIR /sonar-scanner  
  
ENV SONAR_SCANNER_VERSION 3.1.0.1141  
RUN curl -o sonarscanner.zip -L
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-
cli-${SONAR_SCANNER_VERSION}.zip && unzip sonarscanner.zip && rm
sonarscanner.zip  
  
ENV PATH $PATH:/sonar-scanner/sonar-scanner-${SONAR_SCANNER_VERSION}/bin  
  
VOLUME /root/.sonar  
  
COPY entrypoint.sh /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["entrypoint.sh"]  
  
WORKDIR /sonar-sources  
  
ENV SONAR_SCANNER_OPTS ""  
CMD ["sonar-scanner"]

