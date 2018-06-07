FROM java:8-jre  
MAINTAINER Kristian Østergaard Martensen <km@shipbeat.com>  
  
ENV JDBC_DRIVER=mysql-connector-java-5.1.38 \  
TEAMCITY_DATA_PATH=/var/lib/teamcity \  
TEAMCITY_CONF_PATH=/opt/TeamCity/conf  
  
VOLUME $TEAMCITY_DATA_PATH  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -qq update && \  
apt-get -qqy install libtcnative-1 && \  
apt-get -y clean autoclean autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  
  
# Install teamcity  
RUN curl -skL https://download.jetbrains.com/teamcity/TeamCity-9.1.7.tar.gz |
tar -xzC /opt;  
  
COPY server.xml $TEAMCITY_CONF_PATH/server.xml  
COPY run-teamcity-server.sh /run-teamcity-server.sh  
RUN chmod +x /run-teamcity-server.sh  
  
EXPOSE 8111  
ENTRYPOINT ["/run-teamcity-server.sh"]  

