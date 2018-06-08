FROM ubuntu:16.04  
# MAINTAINER pooya parsa <pooya@pi0.ir>  
# https://www.gluu.org/docs/deployment/ubuntu-xenial  
# Export Ports  
EXPOSE 80 443  
# Install Gluu  
ENV GLUU_VERSION 2.4.4  
COPY bin/gluu_install /bin  
RUN gluu_install  
  
# Copy Scripts  
COPY bin/* /bin/  

