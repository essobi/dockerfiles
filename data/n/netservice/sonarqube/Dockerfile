FROM java:8-alpine  
  
MAINTAINER daniele franceschi netserv it  
  
ENV SONAR_VERSION=5.6 \  
SONARQUBE_HOME=/opt/sonarqube \  
# Database configuration  
SONARQUBE_JDBC_USERNAME=sonar \  
SONARQUBE_JDBC_PASSWORD=sonar \  
SONARQUBE_JDBC_URL= \  
SONAR_DOWNLOAD_URL=https://sonarsource.bintray.com/Distribution  
  
# Http port  
EXPOSE 9000  
RUN set -x \  
&& apk add --no-cache gnupg unzip curl \  
  
# pub 2048R/D26468DE 2015-05-25  
# Key fingerprint = F118 2E81 C792 9289 21DB CAB4 CFCA 4A29 D264 68DE  
# uid sonarsource_deployer (Sonarsource Deployer) <infra@sonarsource.com>  
# sub 2048R/06855C1D 2015-05-25  
&& gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
0xCFCA4A29D26468DE \  
  
&& mkdir /opt \  
&& cd /opt \  
&& curl -o sonarqube.zip -fSL
$SONAR_DOWNLOAD_URL/sonarqube/sonarqube-$SONAR_VERSION.zip \  
&& curl -o sonarqube.zip.asc -fSL
$SONAR_DOWNLOAD_URL/sonarqube/sonarqube-$SONAR_VERSION.zip.asc \  
&& gpg --batch --verify sonarqube.zip.asc sonarqube.zip \  
&& unzip sonarqube.zip \  
&& mv sonarqube-$SONAR_VERSION sonarqube \  
&& rm sonarqube.zip* \  
&& rm -rf $SONARQUBE_HOME/bin/*  
  
RUN cd /opt/sonarqube/extensions/plugins/ \  
&& curl -o sonar-java-plugin-3.14.jar -fSL $SONAR_DOWNLOAD_URL/sonar-java-
plugin/sonar-java-plugin-3.14.jar \  
&& curl -o sonar-web-plugin-2.4.jar -fSL $SONAR_DOWNLOAD_URL/sonar-web-
plugin/sonar-web-plugin-2.4.jar \  
&& curl -o sonar-groovy-plugin-1.3.1.jar -fSL $SONAR_DOWNLOAD_URL/sonar-
groovy-plugin/sonar-groovy-plugin-1.3.1.jar \  
&& curl -o sonar-scm-svn-plugin-1.3.jar -fSL $SONAR_DOWNLOAD_URL/sonar-scm-
svn-plugin/sonar-scm-svn-plugin-1.3.jar \  
&& curl -o sonar-ldap-plugin-2.0.jar -fSL $SONAR_DOWNLOAD_URL/sonar-ldap-
plugin/sonar-ldap-plugin-2.0.jar \  
&& curl -o sonar-scm-git-plugin-1.1.jar -fSL $SONAR_DOWNLOAD_URL/sonar-scm-
git-plugin/sonar-scm-git-plugin-1.2.jar \  
&& curl -o sonar-jproperties-plugin-1.7.jar -fSL
https://github.com/racodond/sonar-jproperties-
plugin/releases/download/1.7/sonar-jproperties-plugin-1.7.jar \  
&& curl -o sonar-css-plugin.jar-1.10.jar -fSL
https://github.com/SonarQubeCommunity/sonar-css/releases/download/1.10/sonar-
css-plugin.jar \  
&& curl -o sonar-javascript-plugin-2.13.jar -fSL $SONAR_DOWNLOAD_URL/sonar-
javascript-plugin/sonar-javascript-plugin-2.13.jar \  
&& curl -o sonar-json-plugin-1.4.jar -fSL https://github.com/racodond/sonar-
json-plugin/releases/download/1.4/sonar-json-plugin-1.4.jar \  
&& curl -o sonar-generic-coverage-plugin-1.2.jar -fSL
$SONAR_DOWNLOAD_URL/sonar-generic-coverage/sonar-generic-coverage-
plugin-1.2.jar  
  
VOLUME ["$SONARQUBE_HOME/data", "$SONARQUBE_HOME/extensions"]  
  
WORKDIR $SONARQUBE_HOME  
COPY run.sh $SONARQUBE_HOME/bin/  
RUN chmod +x $SONARQUBE_HOME/bin/run.sh  
ENTRYPOINT ["./bin/run.sh"]  

