FROM alpine  
LABEL maintainer="contact-docker@mo-mar.de"  
  
ADD Caddyfile /data/Caddyfile  
  
RUN apk add --no-cache git jq go musl-dev libcap &&\  
wget -qO-
https://gist.githubusercontent.com/moqmar/ba77bd778e6ebc956eaa36388be3fcdd/raw
| sh -s http.realip http.ipfilter http.cors http.expires http.ratelimit &&\  
setcap 'cap_net_bind_service=+ep' /usr/local/bin/caddy && mkdir -p
/caddy/public && chmod 777 /caddy /caddy/public &&\  
apk del git jq go musl-dev libcap  
  
ADD smell-baron /  
  
EXPOSE 80/tcp  
EXPOSE 443/tcp  
WORKDIR /data  
  
USER 1000  
ENV CADDYPATH /caddy  
  
CMD ["/smell-baron", "/usr/local/bin/caddy", "-agree=true",
"-conf=/data/Caddyfile", "-root=/var/tmp", "-log=stdout", "-email=",
"-grace=1s"]  

