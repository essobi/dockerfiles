FROM nginx:latest  
  
MAINTAINER Ilya Rumyantsev <explosivebit@gmail.com>  
  
ADD nginx.conf /etc/nginx/  
ADD virtual-host.conf /etc/nginx/conf.d/  
  
RUN echo "upstream php-upstream { server php:9001; }" >
/etc/nginx/conf.d/upstream.conf  
  
RUN usermod -u 1000 www-data  
RUN ulimit -s unlimited  
  
CMD ["nginx"]  
  
EXPOSE 80 443  

