  
FROM alpine:edge  
  
ARG BUILD_DATE  
ARG BUILD_VERSION  
ARG BUILD_TYPE  
ARG COLLECTD_VERSION  
  
EXPOSE 2003  
  
ENV \  
TZ='Europe/Berlin'  
  
LABEL \  
version=${BUILD_VERSION} \  
maintainer="Bodo Schulz <bodo@boone-schulz.de>" \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.name="Collectd Docker Image" \  
org.label-schema.description="Inofficial Collectd Docker Image" \  
org.label-schema.url="https://collectd.org" \  
org.label-schema.vcs-url="https://github.com/bodsch/docker-collectd" \  
org.label-schema.vendor="Bodo Schulz" \  
org.label-schema.version=${COLLECTD_VERSION} \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile" \  
com.microscaling.license="Unlicense"  
#
---------------------------------------------------------------------------------------  
  
RUN \  
echo 'hosts: files dns' >> /etc/nsswitch.conf && \  
apk update --quiet --no-cache && \  
apk upgrade --quiet --no-cache && \  
apk add --quiet --no-cache \  
collectd \  
collectd-apache \  
collectd-bind \  
collectd-curl \  
collectd-disk \  
collectd-dns \  
collectd-iptables \  
collectd-lvm \  
collectd-mysql \  
collectd-network \  
collectd-nginx \  
collectd-ping \  
collectd-postgresql \  
collectd-python\  
collectd-redis \  
collectd-sensors \  
collectd-utils \  
collectd-virt \  
collectd-write_redis \  
collectd-write_http \  
tzdata && \  
version=$(collectd -h | grep "http://collectd" | awk -F ',' '{print $1}') && \  
echo "installed version: ${version}" && \  
cp /usr/share/zoneinfo/${TZ} /etc/localtime && \  
echo ${TZ} > /etc/timezone && \  
mv /etc/collectd/collectd.conf /etc/collectd/collectd.conf-DIST && \  
rm -rf \  
/tmp/* \  
/var/cache/apk/*  
  
COPY rootfs/ /  
  
ENTRYPOINT ["/init/run.sh"]  
  
CMD ["collectd","-f"]  

