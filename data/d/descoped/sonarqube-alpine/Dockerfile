FROM openjdk:8-alpine  
  
MAINTAINER Ove Ranheim (oranheim@descoped.io)  
# Based on offical image by David Gageot <david.gageot@sonarsource.com>  
ENV SONAR_VERSION=7.0 \  
SONARQUBE_HOME=/opt/sonarqube \  
# Database configuration  
# Defaults to using H2  
SONARQUBE_JDBC_USERNAME=sonar \  
SONARQUBE_JDBC_PASSWORD=sonar \  
SONARQUBE_JDBC_URL=  
  
# Http port  
EXPOSE 9000  
RUN addgroup -S sonarqube && adduser -S -G sonarqube sonarqube  
  
RUN set -x \  
&& apk add --no-cache gnupg unzip curl \  
&& apk add --no-cache libressl wget \  
&& apk add --no-cache su-exec \  
&& apk add --no-cache bash \  
  
# pub 2048R/D26468DE 2015-05-25  
# Key fingerprint = F118 2E81 C792 9289 21DB CAB4 CFCA 4A29 D264 68DE  
# uid sonarsource_deployer (Sonarsource Deployer) <infra@sonarsource.com>  
# sub 2048R/06855C1D 2015-05-25  
#&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
F1182E81C792928921DBCAB4CFCA4A29D26468DE \  
&& gpg --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
F1182E81C792928921DBCAB4CFCA4A29D26468DE \  
  
&& mkdir /opt \  
&& cd /opt \  
&& curl -o sonarqube.zip -fSL --insecure
https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-$SONAR_VERSION.zip
\  
&& curl -o sonarqube.zip.asc -fSL --insecure
https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-$SONAR_VERSION.zip.asc
\  
&& gpg --batch --verify sonarqube.zip.asc sonarqube.zip \  
&& unzip sonarqube.zip \  
&& mv sonarqube-$SONAR_VERSION sonarqube \  
&& rm sonarqube.zip* \  
&& rm -rf $SONARQUBE_HOME/bin/* \  
&& if [ ! -f "$SONARQUBE_HOME/conf_org" ]; then mv $SONARQUBE_HOME/conf
$SONARQUBE_HOME/conf_org; fi  
  
VOLUME ["$SONARQUBE_HOME/secret", "$SONARQUBE_HOME/conf",
"$SONARQUBE_HOME/extensions", "$SONARQUBE_HOME/data", "$SONARQUBE_HOME/logs"]  
WORKDIR $SONARQUBE_HOME  
COPY run.sh $SONARQUBE_HOME/bin/  
  
#RUN cp $SONARQUBE_HOME/conf_org/* $SONARQUBE_HOME/conf/  
ENTRYPOINT ["./bin/run.sh"]  

