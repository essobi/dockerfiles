FROM debian:wheezy  
MAINTAINER tcnksm <nsd22843@gmail.com>  
  
# Install nginx  
RUN apt-get update && apt-get install -y nginx \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Setup nginx stop deamon mode  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
ADD etc/nginx/sites-enabled/ /etc/nginx/sites-enabled/  
EXPOSE 80  
RUN mkdir /app  
RUN echo "<h1>DEMO container 2</h1><h3>at Docker meetup #4</h3>" >
/app/index.html  
CMD ["/usr/sbin/nginx"]  

