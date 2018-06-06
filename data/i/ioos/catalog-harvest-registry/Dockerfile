FROM debian:jessie  
MAINTAINER Luke Campbell <luke.campbell@rpsgroup.com>  
  
ENV REGISTRY_VERSION 1.2.0  
ENV NODE_VERSION 4.6.1  
ENV GOSU_VERSION 1.9  
ENV SCRIPTS_DIR /opt/build_scripts  
ENV APP_DIR /opt/meteor/dist  
ENV PORT 3000  
RUN mkdir -p $SCRIPTS_DIR  
RUN useradd -m node  
  
COPY contrib/scripts/ $SCRIPTS_DIR/  
  
RUN $SCRIPTS_DIR/install-deps.sh  
RUN $SCRIPTS_DIR/install-node.sh  
RUN $SCRIPTS_DIR/install-app.sh  
  
WORKDIR $APP_DIR/catalog-harvest-registry  
CMD ["/usr/local/bin/gosu", "node", "node", "main.js"]  

