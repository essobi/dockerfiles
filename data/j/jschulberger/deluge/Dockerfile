FROM ubuntu:latest  
MAINTAINER Jon Schulberger <jschoulzy@gmail.com>  
  
EXPOSE 8112 58846 58946 58946/udp  
  
# Create user  
RUN adduser deluge --disabled-login  
  
# Pre-req for adding deluge repo  
RUN apt-get -qq update && \  
apt-get -qqy install \  
software-properties-common  
  
# Add repo, install daemon & webui  
RUN add-apt-repository -y ppa:deluge-team/ppa && \  
apt-get -qq update && \  
apt-get -qqy install \  
deluge-webui \  
deluged && \  
rm -rf /var/lib/apt/lists/*  
  
# Move the entrypint file over  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME /home/deluge  
  
# Assign user  
USER deluge  
  
CMD ["/entrypoint.sh"]  

