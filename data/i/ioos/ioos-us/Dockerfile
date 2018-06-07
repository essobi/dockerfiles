FROM debian:jessie  
MAINTAINER Luke Campbell <luke.campbell@rpsgroup.com>  
  
ENV NODE_VERSION 7.9.0  
ENV GOSU_VERSION 1.9  
ENV SCRIPTS_DIR /opt/build_scripts  
  
RUN mkdir -p $SCRIPTS_DIR  
RUN useradd -m node  
  
COPY contrib/scripts/ $SCRIPTS_DIR/  
  
RUN $SCRIPTS_DIR/install-deps.sh  
RUN $SCRIPTS_DIR/install-node.sh  
COPY bin /opt/ioos-us/bin  
COPY public /opt/ioos-us/public  
COPY routes /opt/ioos-us/routes  
COPY views /opt/ioos-us/views  
COPY .bowerrc app.js assets.json bower.json gruntfile.js package.json
/opt/ioos-us/  
  
WORKDIR /opt/ioos-us  
RUN chown -R node:node /opt/ioos-us && \  
npm install && \  
/usr/local/bin/gosu node node_modules/bower/bin/bower install && \  
/usr/local/bin/gosu node node_modules/grunt-cli/bin/grunt  
  
ENV NODE_ENV production  
  
CMD ["/usr/local/bin/gosu", "node", "bin/www"]  

