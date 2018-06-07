FROM base/archlinux  
  
MAINTAINER Kai Hendry <hendry@iki.fi>  
  
RUN pacman --noconfirm -Sy archlinux-keyring && pacman -q -Syu --noconfirm php
php-fpm texlive-bin texlive-core  
  
RUN update-ca-trust  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/build?os=linux&arch=amd64&features=git" \  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version  
  
ADD www /srv/  
  
EXPOSE 80 443 2015  
ADD Caddyfile /etc/Caddyfile  
  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile"]  

