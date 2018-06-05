FROM debian:stretch-slim  
  
MAINTAINER wilkesystems <maintainer@wilke.systems>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update; \  
apt-get install -y ca-certificates locales locales-all nginx-extras openssl
ssl-cert; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; \  
ln -sf /dev/stdout /var/log/nginx/access.log; \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
COPY ["docker-entrypoint.sh", "/usr/bin/docker-entrypoint.sh"]  
  
WORKDIR /var/www  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]

