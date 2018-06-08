FROM abernix/meteord:node-8-base  
MAINTAINER Michal Wanat  
  
VOLUME /var/deployment_data  
  
COPY scripts $METEORD_DIR  
RUN bash $METEORD_DIR/init.sh  

