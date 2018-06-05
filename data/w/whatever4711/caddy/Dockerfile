FROM alpine:edge  
  
ENV arch=amd64 \  
url="https://caddyserver.com/download/build?" \  
params="&features=git%2Chugo%2Cipfilter%2Cmailout%2Cprometheus%2Crealip%2Csearch"  
RUN apk add --update --no-cache ca-certificates tini git libressl libcap curl
&& \  
mkdir /caddysrc && CADDYARCH=$(echo "${arch}" | sed -e "s/armhf/arm/g" -e
"s/aarch64/arm/g") && \  
curl -sL -o /caddysrc/caddy_linux_arm.tar.gz
"${url}os=linux&arch=${CADDYARCH}${params}" && \  
tar -xf /caddysrc/caddy_linux_arm.tar.gz -C /caddysrc && \  
mv /caddysrc/caddy /usr/sbin/caddy && \  
chmod 755 /usr/sbin/caddy && \  
rm -rf /caddysrc && \  
apk del curl && \  
rm -rf /var/cache/apk/* && \  
adduser -Du 1000 caddy && \  
mkdir -p /home/caddy/logs /home/caddy/srv /home/caddy/.caddy/acme && \  
chown -R caddy:caddy /home/caddy && \  
setcap 'cap_net_bind_service=+ep' /usr/sbin/caddy && \  
printf "localhost:80" > /home/caddy/Caddyfile  
  
EXPOSE 80 443 2015  
USER caddy  
WORKDIR /home/caddy/srv  
  
ENTRYPOINT ["tini", "--", "caddy"]  
CMD ["--agree", "--conf", "/home/caddy/Caddyfile"]  
  
LABEL \  
maintainer="whatever4711@gmail.com" \  
version=0.9.5 \  
os="linux" \  
arch="${arch}"  

