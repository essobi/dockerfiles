FROM ubuntu:14.04  
MAINTAINER Alessio Cassibba (x-drum) <swapon@gmail.com>  
  
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" \  
> /etc/apt/sources.list.d/nginx-stable.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C && \  
apt-get update && \  
apt-get install -y nginx-extras  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

