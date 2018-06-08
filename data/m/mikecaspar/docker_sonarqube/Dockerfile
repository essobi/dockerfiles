# Creates a docker container with SonarQube, incl. several plugins to start a
consistent set of rules in place  
# The MIT License (MIT)  
# Copyright (c) 2016 Caspar Computer Services Inc.  
# Permission is hereby granted, free of charge, to any person obtaining a copy
of this software  
# and associated documentation files (the "Software"), to deal in the Software
without restriction,  
# including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense,  
# and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so,  
# subject to the following conditions:  
# The above copyright notice and this permission notice shall be included in
all  
# copies or substantial portions of the Software.  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT  
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT.  
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY,  
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE  
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
FROM alpine  
  
RUN apk --update add openjdk8-jre  
RUN apk add wget curl gnupg  
  
MAINTAINER Mike Caspar <mike@caspar.com>  
  
ENV SONARQUBE_HOME /opt/sonarqube  
  
ENV SONAR_VERSION 5.2  
ENV SONAR_DOWNLOAD_URL https://sonarsource.bintray.com/Distribution  
  
# pub 2048R/D26468DE 2015-05-25  
# Key fingerprint = F118 2E81 C792 9289 21DB CAB4 CFCA 4A29 D264 68DE  
# uid [ unknown] sonarsource_deployer (Sonarsource Deployer)
<infra@sonarsource.com>  
# sub 2048R/06855C1D 2015-05-25  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
F1182E81C792928921DBCAB4CFCA4A29D26468DE  
  
RUN set -x \  
&& mkdir /opt \  
&& cd /opt \  
&& curl -o sonarqube.zip -fSL
https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-$SONAR_VERSION.zip
\  
&& curl -o sonarqube.zip.asc -fSL
https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-$SONAR_VERSION.zip.asc
\  
&& gpg --verify sonarqube.zip.asc \  
&& unzip sonarqube.zip \  
&& mv sonarqube-$SONAR_VERSION sonarqube \  
&& rm sonarqube.zip* \  
&& rm -rf $SONARQUBE_HOME/bin/*  
  
# Installing Plugins  
RUN cd /opt/sonarqube/extensions/plugins/ \  
&& curl -o sonar-java-plugin-3.9.jar -fSL $SONAR_DOWNLOAD_URL/sonar-java-
plugin/sonar-java-plugin-3.9.jar \  
&& curl -o sonar-web-plugin-2.4.jar -fSL $SONAR_DOWNLOAD_URL/sonar-web-
plugin/sonar-web-plugin-2.4.jar \  
&& curl -o sonar-scm-git-plugin-1.1.jar -fSL
http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-scm-
git-plugin/1.1/sonar-scm-git-plugin-1.1.jar \  
&& curl -o sonar-json-plugin-1.3.jar -fSL https://github.com/racodond/sonar-
json-plugin/releases/download/1.3/sonar-json-plugin-1.3.jar \  
&& curl -o sonar-jproperties-plugin-1.5.jar -fSL
https://github.com/racodond/sonar-jproperties-
plugin/releases/download/1.5/sonar-jproperties-plugin-1.5.jar \  
&& curl -o sonar-generic-coverage-plugin-1.2.jar -fSL
https://sonarsource.bintray.com/Distribution/sonar-generic-coverage/sonar-
generic-coverage-plugin-1.2.jar \  
&& curl -o sonar-cobertura-plugin-1.6.3.jar -fSL
http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-
cobertura-plugin/1.6.3/sonar-cobertura-plugin-1.6.3.jar  
  
VOLUME ["$SONARQUBE_HOME/data" , "$SONARQUBE_HOME/extensions"]  
  
WORKDIR $SONARQUBE_HOME  
COPY run.sh $SONARQUBE_HOME/bin/  
RUN chmod +x $SONARQUBE_HOME/bin/run.sh  
  
RUN apk add bash ttf-dejavu  
  
ENTRYPOINT ["./bin/run.sh"]  
  
# Http port for the outside world  
EXPOSE 9000  
# Require Port  
#EXPOSE 9001  
# H2 Database port  
#EXPOSE 9092  
# Database configuration  
#ENV SONARQUBE_JDBC_USERNAME (set in docker run with --env)  
#ENV SONARQUBE_JDBC_PASSWORD (set in docker run with --env)  
#ENV SONARQUBE_JDBC_URL (set in docker run with --env)  

