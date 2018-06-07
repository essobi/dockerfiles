FROM sonarqube:7.0  
MAINTAINER dolphintwo  
  
RUN wget
https://github.com/SonarQubeCommunity/sonar-l10n-zh/releases/download/sonar-l10n-zh-
plugin-1.20-RC1/sonar-l10n-zh-plugin-1.20-RC1.jar -P
/opt/sonarqube/extensions/plugins/  
RUN chown sonarqube:sonarqube /opt/sonarqube/extensions/plugins/sonar-l10n-zh-
plugin-1.20-RC1.jar  
RUN ls -al /opt/sonarqube/extensions/plugins/  

