FROM ubuntu:14.04  
MAINTAINER Medtech <medtech@uottawa.ca>  
  
# Set correct environment variables  
ENV HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"  
# We use a bootstrap script to avoid having temporary cache files and build  
# dependencies being committed and included into the docker image.  
ADD install.sh /tmp/  
RUN chmod +x /tmp/install.sh  
RUN /tmp/install.sh  
  
# Port for Python Web Wrapper  
EXPOSE 1999  
# Set our working directory  
WORKDIR "/opt/VPServer/scripts"  
  
# Execute our command to start the Visual Paradigm Licensing Server  
CMD ["/opt/VPServer/scripts/startup.sh"]  

