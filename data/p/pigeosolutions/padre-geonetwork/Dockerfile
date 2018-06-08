FROM tomcat:8.0-jre8  
MAINTAINER Jean Pommier <jean.pommier@pi-geosolutions.fr>  
  
# Base Padre2 Geonetwork instance  
RUN apt-get update && apt-get install -y postgresql-client zip && \  
rm -rf /var/lib/apt/lists/*  
  
ENV GN_FILE geonetwork.war  
ENV GN_REPO http://depots.pigeo.fr/WARs/geonetwork/latest  
  
ENV DATA_DIR=$CATALINA_HOME/webapps/geonetwork/WEB-INF/data  
ENV JAVA_OPTS="-Djava.security.egd=file:/dev/./urandom
-Djava.awt.headless=true -server -Xms512m -Xmx2024m -XX:NewSize=512m
-XX:MaxNewSize=1024m -XX:+UseConcMarkSweepGC"  
#Environment variables  
ENV GN_VERSION 3.4.x  
#ENV GN_DOWNLOAD_MD5 54140c3e4badc87651bd656f13f860f2  
WORKDIR $CATALINA_HOME/webapps  
  
RUN curl -fSL -o $GN_FILE \  
$GN_REPO/geonetwork.war && \  
mkdir -p geonetwork && \  
unzip -e $GN_FILE -d geonetwork && \  
rm $GN_FILE  
  
#Set PostgreSQL connection params  
COPY ./jdbc.properties $CATALINA_HOME/webapps/geonetwork/WEB-INF/config-
db/jdbc.properties  
  
#Set geonetwork data dir  
COPY ./docker-entrypoint.sh /entrypoint.sh  
#COPY ./wait-for-postgres.sh /wait-for-postgres.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["catalina.sh", "run"]  

