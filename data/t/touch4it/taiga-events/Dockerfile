FROM node:6.10  
MAINTAINER Touch4IT <hi@touch4it.com>  
  
COPY taiga-events /taiga-events  
  
WORKDIR /taiga-events  
  
RUN npm install --production  
RUN npm install -g coffee-script  
  
COPY config.json /taiga-events/config.json  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["coffee", "index.coffee"]  
  
EXPOSE 80  

