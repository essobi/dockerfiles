FROM pipill/armhf-alpine:3.5  
LABEL maintainer "Abiola Ibrahim <abiola89@gmail.com>"  
  
LABEL caddy_version="0.10.3" architecture="arm7"  
  
ARG plugins=http.git  
  
RUN [ "cross-build-start" ]  
  
RUN apk add --no-cache openssh-client git tar curl  
  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/linux/arm7?plugins=${plugins}" \  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version  
  
EXPOSE 80 443 2015  
VOLUME /root/.caddy  
WORKDIR /srv  
  
COPY Caddyfile /etc/Caddyfile  
COPY index.html /srv/index.html  
  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]  
  
RUN [ "cross-build-end" ]  

