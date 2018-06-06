FROM mcnullty/eclipse-base:latest  
  
MAINTAINER Mladen Čikara <mladen.cikara@gmail.com>  
  
ENV DOWNLOAD_URL
https://5929985c76e75ba25f448dbc6ffd991533aaaab5.googledrive.com/host/0BzODoBJEtRwAV3NnWTVfTS1LVzA/ccw.core_0.34.0.STABLE001.tar.gz  
  
USER root  
  
RUN wget "$DOWNLOAD_URL" -O /tmp/ccw.core_0.34.0.STABLE001.tar.gz -q && \  
echo 'Installing counterclockwise' && \  
tar -xf /tmp/ccw.core_0.34.0.STABLE001.tar.gz -C /opt/eclipse && \  
rm /tmp/ccw.core_0.34.0.STABLE001.tar.gz && \  
chown root:root /opt/eclipse/features && \  
chown root:root /opt/eclipse/plugins  
  
USER developer

