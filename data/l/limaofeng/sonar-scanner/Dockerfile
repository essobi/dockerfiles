FROM java:8-jre-alpine  
  
MAINTAINER 李茂峰 limaofeng@msn.com  
  
ENV SONAR_SCANNER_VERSION 2.6.1  
ENV SONAR_SCANNER_HOME /opt/sonar-scanner-${SONAR_SCANNER_VERSION}  
ENV SONAR_SCANNER_PACKAGE sonar-scanner-${SONAR_SCANNER_VERSION}.zip  
ENV HOME ${SONAR_SCANNER_HOME}  
  
WORKDIR /opt  
  
RUN apk update \  
&& apk add bash wget ca-certificates unzip \  
&& wget https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/${SONAR_SCANNER_PACKAGE} \  
&& unzip ${SONAR_SCANNER_PACKAGE} \  
&& rm ${SONAR_SCANNER_PACKAGE}  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
  
RUN addgroup sonar \  
&& adduser -D -s /usr/sbin/nologin -h ${SONAR_SCANNER_HOME} -G sonar sonar \  
&& chown -R sonar:sonar ${SONAR_SCANNER_HOME} \  
&& mkdir -p /builds \  
&& chown -R sonar:sonar /builds  
  
USER sonar  
  
WORKDIR /builds  
  
ENTRYPOINT ["/entrypoint.sh"]

