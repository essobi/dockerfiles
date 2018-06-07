FROM kennedyoliveira/java8  
MAINTAINER Kennedy Oliveira <kennedy.oliveira@outlook.com>  
  
ENV TEAMCITY_VERSION 10.0.4  
ENV TEAMCITY_DATA_PATH /var/lib/teamcity  
ENV TEAMCITY_POSTGRE_JDBC_DRIVER postgresql-9.4.1209.jar  
  
# Updates the packages and install needed softwares  
RUN apk update && \  
apk upgrade && \  
apk add curl && \  
rm -rf /var/cache/apk/* && \  
# Create dir for TeamCity installation  
mkdir -p /opt && \  
# Get and install teamcity  
curl -L
http://download.jetbrains.com/teamcity/TeamCity-$TEAMCITY_VERSION.tar.gz | tar
xz -C /opt && \  
# Enable the correct Valve when running behind a proxy  
sed -i -e "s/\\.*<\/Host>.*$/<Valve
className=\"org.apache.catalina.valves.RemoteIpValve\"
protocolHeader=\"x-forwarded-proto\" \/><\/Host>/"
/opt/TeamCity/conf/server.xml && \  
# Create the directory for jdbc drivers  
mkdir -p $TEAMCITY_DATA_PATH/lib/jdbc  
  
# Default teamcity port  
EXPOSE 8111  
# Data volume  
VOLUME $TEAMCITY_DATA_PATH  
  
# Copy configuration for migration  
COPY ["database.postgresql.properties", "/tmp/database.postgresql.properties"]  
  
# Copy started script  
COPY ["docker-entrypoint.sh", "/docker-entrypoint.sh"]  
  
# Fix permissions  
RUN chmod 755 /docker-entrypoint.sh  
  
# Set entry point to the starter script  
ENTRYPOINT ["/docker-entrypoint.sh"]  

