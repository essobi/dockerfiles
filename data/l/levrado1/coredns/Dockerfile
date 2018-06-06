# Originally taken from Yorick Poels's dockerfile [yorickps/docker-coredns]  
# Adding a default config with health plugin, and removing volumization  
FROM alpine:3.7  
LABEL maintainer="Lev Radomislensky <lev.radomislensky@gmail.com"  
  
ENV COREDNS_VERSION=1.0.6  
RUN set -xe &&\  
apk add --no-cache bind-tools ca-certificates openssl curl dumb-init &&\  
update-ca-certificates  
  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://github.com/coredns/coredns/releases/download/v${COREDNS_VERSION}/coredns_${COREDNS_VERSION}_linux_amd64.tgz"
\  
| tar --no-same-owner -C /usr/bin/ -xz coredns &&\  
rm -rf /var/cache/apk/* &&\  
chmod 0755 /usr/bin/coredns &&\  
/usr/bin/coredns -version  
  
EXPOSE 53 53/udp  
  
COPY ./config/Corefile-proxy-example /etc/coredns/Corefile  
  
ENTRYPOINT ["dumb-init"]  
  
CMD ["/usr/bin/coredns", "-conf", "/etc/coredns/Corefile"]  

