FROM node:6  
MAINTAINER Luiz Coura <luizcoura@gmail.com>  
  
ENV CALLBACK "http://localhost:8080/login/facebook/return"  
ENV ZOOKEEPER "34.204.88.242:2181"  
ENV DB "mongodb"  
ENV PORT "8080"  
ADD . /var/www/pacientes  
WORKDIR /var/www/pacientes  
  
RUN npm install \  
&& npm install -g bower \  
&& bower install --allow-root  
  
EXPOSE 8080  
CMD ["npm", "start"]  
  

