FROM wizeye/daviz-meteord:base  
MAINTAINER N3N  
  
ARG NODE_VERSION  
ENV NODE_VERSION ${NODE_VERSION:-4.8.3}  
ONBUILD ENV NODE_VERSION ${NODE_VERSION:-4.8.3}  
  
ONBUILD COPY ./ /app  
ONBUILD RUN bash $METEORD_DIR/lib/install_meteor.sh  
ONBUILD RUN bash $METEORD_DIR/lib/build_app.sh  

