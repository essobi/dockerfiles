FROM sonarqube:6.3.1-alpine  
  
ENV PLUGINS_DIR=/opt/sonarqube/extensions/plugins/  
RUN wget -P $PLUGINS_DIR --no-verbose
https://sonarsource.bintray.com/Distribution/sonar-javascript-plugin/sonar-
javascript-plugin-2.11.jar && \  
wget -P $PLUGINS_DIR https://sonarsource.bintray.com/Distribution/sonar-
generic-coverage/sonar-generic-coverage-plugin-1.2.jar && \  
wget -O /tmp/sonar-scanner.zip
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-
cli-3.0.3.778.zip && \  
unzip /tmp/sonar-scanner.zip -d /opt && rm -f /tmp/sonar-scanner.zip && ln -s
/opt/sonar-scanner-*/bin/sonar-scanner /bin/sonar-scanner

