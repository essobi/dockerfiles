FROM debian:jessie  
MAINTAINER Jeremy Shimko <jeremy.shimko@gmail.com>  
  
RUN groupadd -r node && useradd -m -g node node  
  
#COPY tar_1.29b-2_amd64.deb /var/tmp/tar_1.29b-2_amd64.deb  
#RUN dpkg -i /var/tmp/tar_1.29b-2_amd64.deb  
  
# build directories  
ENV APP_SOURCE_DIR /opt/meteor/src  
ENV APP_BUNDLE_DIR /opt/meteor/dist  
ENV BUILD_SCRIPTS_DIR /opt/build_scripts  
  
# Add entrypoint and build scripts  
COPY scripts $BUILD_SCRIPTS_DIR  
RUN chmod -R 750 $BUILD_SCRIPTS_DIR && chown -R node:node $BUILD_SCRIPTS_DIR  
  
RUN mkdir -p $APP_SOURCE_DIR  
RUN mkdir -p $APP_BUNDLE_DIR  
  
ARG INSTALL_PASSENGER  
ENV INSTALL_PASSENGER ${INSTALL_PASSENGER:-true}  
  
RUN cd $APP_SOURCE_DIR && \  
$BUILD_SCRIPTS_DIR/install-passenger.sh  
  
#########################################################  
# ONBUILD  
#########################################################  
  
ONBUILD COPY . $APP_SOURCE_DIR  
  
#ONBUILD USER node  
ARG NPM_TOKEN  
ARG NODE_VERSION  
# Node flags for the Meteor build tool  
ARG TOOL_NODE_FLAGS  
  
ONBUILD ENV NPM_TOKEN $NPM_TOKEN  
ONBUILD ENV NODE_VERSION ${NODE_VERSION:-4.8.4}  
ONBUILD ENV TOOL_NODE_FLAGS ${TOOL_NODE_FLAGS:-'--max-old-space-size=3072'}  
  
ONBUILD RUN cd $APP_SOURCE_DIR && \  
echo "Environmental variable set for TOOL_NODE_FLAGS=$TOOL_NODE_FLAGS" && \  
$BUILD_SCRIPTS_DIR/install-deps.sh && \  
$BUILD_SCRIPTS_DIR/install-node.sh && \  
$BUILD_SCRIPTS_DIR/install-meteor.sh && \  
$BUILD_SCRIPTS_DIR/build-meteor.sh && \  
echo "Changing ownership to node for $APP_SOURCE_DIR and $APP_BUNDLE_DIR" && \  
chown -R node:node $APP_BUNDLE_DIR  
#chown -R node:node $APP_BUNDLE_DIR && \  
#$BUILD_SCRIPTS_DIR/post-install-cleanup.sh && \  
#$BUILD_SCRIPTS_DIR/post-build-cleanup.sh  
  
# export MAX_MEMORY=`python $BUILD_SCRIPTS_DIR/meteorbuild-mem` && \  
# export TOOL_NODE_FLAGS="$TOOL_NODE_FLAGS --max-old-space-size=$MAX_MEMORY"
&& \  
# echo "Environmental variable set for TOOL_NODE_FLAGS=$TOOL_NODE_FLAGS" && \  
  
## start the app  
#WORKDIR $APP_BUNDLE_DIR/bundle  
#CMD ["passenger", "start", "--app-type", "node", "--startup-file", "main.js"]  
#  
##WORKDIR $APP_BUNDLE_DIR/bundle  
##ENTRYPOINT ["./entrypoint.sh"]  
##CMD ["node", "main.js"]  
#CMD passenger start --app-type node --startup-file main.js --port 8090  

