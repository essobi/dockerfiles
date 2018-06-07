FROM sonarqube:6.7.1  
ENV PLUGINS_DIRECTORY=/opt/sonarqube/extensions/plugins/  
MAINTAINER Joost van der Griendt <joostvdg@gmail.com>  
LABEL authors="Joost van der Griendt <joostvdg@gmail.com>"  
LABEL description="Docker container for SonarQube For Docker Swarm"  
LABEL version="6.7.1-1"  
  
RUN wget -nc -P $PLUGINS_DIRECTORY https://github.com/uartois/sonar-
golang/releases/download/v1.2.11-rc13/sonar-golang-plugin-1.2.11-rc13.jar  
RUN wget -nc -P $PLUGINS_DIRECTORY https://github.com/vaulttec/sonar-auth-
oidc/releases/download/v1.0.3/sonar-auth-oidc-plugin-1.0.3.jar

