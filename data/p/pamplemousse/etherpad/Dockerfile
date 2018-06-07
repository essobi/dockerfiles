FROM node:latest  
  
RUN apt-get update  
RUN apt-get install -y gzip git-core curl python libssl-dev pkg-config build-
essential  
  
RUN cd /opt && git clone git://github.com/ether/etherpad-lite.git etherpad  
RUN /opt/etherpad/bin/installDeps.sh  
  
VOLUME /opt/etherpad/var/  
  
EXPOSE 9001  
ENTRYPOINT ["/opt/etherpad/bin/run.sh"]  

