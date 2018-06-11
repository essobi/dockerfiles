FROM alpine  
  
ENV S6v=v1.19.1.1  
ENV LIBC=2.26-r0  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk upgrade --no-cache && \  
apk add --no-cache libressl ca-certificates curl coreutils bash s6-rc
s6-linux-utils s6-portable-utils dropbear && \  
mkdir -p /etc/dropbear && \  
mv /usr/bin/s6-* /bin/ && \  
curl -sOL https://github.com/just-
containers/s6-overlay/releases/download/${S6v}/s6-overlay-amd64.tar.gz && \  
tar xf s6-overlay-amd64.tar.gz -C /tmp && rm s6-overlay-amd64.tar.gz && \  
cp -a /tmp/etc /tmp/init /tmp/usr / && \  
echo '' > /etc/s6/init/init-stage2-fixattrs.txt && \  
rm -rf /tmp/* && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${LIBC}/glibc-${LIBC}.apk && \  
apk add glibc-${LIBC}.apk && rm -f glibc-${LIBC}.apk && \  
mkdir -p /sys /proc /dev  
  
COPY s6-hiercopy /bin/s6-hiercopy  
COPY pre-init.sh /pre-init.sh  
COPY services.d /etc/services.d  
COPY cont-init.d /etc/cont-init.d  
  
RUN chmod g=u -R $(ls -d /* | grep -Ev "dev|proc|sys") && \  
chmod g=u /dev /proc &>/dev/null  
  
CMD ["/pre-init.sh"]  

