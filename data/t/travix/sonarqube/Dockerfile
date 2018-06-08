FROM travix/base-debian-jre8:latest  
  
MAINTAINER Travix  
  
# build time environment variables  
ENV SONAR_VERSION=5.6 \  
SONARQUBE_HOME=/opt/sonarqube  
  
# install sonarqube  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
F1182E81C792928921DBCAB4CFCA4A29D26468DE \  
&& set -x \  
&& cd /opt \  
&& curl -o sonarqube.zip --insecure -fSL
https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-$SONAR_VERSION.zip
\  
&& curl -o sonarqube.zip.asc --insecure -fSL
https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-$SONAR_VERSION.zip.asc
\  
&& gpg --verify sonarqube.zip.asc \  
&& unzip sonarqube.zip \  
&& mv sonarqube-$SONAR_VERSION sonarqube \  
&& rm sonarqube.zip* \  
&& rm -rf $SONARQUBE_HOME/bin/*  
  
# runtime environment variables  
ENV SONARQUBE_JDBC_USERNAME=sonar \  
SONARQUBE_JDBC_PASSWORD=sonar \  
SONARQUBE_JDBC_URL=jdbc:h2:tcp://localhost:9092/sonar  
  
EXPOSE 9000 9092  
WORKDIR $SONARQUBE_HOME  
  
CMD exec java -jar lib/sonar-application-$SONAR_VERSION.jar \  
-Dsonar.log.console=true \  
-Dsonar.jdbc.username="$SONARQUBE_JDBC_USERNAME" \  
-Dsonar.jdbc.password="$SONARQUBE_JDBC_PASSWORD" \  
-Dsonar.jdbc.url="$SONARQUBE_JDBC_URL"

