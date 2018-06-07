FROM kahatie/debian:8  
MAINTAINER kahatie <kahatie@gmail.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="ionic" \  
org.label-schema.description="ionic framework" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/kahatie/docker" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
ENV TERM=xterm \  
WORKDIR=/workspace \  
PROJET=/workspace/myApp \  
IONIC_SERVE_PORT=8100 \  
IONIC_LIVERELOAD_PORT=35729  
# IONIC_VERSION=2.1.14 \  
# CORDOVA_VERSION=6.4.0  
VOLUME ${WORKDIR}  
  
# init script  
COPY init.sh /init.sh  
  
RUN apt-get update && \  
apt-get install -y\  
curl && \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs && \  
ln -s /usr/local/bin/node /usr/local/bin/nodejs && \  
npm update -g && \  
npm install -g cordova ionic && \  
npm cache clear && \  
apt-get clean && \  
apt-get autoclean && \  
chmod a+x /init.sh && \  
cordova telemetry off  
  
# Expose port: web (8100), livereload (35729)  
EXPOSE ${IONIC_SERVE_PORT} ${IONIC_LIVERELOAD_PORT}  
  
CMD ["/init.sh"]  

