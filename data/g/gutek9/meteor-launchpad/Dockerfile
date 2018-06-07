FROM debian:jessie  
MAINTAINER Mateusz Adamek <mateusz.adamek87@gmail.com>  
  
RUN groupadd -r node && useradd -m -g node node  
  
ARG NODE_VERSION  
ENV NODE_VERSION ${NODE_VERSION:-8.9.0}  
  
# Gosu  
ENV GOSU_VERSION 1.10  
# MongoDB  
ENV MONGO_VERSION 3.4.10  
ENV MONGO_MAJOR 3.4  
ENV MONGO_PACKAGE mongodb-org  
  
# PhantomJS  
ENV PHANTOM_VERSION 2.1.1  
# build directories  
ENV APP_SOURCE_DIR /opt/meteor/src  
ENV APP_BUNDLE_DIR /opt/meteor/dist  
ENV BUILD_SCRIPTS_DIR /opt/build_scripts  
  
# Add entrypoint and build scripts  
COPY scripts $BUILD_SCRIPTS_DIR  
  
RUN mkdir -p $APP_SOURCE_DIR  
ADD meteor_release $APP_SOURCE_DIR/  
  
RUN chmod -R 750 $BUILD_SCRIPTS_DIR  
  
RUN cd $APP_SOURCE_DIR && \  
$BUILD_SCRIPTS_DIR/install-deps.sh && \  
$BUILD_SCRIPTS_DIR/install-node.sh && \  
$BUILD_SCRIPTS_DIR/install-phantom.sh && \  
$BUILD_SCRIPTS_DIR/install-graphicsmagick.sh && \  
$BUILD_SCRIPTS_DIR/install-mongo.sh && \  
$BUILD_SCRIPTS_DIR/install-meteor.sh  
  
# Default values for Meteor environment variables  
ENV ROOT_URL http://localhost  
ENV MONGO_URL mongodb://127.0.0.1:27017/meteor  
ENV PORT 3000  
EXPOSE 3000  
WORKDIR $APP_BUNDLE_DIR/bundle  
  
# start the app  
ENTRYPOINT ["./entrypoint.sh"]  
CMD ["node", "main.js"]  

