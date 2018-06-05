FROM sonarqube:6.0-alpine  
  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates  
RUN mkdir -p /opt/sonarqube/bootstrap && touch
/opt/sonarqube/bootstrap/bootstrapped  
  
RUN mkdir -p /opt/sonarqube/bootstrap/extensions/plugins/ \  
&& wget -O /opt/sonarqube/bootstrap/extensions/plugins/sonar-groovy-
plugin-1.4.jar https://sonarsource.bintray.com/Distribution/sonar-groovy-
plugin/sonar-groovy-plugin-1.4.jar \  
&& wget -O /opt/sonarqube/bootstrap/extensions/plugins/sonar-ldap-
plugin-2.0.jar https://sonarsource.bintray.com/Distribution/sonar-ldap-
plugin/sonar-ldap-plugin-2.0.jar \  
&& wget -O /opt/sonarqube/bootstrap/extensions/plugins/sonar-python-
plugin-1.6.jar https://sonarsource.bintray.com/Distribution/sonar-python-
plugin/sonar-python-plugin-1.6.jar \  
&& wget -O /opt/sonarqube/bootstrap/extensions/plugins/sonar-timeline-
plugin-1.5.jar http://downloads.sonarsource.com/plugins/org/codehaus/sonar-
plugins/sonar-timeline-plugin/1.5/sonar-timeline-plugin-1.5.jar \  
&& wget -O /opt/sonarqube/bootstrap/extensions/plugins/sonar-web-
plugin-2.4.jar https://sonarsource.bintray.com/Distribution/sonar-web-
plugin/sonar-web-plugin-2.4.jar \  
&& wget -O /opt/sonarqube/bootstrap/extensions/plugins/sonar-xml-
plugin-1.4.1.jar https://sonarsource.bintray.com/Distribution/sonar-xml-
plugin/sonar-xml-plugin-1.4.1.jar \  
&& wget -O /opt/sonarqube/bootstrap/extensions/plugins/sonar-widget-lab-
plugin-1.8.1.jar https://sonarsource.bintray.com/Distribution/sonar-widget-
lab-plugin/sonar-widget-lab-plugin-1.8.1.jar \  
&& wget -O /opt/sonarqube/bootstrap/extensions/plugins/sonar-javascript-
plugin-2.14.jar https://sonarsource.bintray.com/Distribution/sonar-javascript-
plugin/sonar-javascript-plugin-2.14.jar \  
&& wget -O /opt/sonarqube/bootstrap/extensions/plugins/sonar-css-plugin.jar
https://github.com/SonarQubeCommunity/sonar-css/releases/download/2.0/sonar-
css-plugin.jar  
  
  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

