FROM alpine:3.4  
MAINTAINER Dave Henderson <dhenderson@gmail.com>  
  
RUN apk add --no-cache tar curl  
  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/build?os=linux&arch=amd64&features=minify" \  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version  
  
EXPOSE 80 443  
WORKDIR /srv  
  
COPY Caddyfile /etc/Caddyfile  
COPY index.md /srv/index.md  
COPY *.html /srv/  
  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile"]  

