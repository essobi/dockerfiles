FROM library/sonarqube:5.1.1  
MAINTAINER Anderson Nabas, "andersonnabas@gmail.com"  
RUN apt-get update && apt-get install -q -y wget && apt-get clean  
  
# download and install sonar plugins  
RUN rm /opt/sonarqube/lib/bundled-plugins/sonar-java-plugin-*.jar && \  
wget -P /opt/sonarqube/extensions/downloads/ \  
https://sonarsource.bintray.com/Distribution/sonar-java-plugin/sonar-java-
plugin-3.4.jar \  
http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-
build-breaker-plugin/1.1/sonar-build-breaker-plugin-1.1.jar \  
http://downloads.sonarsource.com/plugins/org/codehaus/sonar-
plugins/java/sonar-checkstyle-plugin/2.3/sonar-checkstyle-plugin-2.3.jar \  
http://downloads.sonarsource.com/plugins/org/codehaus/sonar-
plugins/java/sonar-pmd-plugin/2.4.1/sonar-pmd-plugin-2.4.1.jar  
  
WORKDIR /opt/sonarqube  
  
COPY entrypoint.sh entrypoint.sh  
COPY sonarRestoreRules.sh sonarRestoreRules.sh  
COPY rules.xml rules.xml  
  
ENTRYPOINT ["./entrypoint.sh"]  
  
CMD ["/opt/sonarqube/bin/run.sh"]  
  

