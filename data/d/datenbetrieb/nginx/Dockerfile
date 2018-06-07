# DOCKER-VERSION 1.0.0  
FROM datenbetrieb/debian:jessie  
MAINTAINER Peter Niederlag "peter.niederlag@datenbetrieb.de"  
RUN apt-get update && \  
apt-get install -y nginx-full && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
ADD nginx.conf /etc/nginx/  
  
#RUN rm /etc/nginx/sites-enabled/default  
#RUN echo "upstream php-upstream { server php:9000; }" >
/etc/nginx/conf.d/upstream.conf  
# make www-data use the uid 1000, makes interop with perms more easy  
RUN usermod -u 1000 www-data  
  
# PORTS  
EXPOSE 80  
EXPOSE 443  
#ENTRYPOINT ["entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

