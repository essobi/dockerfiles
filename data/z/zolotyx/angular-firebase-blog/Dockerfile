FROM node:slim  
MAINTAINER Ilya Zolotukhin  
  
COPY ./docker/nginx.conf /etc/nginx/conf.d/default.conf  
COPY . /var/www/app  
WORKDIR /var/www/app  
RUN apt-get update && apt-get install -y --no-install-recommends nginx-light
&& \  
npm install && npm run build -- --prod --aot && \  
cp -r /var/www/app/dist /var/www/dist && rm -rf /var/www/app  
  
CMD ["nginx", "-g", "daemon off;"]  

