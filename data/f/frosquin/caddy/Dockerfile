FROM alpine:3.2  
MAINTAINER frank.rosquin@gmail.com  
  
ENV VERSION "0.9.1"  
ENV FEATURES
"git,ipfilter,cors,search,hugo,prometheus,realip,jwt,mailout,filemanager,locale,mailout,minify"  
LABEL net.nullsense.caddy.version="${VERSION}" architecture="amd64"
net.nullsense.caddy.features="${FEATURES}"  
  
RUN apk add --update openssh-client git tar  
  
RUN mkdir /caddysrc \  
&& curl -sL -o /caddysrc/caddy_linux_amd64.tar.gz
"http://caddyserver.com/download/build?os=linux&arch=amd64&features=${FEATURES}"
\  
&& tar -xzf /caddysrc/caddy_linux_amd64.tar.gz -C /caddysrc \  
&& mv /caddysrc/caddy /usr/bin/caddy \  
&& chmod 755 /usr/bin/caddy \  
&& rm -rf /caddysrc \  
&& printf "0.0.0.0\ngzip\nroot /srv" > /etc/Caddyfile  
  
RUN mkdir /srv \  
&& echo "<h1>Hello from Caddy!</h1>" > /srv/index.html  
  
EXPOSE 2015  
EXPOSE 443  
EXPOSE 80  
WORKDIR /srv  
  
ENTRYPOINT ["/usr/bin/caddy", "-log=stderr"]  
CMD ["--conf", "/etc/Caddyfile"]  

