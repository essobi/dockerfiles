FROM node:0.12.14  
MAINTAINER IDNG <docker@idng.com>  
  
WORKDIR /  
  
RUN apt-get update && \  
apt-get install imagemagick -y && \  
# clean apt and tmp etc ...  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD [ "node" ]  

