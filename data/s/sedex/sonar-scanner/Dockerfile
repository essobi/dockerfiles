FROM openjdk:8-jre-alpine  
MAINTAINER devops <devops@sedexglobal.com>  
  
ENV SONAR_SCANNER_VERSION cli-3.0.1.733-linux  
ENV SONAR_FOLDER 3.0.1.733-linux  
  
ADD "https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-${SONAR_SCANNER_VERSION}.zip" /  
RUN unzip "sonar-scanner-${SONAR_SCANNER_VERSION}.zip"  
RUN ls -ltr /  
RUN mv /sonar-scanner-${SONAR_FOLDER} /sonar  
  
RUN mkdir -p /data  
VOLUME /workspace  
WORKDIR /workspace  
  
RUN sed -i 's/use_embedded_jre=true/use_embedded_jre=false/g'
/sonar/bin/sonar-scanner  
ENV PATH "${PATH}:/sonar/bin"  
ENTRYPOINT ["sonar-scanner"]  
  
CMD ["--help"]  

