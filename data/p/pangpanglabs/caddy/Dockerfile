FROM alpine:3.5  
RUN apk add --no-cache bash tar curl  
  
# install caddy  
RUN curl https://getcaddy.com | bash -s jwt,git  
  
EXPOSE 80 443 2015  
COPY Caddyfile /etc/Caddyfile  
  
ENTRYPOINT ["/usr/local/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]  

