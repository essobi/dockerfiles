# -*- docker-image-name: "ashgillman/niftireg:latest" -*-  
FROM debian:jessie  
MAINTAINER Ashley Gillman <ashley.gillman@csiro.au>  
  
# Source working/installation directory  
ENV INSTALL /usr/local/src  
  
#---------------------------------------------------------------------  
# Dependencies  
#---------------------------------------------------------------------  
ENV DEBIAN_FRONTEND noninteractive  
  
#---------------------------------------------------------------------  
# Nifty Reg  
#---------------------------------------------------------------------  
ENV NIFTY_VER 1.3.9  
ENV NIFTY_SRC $INSTALL/niftyreg-src  
ENV NIFTY_DIR $INSTALL/niftyreg  
COPY install.sh /scripts/install_niftyreg.sh  
RUN /scripts/install_niftyreg.sh  
  
#---------------------------------------------------------------------  
# MOTD / Welcome message  
#---------------------------------------------------------------------  
COPY ABOUT /etc/motd  
RUN echo '[ ! -z "$TERM" -a -r /etc/motd ] '\  
'&& cat /proc/version && cat /etc/motd'\  
'&& echo "Source directory is $INSTALL\n"' \  
>> /etc/bash.bashrc  
  
#---------------------------------------------------------------------  
# Tini entrypoint  
#---------------------------------------------------------------------  
# Add Tini init script - take care of runaway processes  
ENV TINI_VERSION v0.7.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
  
ENTRYPOINT ["/tini", "--"]  
CMD ["bash"]  

