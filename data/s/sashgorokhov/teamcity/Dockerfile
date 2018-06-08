FROM java:8-jre  
MAINTAINER Alexander Gorokhov <sashgorokhov@gmail.com>  
  
EXPOSE 8111  
ENV TEAMCITY_VERSION="9.1.6"  
ENV
TEAMCITY_DOWNLOAD_URL="https://download.jetbrains.com/teamcity/TeamCity-"$TEAMCITY_VERSION".tar.gz"
\  
TEAMCITY_DATA_PATH="/mnt/teamcity" \  
DATABASE=""  
VOLUME $TEAMCITY_DATA_PATH  
  
RUN wget -qO - $TEAMCITY_DOWNLOAD_URL | tar xz -C /opt  
  
COPY install_db_plugin.sh /  
RUN chmod +x /install_db_plugin.sh  
CMD /install_db_plugin.sh && /opt/TeamCity/bin/teamcity-server.sh run  

