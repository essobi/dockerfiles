FROM ubuntu:14.04  
MAINTAINER DracoBlue <JanS@DracoBlue.de>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C && \  
echo "deb http://ppa.launchpad.net/nginx/development/ubuntu trusty main" >>
/etc/apt/sources.list  
  
ENV NGINX_VERSION 1.13.3-0+trusty1  
  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx-extras=${NGINX_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

