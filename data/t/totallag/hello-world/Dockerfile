FROM alpine:edge  
MAINTAINER Chris Phan <phanx068@gmail.com>  
  
# Add s6-overlay  
ENV S6_OVERLAY_VERSION=v1.18.1.5  
  
RUN apk add --update --no-cache git tzdata musl && \  
apk --no-cache add --virtual devs tar curl && \  
adduser -Du 1000 caddy && \  
curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz \  
| tar xfz - -C / && \  
curl
"https://caddyserver.com/download/build?os=linux&arch=amd64&features=DNS%2Cawslambda%2Ccors%2Cexpires%2Cfilemanager%2Cgit%2Chugo%2Cipfilter%2Cjsonp%2Cjwt%2Clocale%2Cmailout%2Cminify%2Cmultipass%2Cprometheus%2Cratelimit%2Crealip%2Csearch%2Cupload%2Ccloudflare%2Cdigitalocean%2Cdnsimple%2Cdyn%2Cgandi%2Cgooglecloud%2Clinode%2Cnamecheap%2Crfc2136%2Croute53%2Cvultr"
\  
| tar --no-same-owner -C /usr/bin/ -xz caddy && \  
apk del devs tar curl  
  
COPY rootfs/ /  
  
USER caddy  
  
ENTRYPOINT ["/init"]  
  
CMD ["caddy", "\--conf", "/etc/Caddyfile","-ca","https://acme-
staging.api.letsencrypt.org/directory"]

