FROM ubuntu:14.04  
# Install wget  
RUN apt-get update  
RUN apt-get install -y wget  
  
# Add start script  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
# Run configuration  
ENTRYPOINT ["/start.sh"]

