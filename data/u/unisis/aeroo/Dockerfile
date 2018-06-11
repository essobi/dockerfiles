##################################################  
#  
# Dockerfile for Aeroo  
#  
###################################################  
  
# Based on https://github.com/ingadhoc/docker-aeroo-docs  
  
FROM ubuntu:14.04  
MAINTAINER Unisis <contacto@unisis.com.ar>  
  
ENV REFRESHED_AT 2015-05-02  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y git nano python3-uno libreoffice-writer libreoffice-calc
python3-pip xvfb supervisor openjdk-7-jre libreoffice-l10n-es && \  
apt-get clean  
  
RUN pip3 install jsonrpc2  
RUN pip3 install daemonize  
  
RUN git clone https://github.com/aeroo/aeroo_docs.git /opt/aeroo_docs  
  
# Add config file  
ADD config/supervisord.conf /root/supervisord.conf  
  
# Install startup script  
ADD scripts/start.sh /root/start.sh  
RUN chmod +x /root/start.sh  
  
# Run Init script  
CMD ["/root/start.sh"]  

