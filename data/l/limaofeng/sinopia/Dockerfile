FROM limaofeng/node-alpine  
  
MAINTAINER Maofeng Li <limaofeng@msn.com>  
  
RUN mkdir -p /opt/sinopia/storage  
  
WORKDIR /opt/sinopia  
  
RUN npm install js-yaml sinopia  
  
ADD /config.yaml /tmp/config.yaml  
ADD /start.sh /opt/sinopia/start.sh  
  
CMD ["/opt/sinopia/start.sh"]  
  
EXPOSE 4873  
VOLUME /opt/sinopia  

