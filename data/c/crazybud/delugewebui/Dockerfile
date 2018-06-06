# Select the latest ubuntu image to build this container  
########################################################  
FROM crazybud/base-ubu-latest:latest  
MAINTAINER crazyBUD  
  
# Add needed packages  
#####################  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq unzip
unrar deluged deluge-webui  
  
# Docker settings  
#################  
  
# expose port for http : 8112  
# expose port for deluge daemon : 58846  
# expose port for incoming torrent data (tcp and udp) : 58946 58946/udp  
EXPOSE 8112 58846 58946 58946/udp  
  
# Build deluge file system  
##########################  
  
RUN mkdir /data/.incomplete && mkdir /data/AutoAdd  
  
# Add conf file for `supervisor`  
################################  
  
ADD https://raw.githubusercontent.com/40thoughts/docker-
DelugeWebUI/master/.apps.conf /etc/supervisor/conf.d/deluge.conf  
  
# Lighten the image if possible  
###############################  
RUN apt-get clean && rm -rf /tmp/*  
  
# Run `supervisor`  
##################  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.conf", "-n"]  

