FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx nginx-extras && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
ADD default.conf /etc/nginx/conf.d/default.conf  
  
ADD fancyindex /usr/share/nginx/fancyindex  
  
WORKDIR /usr/share/nginx/html  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

