FROM isbjorn/meteord:base  
MAINTAINER MeteorHacks Pvt Ltd.  
  
ARG NODE_VERSION  
ENV NODE_VERSION ${NODE_VERSION:-4.8.4}  
ONBUILD ENV NODE_VERSION ${NODE_VERSION:-4.8.4}  
  
ONBUILD COPY ./ /app  
ONBUILD RUN bash $METEORD_DIR/lib/install_meteor.sh  
ONBUILD RUN bash $METEORD_DIR/lib/build_app.sh  

