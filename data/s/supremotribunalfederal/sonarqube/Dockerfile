FROM sonarqube:4.5.7  
MAINTAINER Tomás Godoi  
  
RUN wget http://central.maven.org/maven2/org/sonarsource/java/sonar-java-
plugin/3.14/sonar-java-plugin-3.14.jar -P /opt/download  
RUN wget https://oss.sonatype.org/content/groups/public/fr/sii/sonar/sonar-
web-frontend-plugin/2.1.0/sonar-web-frontend-plugin-2.1.0.jar -P /opt/download  
  
COPY install-plugins-and-run.sh /  
  
ENTRYPOINT ["/install-plugins-and-run.sh"]

