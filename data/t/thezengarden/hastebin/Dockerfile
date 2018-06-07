###################################  
# The Zen Garden :: Hastebin #  
# Build Tag: 171128-1042 #  
###################################  
FROM alpine:latest  
MAINTAINER Chris Hammer <chris@thezengarden.net>  
  
  
# Update base and install required deps:  
########################################  
RUN apk update  
RUN apk add nodejs nodejs-npm git procps bash redis  
  
  
# Clone git repo & run installer:  
#################################  
RUN /bin/bash -l -c "cd / \  
&& git clone https://github.com/seejohnrun/haste-server.git \  
&& cd haste-server \  
&& npm install"  
  
  
# Expose default port:  
######################  
EXPOSE 7777  
  
  
# Set CWD upon launch to hastebin-server  
# install path:  
########################################  
WORKDIR /haste-server  
  
  
# Copy configs into image:  
##########################  
COPY etc/config_local_redis.js /haste-server/config.js  
COPY etc/redis_no_comments.conf /etc/redis.conf  
  
  
# By default, kick off hastebin-server:  
#######################################  
#CMD ["npm start"]  
CMD redis-server /etc/redis.conf && npm start  

