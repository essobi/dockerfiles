FROM alpine:3.4  
RUN apk --no-cache add curl ca-certificates git  
  
# ARG CADDY_VERSION=0.9.4  
ARG
CADDY_FEATURES=awslambda,cors,expires,filemanager,filter,git,hugo,ipfilter,jsonp,jwt,locale,mailout,minify,multipass,prometheus,ratelimit,realip,search,upload,cloudflare,digitalocean,dnsimple,dyn,gandi,googlecloud,linode,namecheap,ovh,rfc2136,route53,vultr  
  
RUN ARCH=$(apk --print-arch | sed 's/x86_64/amd64/') \  
&& curl -sfSL
"https://caddyserver.com/download/build?os=linux&arch=$ARCH&features=$CADDY_FEATURES"
\  
| tar -xz -C /tmp \  
&& mv /tmp/caddy /usr/bin/caddy \  
&& mkdir /var/www  
# FIXME! checksum  
COPY ./Caddyfile /etc/caddy/  
ENV CADDYPATH /var/lib/caddy  
  
VOLUME /etc/caddy  
VOLUME /var/lib/caddy  
VOLUME /var/www  
  
EXPOSE 80 443  
CMD ["caddy", "-conf", "/etc/caddy/Caddyfile"]  

