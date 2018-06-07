FROM gregory90/base:latest  
  
ENV NGINX_VERSION 1.9.1-1~jessie  
  
RUN wget http://nginx.org/keys/nginx_signing.key && apt-key add
nginx_signing.key  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y nginx=${NGINX_VERSION} && rm -rf
/var/lib/apt/lists/*  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN mkdir -p /app  
  
ADD nginx/nginx.conf /etc/nginx/nginx.conf  
  
ADD run.sh /app/run.sh  
  
RUN chmod +x /app/run.sh  
  
EXPOSE 80  
CMD ["/app/run.sh"]  

