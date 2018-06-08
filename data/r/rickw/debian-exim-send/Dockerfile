# This Dockerfile is based on miracle2k's exim-sender  
# (https://github.com/miracle2k/dockerfiles/tree/master/exim-sender)  
FROM debian:jessie  
  
MAINTAINER Rick Wieman <git@rickw.nl>  
  
# Install exim and xtail (for logs)  
RUN apt-get update && apt-get install -y exim4 xtail \  
&& rm -r /var/lib/apt/lists/*  
  
# Add our configuration  
RUN rm -rf /etc/exim4 && mkdir -p /etc/exim4  
ADD exim4.conf /etc/exim4/exim4.conf  
  
# Add the launch script  
ADD start.sh /exim  
RUN chmod +x /exim  
  
ENTRYPOINT ["/exim"]  

