######################  
# Dockerfile for #  
# building a go-tour #  
# image for Docker #  
######################  
  
# Set base image to Alpine.  
FROM gliderlabs/alpine  
  
# Set maintainer.  
MAINTAINER shymega <shymega@shymega.org.uk>  
  
# Inject installation script.  
ADD ./install.sh /install.sh  
  
# Run installation script.  
RUN /install.sh  
  
# Add run.sh  
ADD ./run.sh /run.sh  
  
# Expose the listening port  
EXPOSE 3999  
  
# Set cmd on run and run as gotour  
USER gotour  
CMD ["/run.sh"]  

