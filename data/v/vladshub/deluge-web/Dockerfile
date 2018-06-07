FROM vladshub/deluge:latest  
MAINTAINER Vladislav Shub <vlad6il@gmail.com>  
  
# Managment  
#EXPOSE 58846  
# Torrent ports  
#EXPOSE 6881 6891  
# Deluge-web  
EXPOSE 8112  
  
# Torrent Client  
#CMD ["deluged", "-c", "/config", "-d"]  
# Web interface  
CMD ["deluge-web", "-c", "/data"]  

