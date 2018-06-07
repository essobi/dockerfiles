FROM nginx  
  
RUN apt-get update && apt-get install vim -y  
  
ADD conf.d /etc/nginx/conf.d/  
  
COPY nginx.conf /etc/nginx/nginx.conf  

