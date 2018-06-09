FROM odino/docker-node-alpine  
MAINTAINER Katsuma Ito <katsumai@gmail.com>  
  
RUN npm install --no-optional -g dynalite \  
&& npm cache clear \  
&& rm -rf /tmp/* /var/tmp/*  
  
EXPOSE 4567  
CMD dynalite  

