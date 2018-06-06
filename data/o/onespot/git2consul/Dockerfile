FROM alpine:3.5  
MAINTAINER Richard Bolkey <https://github.com/rbolkey>  
  
# Need testing in order to use gosu
https://pkgs.alpinelinux.org/packages?name=gosu  
RUN addgroup -g 1001 git2consul && \  
adduser -u 1000 -S -G git2consul git2consul && \  
echo http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories &&
\  
apk --update add bash nodejs git openssh ca-certificates gosu dumb-init
sshpass perl && \  
rm -rf /var/cache/apk/* && \  
npm install git2consul@0.12.13 --global && \  
mkdir -p /etc/git2consul.d  
  
COPY docker-entrypoint.sh /usr/local/bin  
  
WORKDIR /home/git2consul  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["git2consul"]  

