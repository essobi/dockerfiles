FROM alpine:3.6  
ARG plugins=tls.dns.route53  
ARG version=0.10.6  
ENV CADDYPATH=/certs  
RUN mkdir /certs  
VOLUME /certs  
  
RUN apk add --no-cache curl && \  
curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/linux/amd64?plugins=${plugins}" | \  
tar --no-same-owner -C /usr/bin/ -xz caddy && \  
chmod 0755 /usr/bin/caddy  
  
EXPOSE 80 443 2015  
COPY Caddyfile /etc/Caddyfile  
  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]  

