FROM node:6  
MAINTAINER Luiz Coura <luizcoura@gmail.com>  
  
ENV PORT 9090  
ENV ZOOKEEPER "34.204.88.242:2181"  
ADD . /var/www/timeline  
WORKDIR /var/www/timeline  
  
RUN npm install \  
&& npm install -g bower \  
&& bower install --allow-root  
  
EXPOSE 9090  
CMD ["npm", "start"]  
  

