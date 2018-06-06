FROM watawuwu/ubuntu:14.04  
ENV NGINX_VERSION 1.8.0-1+trusty1  
  
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu $(lsb_release -cs)
main" >> /etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C && \  
apt-get update && \  
apt-get install -y wget ca-certificates nginx=${NGINX_VERSION} nginx-
extras=${NGINX_VERSION} \--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD [ "nginx", "-g", "daemon off;"]  

