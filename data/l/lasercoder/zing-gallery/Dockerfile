FROM node:6  
RUN mkdir -p /var/www/app  
WORKDIR /var/www/app  
  
ADD . /var/www/app  
RUN rm -rf /var/www/app/resources/photos/* /var/www/app/config.js  
  
EXPOSE 3000  
RUN npm install -g cnpm --registry=https://registry.npm.taobao.org && return 0  
RUN cnpm install  
  
CMD ["cnpm", "run", "start"]  

