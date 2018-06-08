# Create a data volume container for etc samples.  
# Re-use the node base, to reduce # of images  
FROM node:argon  
MAINTAINER W S Mckenzie <wsmckenz@cartewright.com>  
  
# create a folder for configuration  
RUN mkdir -p /var/etp/config  
WORKDIR /var/etp/config  
  
COPY . /var/etp/config  
  
VOLUME /var/etp/config  
  
ENTRYPOINT /usr/bin/tail -f /dev/null

