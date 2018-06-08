# Base image  
FROM openjdk:8  
# Maintainer  
MAINTAINER Ivo Krooswijk "ivo@krooswijk.com"  
# Environment variables  
ENV SONAR_VERSION=6.2 \  
SONARQUBE_HOME=/opt/sonarqube \  
# Database configuration  
# Defaults to using H2  
SONARQUBE_JDBC_USERNAME=sonar \  
SONARQUBE_JDBC_PASSWORD=sonar \  
SONARQUBE_JDBC_URL=  
  
# Install Sonarqube  
RUN set -x \  
# pub 2048R/D26468DE 2015-05-25  
# Key fingerprint = F118 2E81 C792 9289 21DB CAB4 CFCA 4A29 D264 68DE  
# uid sonarsource_deployer (Sonarsource Deployer) <infra@sonarsource.com>  
# sub 2048R/06855C1D 2015-05-25  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
F1182E81C792928921DBCAB4CFCA4A29D26468DE \  
  
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
  
# Volumes  
VOLUME "$SONARQUBE_HOME/data"  
  
# Copy configuration  
WORKDIR $SONARQUBE_HOME  
COPY run.sh $SONARQUBE_HOME/bin/  
  
# Expose ports  
EXPOSE 9000  
# Run command  
ENTRYPOINT ["./bin/run.sh"]  

