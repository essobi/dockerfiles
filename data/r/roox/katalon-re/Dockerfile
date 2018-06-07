FROM ubuntu:16.04  
# common environment variables  
ENV KATALON_ROOT_DIR=/katalon  
ENV KATALON_VERSION_FILE=/katalon/version  
ENV KATALON_INSTALL_DIR=/opt/katalonstudio  
ENV KATALON_KATALON_DIR=/katalon/katalon  
  
# copy scripts  
RUN mkdir -p $KATALON_ROOT_DIR  
RUN mkdir -p $KATALON_KATALON_DIR  
RUN mkdir -p $KATALON_ROOT_DIR/scripts  
WORKDIR $KATALON_ROOT_DIR  
  
ADD ./scripts/*.sh $KATALON_ROOT_DIR/scripts/  
RUN chmod a+x $KATALON_ROOT_DIR/scripts/*.sh  
  
# build  
ENV DISPLAY :99  
ENV DISPLAY_CONFIGURATION 1280x1024x24  
  
WORKDIR /  
RUN $KATALON_ROOT_DIR/scripts/index.sh  
  
WORKDIR /  
  
ENTRYPOINT cat $KATALON_VERSION_FILE &&
$KATALON_ROOT_DIR/scripts/entrypoint.sh  

