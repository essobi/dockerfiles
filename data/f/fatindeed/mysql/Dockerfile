FROM alpine  
  
ARG ALPINE_MIRROR  
ARG TIMEZONE=Asia/Shanghai  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL maintainer="James Zhu <fatindeed at hotmail dot com>" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="MySQL:alpine" \  
org.label-schema.description="MySQL Docker image based on Alpine Linux" \  
org.label-schema.url="https://hub.docker.com/r/fatindeed/mysql/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/fatindeed/docker-mysql" \  
org.label-schema.vendor="James Zhu" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN set -xe; \  
chmod a+x /usr/local/bin/*; \  
addgroup -S mysql; \  
adduser -D -S -G mysql mysql; \  
# Switch to a mirror if given  
if [ -n "$ALPINE_MIRROR" ]; then \  
ALPINE_MIRROR=${ALPINE_MIRROR//\//\\\\\/}; \  
sed -i "s/http:\/\/dl-cdn.alpinelinux.org/$ALPINE_MIRROR/g"
/etc/apk/repositories; \  
fi; \  
apk add \--no-cache tzdata mysql; \  
# Setup timezone  
if [ -n "$TIMEZONE" ]; then \  
cp "/usr/share/zoneinfo/$TIMEZONE" /etc/localtime; \  
echo "$TIMEZONE" > /etc/timezone; \  
fi; \  
# Setup MySQL  
mkdir -p /var/lib/mysql /run/mysqld /etc/mysql/conf.d; \  
chown -R mysql:mysql /var/lib/mysql /run/mysqld; \  
echo "[mysqld]\nskip-host-cache\nskip-name-resolve" >
/etc/mysql/conf.d/docker.cnf; \  
# Delete packages  
apk del --purge tzdata  
  
VOLUME ["/var/lib/mysql"]  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld", "--user=mysql", "--console"]  

