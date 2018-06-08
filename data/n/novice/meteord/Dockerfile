FROM ubuntu:14.04  
MAINTAINER David  
  
ENV METEORD_DIR /opt/meteord  
COPY scripts $METEORD_DIR  
  
RUN bash $METEORD_DIR/init.sh  
  
EXPOSE 80  
ENTRYPOINT bash $METEORD_DIR/run_app.sh  

