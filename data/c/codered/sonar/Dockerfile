FROM codered/ubuntu-java8  
MAINTAINER Ronan Gill <ronan.gill@code.com>  
  
# Based on https://github.com/SonarSource/docker-sonarqube  
ENV SONARQUBE_HOME /opt/sonarqube  
ENV SONARQUBE_JDBC_USERNAME sonar  
ENV SONARQUBE_JDBC_PASSWORD sonar  
ENV SONARQUBE_JDBC_URL jdbc:h2:tcp://localhost:9092/sonar  
ENV SONAR_VERSION 5.3  
ENV SONARQUBE_WEB_CONTEXT ""  
# pub 2048R/D26468DE 2015-05-25  
# Key fingerprint = F118 2E81 C792 9289 21DB CAB4 CFCA 4A29 D264 68DE  
# uid sonarsource_deployer (Sonarsource Deployer) <infra@sonarsource.com>  
# sub 2048R/06855C1D 2015-05-25  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
F1182E81C792928921DBCAB4CFCA4A29D26468DE  
  
RUN set -x \  
&& cd /opt \  
&& curl -o sonarqube.zip -fSL
https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-$SONAR_VERSION.zip
\  
&& curl -o sonarqube.zip.asc -fSL
https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-$SONAR_VERSION.zip.asc
\  
&& gpg --batch --verify sonarqube.zip.asc sonarqube.zip \  
&& unzip sonarqube.zip \  
&& mv sonarqube-$SONAR_VERSION sonarqube \  
&& rm sonarqube.zip* \  
&& rm -rf $SONARQUBE_HOME/bin/*  
  
EXPOSE 9000  
VOLUME ["$SONARQUBE_HOME/data", "$SONARQUBE_HOME/extensions"]  
  
WORKDIR $SONARQUBE_HOME  
CMD java -jar lib/sonar-application-$SONAR_VERSION.jar \  
-Dsonar.log.console=true \  
-Dsonar.jdbc.username="$SONARQUBE_JDBC_USERNAME" \  
-Dsonar.jdbc.password="$SONARQUBE_JDBC_PASSWORD" \  
-Dsonar.jdbc.url="$SONARQUBE_JDBC_URL" \  
-Dsonar.web.javaAdditionalOpts="-Djava.security.egd=file:/dev/./urandom" \  
-Dsonar.web.context="$SONARQUBE_WEB_CONTEXT"  

