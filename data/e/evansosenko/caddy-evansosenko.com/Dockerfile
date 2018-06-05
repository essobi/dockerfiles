FROM alpine  
  
MAINTAINER Evan Sosenko <razorx@evansosenko.com>  
  
RUN apk add --update \  
curl \  
tar \  
openssh-client \  
git \  
&& rm -rf /var/cache/apk/*  
  
RUN curl --silent --show-error --fail --location \  
\--header \  
"Accept: application/tar+gzip, application/x-gzip, application/octet-stream" \  
-o - \  
"https://caddyserver.com/download/build?os=linux&arch=amd64&features=git" \  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version  
  
EXPOSE 80 443  
VOLUME /root/.caddy  
  
COPY Caddyfile /etc/Caddyfile  
COPY Caddyfile.default /etc/Caddyfile.default  
COPY Caddyfile.csp /etc/Caddyfile.csp  
  
WORKDIR /srv  
  
ENTRYPOINT ["/usr/bin/caddy"]  
  
CMD ["--conf", "/etc/Caddyfile"]  

