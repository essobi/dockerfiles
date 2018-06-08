FROM rowanto/docker-wheezy-java8:master  
MAINTAINER Rowanto "rowanto@gmail.com"  
RUN apt-get update && apt-get install nginx -y  
COPY default /etc/nginx/sites-available/default  
RUN service nginx restart  
  
EXPOSE 80  
  
CMD ["bash"]  

