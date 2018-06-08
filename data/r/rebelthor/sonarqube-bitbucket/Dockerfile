# SonarQube Server  
#  
# VERSION 0.0.1  
  
FROM sonarqube:alpine  
  
RUN apk add --update curl && \  
rm -rf /var/cache/apk/*  
  
WORKDIR $SONARQUBE_HOME/extensions/plugins  
  
RUN set -x \  
&& curl -fSL -o sonar-bitbucket-plugin.jar
https://github.com/mibexsoftware/sonar-bitbucket-
plugin/releases/download/v1.2.1/sonar-bitbucket-plugin-1.2.1.jar \  
&& curl -fSL -o sonar-build-breaker-plugin.jar
https://github.com/SonarQubeCommunity/sonar-build-
breaker/releases/download/2.2/sonar-build-breaker-plugin-2.2.jar \  
&& curl -fSL -o sonar-auth-bitbucket-plugin.jar
https://github.com/SonarQubeCommunity/sonar-auth-
bitbucket/releases/download/1.0/sonar-auth-bitbucket-plugin-1.0.jar  
  
WORKDIR $SONARQUBE_HOME

