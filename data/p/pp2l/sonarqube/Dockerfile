FROM sonarqube:latest  
  
RUN mkdir -p /var/sonarqube/plugins  
RUN curl -L -o "/var/sonarqube/plugins/sonar-javascript-plugin-2.10.jar"
'https://sonarsource.bintray.com/Distribution/sonar-javascript-plugin/sonar-
javascript-plugin-2.10.jar'  
RUN curl -L -o "/var/sonarqube/plugins/sonar-csharp-plugin-4.5.jar"
'https://sonarsource.bintray.com/Distribution/sonar-csharp-plugin/sonar-
csharp-plugin-4.5.jar'  
COPY start.sh ${SONARQUBE_HOME}/bin/start.sh  
  
ENTRYPOINT ["./bin/start.sh"]  
  

