FROM registry:2  
MAINTAINER Roberto Aguilar <roberto.c.aguilar@gmail.com>  
  
RUN apk update && apk add apache2-utils bash openssl  
  
ADD files/ /  
RUN chmod +x /usr/local/bin/* /registry-entrypoint.sh  
  
ADD compose/docker-compose.yml /  
  
RUN mkdir -p /auth && touch /auth/htpasswd  
  
VOLUME /auth  
VOLUME /certs  
  
ENTRYPOINT ["/registry-entrypoint.sh"]  
  
# same CMD from upstream registry image  
# https://github.com/docker/distribution-library-
image/blob/576b139d6eac5b35c9b3e9fe6c2e5132b0c7e03b/Dockerfile  
CMD ["/etc/docker/registry/config.yml"]  

