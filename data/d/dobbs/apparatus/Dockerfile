FROM alpine:3.5 as caddy  
RUN apk add --no-cache openssh-client tar curl libcap \  
&& curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" \  
-o - \  
"https://caddyserver.com/download/linux/amd64" \  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& setcap 'cap_net_bind_service=+ep' /usr/bin/caddy  
  
FROM node:4-slim as apparatus  
COPY . /apparatus  
WORKDIR /apparatus  
RUN npm install \  
&& npm run build  
  
FROM alpine:3.5  
COPY \--from=caddy /usr/bin/caddy /usr/bin/caddy  
RUN addgroup -S -g 8888 apparatus \  
&& adduser -S -u 8888 -D -H apparatus \  
&& mkdir -p /src/vendor /src/dist /src/examples /src/saves  
WORKDIR /src  
COPY \--from=apparatus /apparatus/index.html .  
COPY \--from=apparatus /apparatus/doc/examples/* examples/  
COPY \--from=apparatus /apparatus/vendor/* vendor/  
COPY \--from=apparatus /apparatus/dist/* dist/  
RUN chown -R apparatus:apparatus /src  
USER apparatus  
EXPOSE 2015  
VOLUME ["/src/saves"]  
CMD ["caddy", "browse", "log stdout", "errors stdout"]  

