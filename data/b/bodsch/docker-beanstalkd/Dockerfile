  
FROM alpine:latest  
  
ARG BUILD_DATE  
ARG BUILD_VERSION  
ARG BUILD_TYPE  
ARG BEANSTALKD_VERSION  
  
  
ENV \  
TZ='Europe/Berlin'  
EXPOSE 11300  
LABEL \  
version=${BUILD_VERSION} \  
maintainer="Bodo Schulz <bodo@boone-schulz.de>" \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.name="beanstalkd Docker Image" \  
org.label-schema.description="Inofficial beanstalkd Docker Image" \  
org.label-schema.url="http://kr.github.io/beanstalkd/" \  
org.label-schema.vcs-url="https://github.com/bodsch/docker-beanstalkd" \  
org.label-schema.vendor="Bodo Schulz" \  
org.label-schema.version=${BEANSTALKD_VERSION} \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile" \  
com.microscaling.license="GNU General Public License v3.0"  
  
#
---------------------------------------------------------------------------------------  
RUN \  
apk update --quiet --no-cache && \  
apk upgrade --quiet --no-cache && \  
apk add --quiet --no-cache --virtual .build-deps \  
build-base git tzdata && \  
cp /usr/share/zoneinfo/${TZ} /etc/localtime && \  
echo ${TZ} > /etc/timezone && \  
cd /tmp && \  
git clone https://github.com/kr/beanstalkd.git && \  
cd beanstalkd && \  
if [ "${BUILD_TYPE}" == "stable" ] ; then \  
echo "switch to stable Tag v${BEANSTALKD_VERSION}" && \  
git checkout tags/v${BEANSTALKD_VERSION} 2> /dev/null ; \  
fi && \  
sed -i 's,sys/fcntl.h,fcntl.h,' sd-daemon.c && \  
make && \  
mv beanstalkd /usr/bin/ && \  
mkdir /var/cache/beanstalkd && \  
/usr/bin/beanstalkd -v && \  
apk del --quiet .build-deps && \  
rm -rf \  
/tmp/* \  
/var/cache/apk/  
  
HEALTHCHECK \  
\--interval=5s \  
\--timeout=2s \  
\--retries=12 \  
CMD ps ax | grep -v grep | grep -c beanstalkd || exit 1  
  
COPY rootfs/ /  
  
VOLUME [ "/var/cache/beanstalkd" ]  
  
ENTRYPOINT ["/init/run.sh"]  
  
CMD ["beanstalkd", "-b", "/var/cache/beanstalkd", "-f", "0", "-VV"]  

