####################  
# Dockerfile for #  
# building a SBBS #  
# image for Docker #  
####################  
  
# Set base image  
FROM debian:stable  
  
# Set maintainer.  
MAINTAINER shymega <shymega@shymega.org.uk>  
  
# Add install script to the image.  
ADD ./install.sh /install.sh  
# Run install script.  
RUN /install.sh  
  
# Add run script to image  
ADD ./run.sh /run.sh  
  
# Set runtime user as root.  
USER root  
  
# Set entrypoint to /run.sh  
CMD ["/run.sh"]  

