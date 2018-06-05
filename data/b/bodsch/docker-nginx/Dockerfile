  
FROM alpine:3.7  
  
ENV \  
TERM=xterm \  
BUILD_DATE="2018-05-04" \  
NGINX_VERSION="1.12.2" \  
TZ='Europe/Berlin'  
  
EXPOSE 80 443  
  
LABEL \  
version="1805" \  
maintainer="Bodo Schulz <bodo@boone-schulz.de>" \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.name="NginX Docker Image" \  
org.label-schema.description="Inofficial NginX Docker Image" \  
org.label-schema.url="https://nginx.org" \  
org.label-schema.vcs-url="https://github.com/bodsch/docker-nginx" \  
org.label-schema.vendor="Bodo Schulz" \  
org.label-schema.version=${NGINX_VERSION} \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile" \  
com.microscaling.license="GNU General Public License v3.0"  
#
---------------------------------------------------------------------------------------  
  
RUN \  
apk update --quiet --no-cache && \  
apk upgrade --quiet --no-cache && \  
apk add --quiet --no-cache \  
curl nginx tzdata && \  
cp /usr/share/zoneinfo/${TZ} /etc/localtime && \  
echo ${TZ} > /etc/timezone && \  
mkdir -p \  
/etc/nginx/secure \  
/etc/nginx/external \  
/var/log/nginx/ \  
/run/nginx \  
/var/cache/nginx/body \  
/var/cache/nginx/proxy && \  
chown -R nginx:nginx /var/cache/nginx && \  
rm -rf \  
/tmp/* \  
/var/cache/apk/*  
  
COPY rootfs/ /  
  
VOLUME [ "/etc/nginx" ]  
WORKDIR "/etc/nginx"  
  
HEALTHCHECK \  
\--interval=5s \  
\--timeout=2s \  
\--retries=12 \  
CMD curl --silent --fail http://localhost/health || exit 1  
  
ENTRYPOINT [ "/init/run.sh" ]  
  
CMD [ "/usr/sbin/nginx" ]  
  
#
---------------------------------------------------------------------------------------  

