FROM sonarqube:alpine  
  
# Fix name finding bug http://stackoverflow.com/a/39244439  
RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >
/etc/nsswitch.conf  
  
# Git from https://docs.sonarqube.org/display/PLUG/Git+Plugin  
ARG SONARGIT_VERSION=1.2  
ADD https://sonarsource.bintray.com/Distribution/sonar-scm-git-plugin/sonar-
scm-git-plugin-${SONARGIT_VERSION}.jar /opt/sonarqube/extensions/plugins/  
  
# Angular from https://github.com/Pablissimo/SonarTsPlugin/releases  
ARG SONARTS_VERSION=1.1.0  
ADD
https://github.com/Pablissimo/SonarTsPlugin/releases/download/v${SONARTS_VERSION}/sonar-
typescript-plugin-${SONARTS_VERSION}.jar /opt/sonarqube/extensions/plugins/  
  
# Java from https://docs.sonarqube.org/display/PLUG/SonarJava  
ARG SONARJAVA_VERSION=4.7.1.9272  
ADD https://sonarsource.bintray.com/Distribution/sonar-java-plugin/sonar-java-
plugin-${SONARJAVA_VERSION}.jar /opt/sonarqube/extensions/plugins/  
  
# Findbugs from https://github.com/SonarQubeCommunity/sonar-findbugs/releases  
ARG SONARFINDBUGS_VERSION=3.4.4  
ADD https://github.com/SonarQubeCommunity/sonar-
findbugs/releases/download/3.4.4/sonar-findbugs-
plugin-${SONARFINDBUGS_VERSION}.jar /opt/sonarqube/extensions/plugins/  
  
# Checkstyle from https://github.com/checkstyle/sonar-checkstyle/releases  
ARG SONARCHECKSTYLE_VERSION=3.6  
ADD https://github.com/checkstyle/sonar-
checkstyle/releases/download/3.6/checkstyle-sonar-
plugin-${SONARCHECKSTYLE_VERSION}.jar /opt/sonarqube/extensions/plugins/  

