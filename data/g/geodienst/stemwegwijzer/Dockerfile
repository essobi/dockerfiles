FROM node  
COPY www /data/www  
COPY package.json yarn.lock /data/  
WORKDIR /data  
RUN yarn  
RUN yarn build  
  
FROM nginx  
COPY \--from=0 /data/www/ /static  
COPY nginx.conf /etc/nginx/nginx.conf  
VOLUME /data  

