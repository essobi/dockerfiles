FROM node:7-alpine  
MAINTAINER kahatie <kahatie@gmail.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="ionic" \  
org.label-schema.description="ionic framework" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/kahatie/docker-ionic" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
ENV TERM=xterm \  
IONIC_VERSION=2.1.14 \  
CORDOVA_VERSION=6.4.0  
RUN npm install -g cordova@"$CORDOVA_VERSION" ionic@"$IONIC_VERSION" && \  
npm cache clear && \  
ionic start myApp sidemenu  
  
WORKDIR myApp  
  
# Expose port: web (8100), livereload (35729) EXPOSE 8100 35729  
EXPOSE 8100 35729  
CMD ["ionic", "serve", "8100", "35729"]  

