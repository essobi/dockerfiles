FROM wodby/alpine:latest as builder  
# to retrieve gotpl program used in docker-entrypoint.sh  
FROM traefik:alpine  
  
COPY \--from=builder /usr/local/bin/gotpl /usr/local/bin  
  
RUN set -xe && \  
apk add --update --no-cache \  
bash\  
apache2-utils  
  
RUN mkdir /etc/gotpl/  
RUN mkdir /var/traefik/  
  
COPY ./docker-entrypoint.sh /usr/local/bin/  
COPY ./traefik.toml.tpl /etc/gotpl/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
#CMD ["traefik"]  

