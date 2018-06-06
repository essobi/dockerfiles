FROM ubuntu:14.04.1  
MAINTAINER Dewey Sasser <dewey@sasser.com>  
  
env DEBIAN_FRONTEND=noninteractive  
ADD AutomaticCleanup /etc/apt/apt.conf.d/99AutomaticCleanup  
  
# Install what we need from Ubuntu  
RUN apt-get update  
RUN apt-get install -y curl xymon-client  
  
# Get the 'dumb init' package for proper 'init' behavior  
RUN curl -L https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb > dumb-init.deb && \  
dpkg -i dumb-init.deb && \  
rm dumb-init.deb  
  
ENV TZ=posixrules  
ENV XYMONSERVERS=xymon  
  
ADD start /root/start  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["sh", "/root/start"]  

