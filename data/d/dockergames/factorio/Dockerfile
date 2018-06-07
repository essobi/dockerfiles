FROM dockergames/factorio:base  
  
# Author  
MAINTAINER Milan Sulc <sulcmil@gmail.com>  
  
# Variables  
ENV FACTORIO_VERSION=0.12.35  
ENV FACTORIO_BIN=$FACTORIO_HOME/bin/x64/factorio  
  
# Change user  
USER $FACTORIO_USER  
  
# Download factorio  
RUN wget --no-check-certificate https://www.factorio.com/get-
download/$FACTORIO_VERSION/demo/linux64 -O $FACTORIO_HOME/factorio.tar.gz  
  
# Extract factorio  
RUN tar -xzf $FACTORIO_HOME/factorio.tar.gz -C /home  
  
# Remove downloaded files  
RUN rm $FACTORIO_HOME/factorio.tar.gz  
  
# Volumes  
VOLUME $FACTORIO_HOME  
  
# Run factorio  
ENTRYPOINT $FACTORIO_BIN  

