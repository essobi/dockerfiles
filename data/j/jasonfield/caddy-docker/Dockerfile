FROM alpine:3.7  
LABEL maintainer="Xorima"  
  
ENV CADDY_VERSION 'v0.10.12'  
ENV CADDYPATH=/data/caddy/ssl/  
ENV CADDY_EMAIL='example@example.org'  
RUN apk add --no-cache curl  
  
ADD
https://github.com/mholt/caddy/releases/download/${CADDY_VERSION}/caddy_${CADDY_VERSION}_linux_amd64.tar.gz
/tmp/caddy/  
RUN tar -xvzf /tmp/caddy/caddy_${CADDY_VERSION}_linux_amd64.tar.gz -C
/tmp/caddy  
  
COPY Caddyfile /data/caddy/Caddyfile  
  
RUN mkdir -pv /data/caddy/ssl  
RUN mv /tmp/caddy/caddy /usr/bin/caddy  
  
CMD ["sh", "-c", "/usr/bin/caddy -conf=/data/caddy/Caddyfile -email
${CADDY_EMAIL} -agree"]

