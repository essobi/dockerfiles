FROM alpine:3.6  
RUN apk add --no-cache wget ca-certificates  
ADD caddy.sh /usr/bin/caddy.sh  
RUN wget -O /usr/bin/caddy https://file.dengqi.org/caddy/caddy && mkdir -p
/data && chmod a+x /usr/bin/caddy && chmod a+x /usr/bin/caddy.sh  
ADD Caddyfile /Caddyfile  
  
EXPOSE 80  
CMD ["/usr/bin/caddy.sh"]  

