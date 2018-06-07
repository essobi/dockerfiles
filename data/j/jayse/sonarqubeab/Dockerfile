FROM java:8  
MAINTAINER jayse <g.tour@free.fr>  
  
ENV SONAR_VERSION=6.1 \  
SONARQUBE_HOME=/opt/sonarqube \  
# Database configuration  
# Defaults to using H2  
SONARQUBE_JDBC_USERNAME=sonar \  
SONARQUBE_JDBC_PASSWORD=sonar \  
SONARQUBE_JDBC_URL=  
  
ENV SONAR_SCANNER_VERSION 2.8  
ENV SONAR_SCANNER_PACKAGE sonar-scanner-${SONAR_SCANNER_VERSION}.zip  
  
# Http port  
EXPOSE 9000  
# If Proxy add  
# export http_proxy=http://proxy:3128 \  
# && export https_proxy=$http_proxy  
RUN set -x \  
&& cd /opt \  
&& wget
https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-$SONAR_VERSION.zip
\  
&& unzip sonarqube-$SONAR_VERSION.zip \  
&& mv sonarqube-$SONAR_VERSION sonarqube \  
&& rm sonarqube-$SONAR_VERSION.zip* \  
&& rm -rf $SONARQUBE_HOME/bin/*  
  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-php-plugin/sonar-
php-plugin-2.9.1.1705.jar \  
&& mv sonar-php-plugin-2.9.1.1705.jar $SONARQUBE_HOME/extensions/plugins/ \  
&& wget https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/${SONAR_SCANNER_PACKAGE} \  
&& unzip ${SONAR_SCANNER_PACKAGE} \  
&& rm ${SONAR_SCANNER_PACKAGE} \  
&& mv sonar-scanner-${SONAR_SCANNER_VERSION}/bin/* $SONARQUBE_HOME/bin/ \  
&& mv sonar-scanner-${SONAR_SCANNER_VERSION}/lib/sonar-scanner-
cli-${SONAR_SCANNER_VERSION}.jar $SONARQUBE_HOME/lib/ \  
&& mv sonar-scanner-${SONAR_SCANNER_VERSION}/conf/sonar-scanner.properties
$SONARQUBE_HOME/conf/  
RUN rm -r sonar-scanner-${SONAR_SCANNER_VERSION}  
  
VOLUME ["$SONARQUBE_HOME/data", "$SONARQUBE_HOME/extensions"]  
  
WORKDIR $SONARQUBE_HOME  
COPY run.sh $SONARQUBE_HOME/bin/  
ENTRYPOINT ["./bin/run.sh"]  
  

