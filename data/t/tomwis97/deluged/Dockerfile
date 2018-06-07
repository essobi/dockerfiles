FROM ubuntu:latest  
RUN apt-get update && \  
apt-get install deluged deluge-console -y  
RUN useradd deluge -m  
# Creating default configs  
USER deluge  
RUN deluged && \  
sleep 1 && \  
deluge-console "config -s allow_remote True" && \  
sleep 1 && \  
pkill deluged --signal SIGINT && \  
sleep 1  
  
# Environment variable for deluge admin user  
ENV ADMIN_PASSWD='Pa$$w0rd'  
# TODO: Set pasword here for now, should be moved to an initialisation script.  
RUN echo "admin:$ADMIN_PASSWD:10" >> ~/.config/deluge/auth  
  
VOLUME /home/deluge/.config/deluge  
VOLUME /home/deluge/Downloads  
  
# Deluge ports:  
# 58846: Access port  
# 58850-58860: Torrent traffic  
EXPOSE 58850-58860 58846  
CMD deluged -d  

