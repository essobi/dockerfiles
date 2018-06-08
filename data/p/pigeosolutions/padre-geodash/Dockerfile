FROM tomcat:8.0-jre8  
MAINTAINER Jean Pommier <jean.pommier@pi-geosolutions.fr>  
  
# Base Padre2 geodash instance  
RUN apt-get update && apt-get install -y postgresql-client && \  
rm -rf /var/lib/apt/lists/*  
  
ENV WAR_FILE geodash.war  
ENV REPO http://depots.pigeo.fr/WARs/geodash/latest  
ENV APP_NAME geodash  
  
ENV JAVA_OPTS="-Djava.security.egd=file:/dev/./urandom
-Djava.awt.headless=true -server -Xms512m -Xmx2024m -XX:NewSize=512m
-XX:MaxNewSize=1024m -XX:+UseConcMarkSweepGC"  
WORKDIR $CATALINA_HOME/webapps  
  
RUN curl -fSL -o $WAR_FILE \  
$REPO/$WAR_FILE && \  
mkdir -p $APP_NAME && \  
unzip -e $WAR_FILE -d $APP_NAME && \  
rm $WAR_FILE  
  
#Set PostgreSQL connection params  
COPY ./db.properties $CATALINA_HOME/webapps/$APP_NAME/WEB-INF/db.properties  
  
COPY ./docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["catalina.sh", "run"]  

