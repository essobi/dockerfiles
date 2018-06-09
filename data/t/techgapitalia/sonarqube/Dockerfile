FROM jboss/base-jdk:8  
MAINTAINER Erik Jacobs <erikmjacobs@gmail.com>  
MAINTAINER Siamak Sadeghianfar <siamaksade@gmail.com>  
MAINTAINER Giovanni Condello <g.condello@techgap.it>  
  
ENV SONAR_VERSION=7.1 \  
SONARQUBE_HOME=/opt/sonarqube \  
SONARQUBE_JDBC_USERNAME=sonar \  
SONARQUBE_JDBC_PASSWORD=sonar \  
SONARQUBE_JDBC_URL=  
  
USER root  
EXPOSE 9000  
ADD root /  
  
RUN set -x \  
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
  
WORKDIR $SONARQUBE_HOME  
COPY run.sh $SONARQUBE_HOME/bin/  
  
RUN useradd -r sonar  
RUN /usr/bin/fix-permissions $SONARQUBE_HOME \  
&& chmod 775 $SONARQUBE_HOME/bin/run.sh  
  
USER sonar  
ENTRYPOINT ["./bin/run.sh"]  

