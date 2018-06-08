FROM openjdk:8  
LABEL maintainer="pctao.tw@gmail.com"  
  
RUN mkdir -p /opt \  
&& curl -o /tmp/sonarscanner.zip -L
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-
cli-3.0.3.778-linux.zip \  
&& cd /opt && unzip /tmp/sonarscanner.zip \  
&& rm /tmp/sonarscanner.zip  
  
ENV SONAR_RUNNER_HOME=/opt/sonar-scanner-3.0.3.778-linux  
ENV PATH $PATH:/opt/sonar-scanner-3.0.3.778-linux/bin  
  
WORKDIR /opt/src  
  
CMD sonar-scanner -Dsonar.projectBaseDir=/opt/src  
  

