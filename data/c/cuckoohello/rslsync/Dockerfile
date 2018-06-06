FROM alpine  
ENV GLIBC_VERSION 2.25-r0  
ENV SYNC_USER rslsync  
ENV UID 1000  
RUN apk add --update --no-cache tzdata && cp /usr/share/zoneinfo/Asia/Shanghai
/etc/localtime && echo "Asia/Shanghai" > /etc/timezone && apk del tzdata  
  
RUN apk add --update --no-cache curl tar ca-certificates jq su-exec iptables
&& \  
curl -LOsS https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \  
curl -LsS -o /etc/apk/keys/sgerrand.rsa.pub
https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/sgerrand.rsa.pub && \  
apk add glibc-${GLIBC_VERSION}.apk && \  
rm /etc/apk/keys/sgerrand.rsa.pub glibc-${GLIBC_VERSION}.apk && \  
curl -LsS https://download-cdn.resilio.com/stable/linux-x64/resilio-
sync_x64.tar.gz | tar xzf - -C /usr/local/bin rslsync && \  
chmod +x /usr/local/bin/rslsync && \  
apk del curl tar ca-certificates  
  
EXPOSE 8080 55555 55555/udp  
  
COPY rslsync.conf /etc/  
COPY entrypoint.sh /  
COPY docker-compose.yml /  
RUN chmod +x /entrypoint.sh  
  
WORKDIR /data  
  
VOLUME /data  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["--config", "/etc/rslsync.conf", "--nodaemon"]  

