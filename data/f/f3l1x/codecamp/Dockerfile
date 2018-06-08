FROM debian:jessie  
  
MAINTAINER Milan Sulc <sulcmil@gmail.com>  
  
# Disable interactive mode  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update dist  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y curl wget  
  
# Install NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - \  
&& apt-get install -y nodejs  
  
# Install packages  
RUN npm install -g \  
gulp \  
bower \  
grunt \  
ionic@beta \  
cordova  
  
# Install git  
RUN apt-get install -y git  
  
# Clean  
RUN apt-get clean && apt-get autoremove  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Volumes  
VOLUME /data  
WORKDIR /data  
  
# Scripts  
ADD ./scripts/codecamp-share.sh /usr/bin/codecamp-share  
  
# Entrypoint  
CMD ["/bin/bash"]  

