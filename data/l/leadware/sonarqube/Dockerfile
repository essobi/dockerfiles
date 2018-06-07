# Leadware  
#  
# Sonarqube Quality Server Dockerfile  
# https://bitbucket.org/leadware/dockerfile-sonarqube  
# https://jetune@bitbucket.org/leadware/dockerfile-sonarqube.git  
# git@bitbucket.org:leadware/dockerfile-sonarqube.git  
#  
# Pull base image.  
FROM sonarqube:6.3  
# Maintainer  
MAINTAINER Jean-Jacques ETUNÈ NGI<jetune@leadware.net>  
  
# Sonar Java version  
ARG SONAR_JAVA_VERSION=4.8.0.9441  
# Sonar JS version  
ARG SONAR_JS_VERSION=2.21.0.4409  
# Sonar PHP version  
ARG SONAR_PHP_VERSION=2.10.0.2087  
# Sonar WEB version  
ARG SONAR_WEB_VERSION=2.5.0.476  
# Sonar XML version  
ARG SONAR_XML_VERSION=1.4.2.885  
# Sonar PYTHON version  
ARG SONAR_PYTHON_VERSION=1.7.0.1195  
# Sonar C# version  
ARG SONAR_CSHARP_VERSION=5.9.0.1001  
# Sonar Extension Directory  
ARG SONAR_PLUGINS_DIR=/opt/sonarqube/extensions/plugins  
  
# Root User  
USER root  
  
# Create Maven directories, download and untar maven.  
RUN \  
apt-get update -y && \  
mkdir -p $SONAR_PLUGINS_DIR && \  
wget -O $SONAR_PLUGINS_DIR/sonar-java-plugin-$SONAR_JAVA_VERSION.jar
https://sonarsource.bintray.com/Distribution/sonar-java-plugin/sonar-java-
plugin-$SONAR_JAVA_VERSION.jar && \  
wget -O $SONAR_PLUGINS_DIR/sonar-javascript-plugin-$SONAR_JS_VERSION.jar
https://sonarsource.bintray.com/Distribution/sonar-javascript-plugin/sonar-
javascript-plugin-$SONAR_JS_VERSION.jar && \  
wget -O $SONAR_PLUGINS_DIR/sonar-php-plugin-$SONAR_PHP_VERSION.jar
https://sonarsource.bintray.com/Distribution/sonar-php-plugin/sonar-php-
plugin-$SONAR_PHP_VERSION.jar && \  
wget -O $SONAR_PLUGINS_DIR/sonar-web-plugin-$SONAR_WEB_VERSION.jar
https://sonarsource.bintray.com/Distribution/sonar-web-plugin/sonar-web-
plugin-$SONAR_WEB_VERSION.jar && \  
wget -O $SONAR_PLUGINS_DIR/sonar-xml-plugin-$SONAR_XML_VERSION.jar
https://sonarsource.bintray.com/Distribution/sonar-xml-plugin/sonar-xml-
plugin-$SONAR_XML_VERSION.jar && \  
wget -O $SONAR_PLUGINS_DIR/sonar-python-plugin-$SONAR_PYTHON_VERSION.jar
https://sonarsource.bintray.com/Distribution/sonar-python-plugin/sonar-python-
plugin-$SONAR_PYTHON_VERSION.jar && \  
wget -O $SONAR_PLUGINS_DIR/sonar-csharp-plugin-$SONAR_CSHARP_VERSION.jar
https://sonarsource.bintray.com/Distribution/sonar-csharp-plugin/sonar-csharp-
plugin-$SONAR_CSHARP_VERSION.jar  
  
# Set ENV  
ENV SONAR_PLUGINS_DIR $SONAR_PLUGINS_DIR  
  
# Add Entry point script file  
ADD entrypoint.sh /leadware-sonarqube-entrypoint.sh  
  
# Set Workdir  
WORKDIR $SONARQUBE_HOME  
  
# Command  
CMD ["/leadware-sonarqube-entrypoint.sh"]

