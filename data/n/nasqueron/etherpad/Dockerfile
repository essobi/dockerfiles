#  
# Docker image for Etherpad  
#  
FROM debian:jessie  
  
# Forked from Tony Motakis <tvelocity@gmail.com>  
MAINTAINER Sébastien Santoro aka Dereckson <dereckson+nasqueron-docker@espace-
win.org>  
  
RUN apt-get update && \  
apt-get install -y curl unzip nodejs-legacy npm mysql-client git && \  
rm -r /var/lib/apt/lists/*  
  
RUN cd /opt && \  
git clone https://github.com/ether/etherpad-lite && \  
cd etherpad-lite && \  
bin/installDeps.sh && \  
rm settings.json  
  
COPY entrypoint.sh /entrypoint.sh  
VOLUME /opt/etherpad-lite/var  
  
RUN ln -s /opt/etherpad-lite/var/settings.json /opt/etherpad-
lite/settings.json  
  
WORKDIR /opt/etherpad-lite  
EXPOSE 9001  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bin/run.sh", "--root"]  

