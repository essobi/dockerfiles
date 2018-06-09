FROM alpine:latest AS build  
  
RUN apk add --no-cache wget ca-certificates && \  
wget -q -O caddy.tar.gz
https://caddyserver.com/download/linux/amd64?license=personal && \  
tar -xzf caddy.tar.gz  
  
FROM alpine:latest  
LABEL maintainer="Denis Ivanov"  
  
RUN apk add --no-cache ca-certificates && \  
mkdir -p /srv/caddy && \  
mkdir -p /srv/project  
  
WORKDIR /srv/  
  
COPY \--from=build /caddy .  
RUN chmod u+x caddy  
  
EXPOSE 80 443 2015  
ENTRYPOINT [ "/srv/caddy" ]  

