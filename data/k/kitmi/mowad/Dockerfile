FROM debian:wheezy  
MAINTAINER KIT Mobile Internet Pty Ltd  
  
ENV MOWAD_DIR /opt/mowad  
COPY scripts $MOWAD_DIR  
  
RUN bash $MOWAD_DIR/init.sh  
  
EXPOSE 80

