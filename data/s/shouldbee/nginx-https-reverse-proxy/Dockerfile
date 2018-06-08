FROM ubuntu:14.04  
RUN sudo apt-get update  
RUN sudo apt-get install -y nginx  
  
RUN sudo mkdir /usr/local/nginx  
RUN sudo mkdir /usr/local/nginx/conf  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
RUN rm /etc/nginx/sites-enabled/default  
  
ADD server.key /usr/local/nginx/conf/server.key  
ADD server.crt /usr/local/nginx/conf/server.crt  
ADD nginx.conf /etc/nginx/conf.d/nginx.conf  
  
CMD ["nginx"]  

