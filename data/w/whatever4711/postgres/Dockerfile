FROM alpine:edge  
  
# grab gosu for easy step-down from root  
ENV ARCH=amd64 \  
GOSU_VERSION=1.4 \  
LANG=en_US.utf8 \  
PGDATA=/var/lib/postgresql/data  
  
ADD docker-entrypoint.sh /entrypoint.sh  
RUN apk add --update --no-cache \  
postgresql curl bash tini && \  
curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$ARCH" &&
\  
chmod +x /usr/local/bin/gosu && \  
apk del curl && \  
rm -rf /var/cache/apk/* && \  
chmod +x /entrypoint.sh  
  
VOLUME $PGDATA  
  
ENTRYPOINT [ "/sbin/tini", "--", "/entrypoint.sh" ]  
  
EXPOSE 5432  
CMD [ "postgres" ]  
  
COPY healthcheck.sh /usr/local/bin/  
HEALTHCHECK \--interval=30s --timeout=5s --retries=3 \  
CMD ["healthcheck.sh"]  
  
LABEL \  
maintainer=whatever4711@gmail.com \  
version=9.5.6 \  
os="linux" \  
arch="${ARCH}"  

