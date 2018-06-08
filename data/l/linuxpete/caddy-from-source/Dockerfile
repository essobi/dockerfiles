# Caddy server from source  
# Inspired by  
# * https://hub.docker.com/r/sapk/caddy/  
# * https://hub.docker.com/r/abiosoft/caddy/  
FROM golang:alpine  
LABEL caddy_version="dev" architecture="amd64"  
  
RUN apk -U --no-progress upgrade \  
&& apk -U --force --no-progress add git \  
&& git clone https://github.com/mholt/caddy.git /go/src/github.com/mholt/caddy
\  
&& cd /go/src/github.com/mholt/caddy \  
&& git config --global user.email "caddy@caddyserver.com" \  
&& git config --global user.name "caddy" \  
&& git fetch origin pull/1316/head:websocket \  
&& git checkout websocket \  
&& git rebase origin/master \  
&& cd /go \  
&& go get -v ... \  
&& mv /go/bin/caddy /usr/bin \  
&& apk del --purge git \  
&& rm -rf $GOPATH /var/cache/apk/*  
  
WORKDIR /srv  
COPY Caddyfile /etc/Caddyfile  
COPY index.html /srv/index.html  
  
EXPOSE 80 443 2015  
VOLUME ["/root/.caddy"]  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]  

