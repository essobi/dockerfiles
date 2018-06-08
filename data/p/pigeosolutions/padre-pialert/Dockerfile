FROM tomcat:8-jre8  
MAINTAINER Jean Pommier <jean.pommier@pi-geosolutions.fr>  
  
# Base Padre2 pi-alert instance  
RUN apt-get update && apt-get install -y \  
mailutils \  
postgresql-client \  
smstools \  
&& rm -rf /var/lib/apt/lists/* && apt-get clean  
  
ENV WAR_FILE pi-alert.war  
ENV REPO http://depots.pigeo.fr/WARs/pi-alert/latest  
ENV APP_NAME pi-alert  
  
ENV JAVA_OPTS="-Djava.security.egd=file:/dev/./urandom
-Djava.awt.headless=true -server -Xms512m -Xmx2024m -XX:NewSize=512m
-XX:MaxNewSize=1024m -XX:+UseConcMarkSweepGC"  
WORKDIR $CATALINA_HOME/webapps  
  
#Download pi-alert war  
#COPY ~/tmp/$WAR_FILE $CATALINA_HOME/webapps/  
RUN curl -fSL -o $WAR_FILE \  
$REPO/$WAR_FILE  
  
# Install pi-alert from war  
RUN unzip -e $WAR_FILE -d $APP_NAME && \  
rm $WAR_FILE  
  
#Set PostgreSQL connection params  
COPY ./config/application.yml ${CATALINA_HOME}/webapps/${APP_NAME}/WEB-
INF/classes/application.yml  
  
COPY ./docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["catalina.sh", "run"]  

