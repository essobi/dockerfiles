############################################################  
# Dockerfile to build the SoftFIRE Middleware Container  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu  
  
# File Author / Maintainer  
MAINTAINER SoftFIRE  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update the sources list  
RUN apt-get update && apt-get install -y git  
ADD https://api.github.com/repos/softfire-eu/bootstrap/compare/master...HEAD
/dev/null  
RUN git clone https://github.com/softfire-eu/bootstrap.git && sed -i "s/sudo
//g" bootstrap/bootstrap.sh && sed -i 's/$HOME\/.softfire/.softfire/g'
bootstrap/bootstrap.sh  
  
WORKDIR bootstrap  
  
RUN /bootstrap/bootstrap.sh install -y  
  
# Expose ports  
EXPOSE 5080  
  
CMD bash -c "source /bootstrap/.softfire/bin/activate && experiment-manager;
bash"  

