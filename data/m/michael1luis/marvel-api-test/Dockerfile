FROM nginx  
  
RUN mkdir /etc/nginx/logs && touch /etc/nginx/logs/static.log  
  
ADD ./nginx.conf /etc/nginx/conf.d/default.conf  
ADD ./src /www  
  
RUN mkdir /www/build  
ADD ./build /www/build  
  
RUN chmod -R 755 ./www  

