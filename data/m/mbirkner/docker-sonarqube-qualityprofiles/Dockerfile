FROM sonarqube:6.3  
ENV SONAR_DOWNLOAD_URL https://sonarsource.bintray.com/Distribution  
  
# Installing Plugins  
RUN cd /opt/sonarqube/extensions/plugins/  
RUN curl -o sonar-java-plugin.jar -fSL $SONAR_DOWNLOAD_URL/sonar-java-
plugin/sonar-java-plugin-4.8.0.9441.jar  
RUN curl -o sonar-web-plugin.jar -fSL $SONAR_DOWNLOAD_URL/sonar-web-
plugin/sonar-web-plugin-2.5.0.476.jar  
RUN curl -o sonar-scm-git-plugin.jar -fSL $SONAR_DOWNLOAD_URL/sonar-scm-git-
plugin/sonar-scm-git-plugin-1.2.jar  
RUN curl -o sonar-csharp-plugin.jar -fSL $SONAR_DOWNLOAD_URL/sonar-csharp-
plugin/sonar-csharp-plugin-5.8.0.660.jar  
RUN curl -o sonar-javascript-plugin.jar -fSL $SONAR_DOWNLOAD_URL/sonar-
javascript-plugin/sonar-javascript-plugin-2.21.1.4786.jar  
RUN curl -o sonar-php-plugin.jar -fSL $SONAR_DOWNLOAD_URL/sonar-php-
plugin/sonar-php-plugin-2.10.0.2087.jar  
RUN curl -o sonar-checkstyle-plugin.jar -fSL $SONAR_DOWNLOAD_URL/sonar-
checkstyle-plugin/sonar-checkstyle-plugin-2.4.jar  
  
# Add Scala Plugin - https://github.com/ncredinburgh/sonar-scalastyle  
ADD plugins/sonar-scalastyle-0.0.3-SNAPSHOT.jar
/opt/sonarqube/extensions/plugins/  
  
# Add Kotlin Plugin - https://github.com/K0zka/kotlin-sonar  
ADD plugins/kotlin-sonar-0.1-SNAPSHOT.jar /opt/sonarqube/extensions/plugins/  
  
# Add default Java Quality Profile  
ADD qualityprofile/java-standardprofile.xml /qualityprofile/  
  
VOLUME ["$SONARQUBE_HOME/data", "$SONARQUBE_HOME/extensions",
"/qualityprofile"]  
  
ADD start_with_profile.sh /opt/sonarqube/start_with_profile.sh  
  
ENTRYPOINT ["/opt/sonarqube/start_with_profile.sh"]  

