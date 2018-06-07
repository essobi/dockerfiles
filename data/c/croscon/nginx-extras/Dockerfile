FROM croscon/ubuntu:xenial  
MAINTAINER Croscon Devops <devops@croscon.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV NGINX_VERSION 1.10.3-0+xenial0  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C && \  
echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu xenial main" >>
/etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx-extras=${NGINX_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to Docker logs  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

