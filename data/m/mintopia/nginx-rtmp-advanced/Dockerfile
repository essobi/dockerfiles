FROM alpine:latest  
MAINTAINER Jessica Smith <jess@mintopia.net>  
  
RUN apk update && \  
apk add \  
openssl \  
libstdc++ \  
ca-certificates \  
pcre \  
bash  
  
ADD nginx.tar.gz /opt/  
ADD nginx.conf /opt/nginx/conf/nginx.conf  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh  
  
EXPOSE 1935  
EXPOSE 8080  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["/opt/nginx/sbin/nginx", "-g", "daemon off;"]  

