FROM node:8.11.1-wheezy  
MAINTAINER Fabian <fabsterpal@gmail.com>  
  
#ENV volume /cacheserver_data  
ADD config/ /opt  
  
RUN mkdir /cacheserver_data  
  
VOLUME /cacheserver_data  
  
RUN cd /opt \  
&& ls \  
&& npm install github:Unity-Technologies/unity-cache-server -g  
EXPOSE 8126  
ENTRYPOINT ["unity-cache-server", "--NODE_CONFIG_DIR=/opt"]

