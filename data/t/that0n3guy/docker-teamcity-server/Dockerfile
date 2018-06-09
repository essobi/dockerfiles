####################################  
# Ubuntu Baseimage Team City 8 Docker Image  
# run this with: docker run -dt --name teamcity_server -p 8111:8111
that0n3guy/docker-teamcity-server  
# build this with: docker build -t teamcity-server .  
####################################  
FROM phusion/baseimage:0.9.17  
ENV TEAM_CITY_BASE_URL http://download-ln.jetbrains.com/teamcity  
ENV TEAM_CITY_PACKAGE TeamCity-9.1.5.tar.gz  
ENV TEAM_CITY_INSTALL_DIR /opt/  
ENV MYSQL_JDBC_PACKAGE mysql-connector-java-5.1.37  
# teamcity uses this env var to define the datapath  
ENV TEAMCITY_DATA_PATH /opt/teamcity-data  
  
# this is based on http://phusion.github.io/baseimage-docker/  
CMD ["/sbin/my_init"]  
  
## update apt and install jre  
RUN apt-get update  
RUN apt-get install -y wget default-jre  
  
# Get the teamcity package and extract it.  
RUN wget -q -O - $TEAM_CITY_BASE_URL/$TEAM_CITY_PACKAGE | tar xzf - -C
$TEAM_CITY_INSTALL_DIR  
  
# Get the jdbc drivers for mysql and mv it to a temp location. We will copy to
the right location durring boot just in case volume  
RUN mkdir -p $TEAMCITY_DATA_PATH/lib/jdbc  
RUN wget -q -O -
http://dev.mysql.com/get/Downloads/Connector-J/$MYSQL_JDBC_PACKAGE.tar.gz |
tar xzf - -C /opt/  
#RUN mv $TEAMCITY_DATA_PATH/lib/jdbc/$MYSQL_JDBC_PACKAGE/$MYSQL_JDBC_PACKAGE-
bin.jar $TEAMCITY_DATA_PATH/lib/jdbc  
#RUN rm -r $TEAMCITY_DATA_PATH/lib/jdbc/$MYSQL_JDBC_PACKAGE  
# setup runit to run teamcity on startup  
RUN mkdir /etc/service/teamcity-server  
ADD run-teamcity-server.sh /etc/service/teamcity-server/run  
RUN chmod +x /etc/service/teamcity-server/run  
  
EXPOSE 8111  
# this isn't needed:  
# CMD .$TEAM_CITY_INSTALL_DIR/TeamCity/bin/teamcity-server.sh run  
VOLUME ["/opt/teamcity-data"]  
  

