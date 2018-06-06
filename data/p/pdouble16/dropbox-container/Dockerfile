FROM alpine:3.7  
MAINTAINER Patrick Double <pat@patdouble.com>  
  
ARG BUILD_DATE  
ARG SOURCE_COMMIT  
ARG DOCKERFILE_PATH  
ARG SOURCE_TYPE  
ARG VERSION=45.4.92  
#########################################  
## ENVIRONMENTAL CONFIG ##  
#########################################  
# Set correct environment variables  
ENV HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"
TERM=dumb GLIBC_VERSION=2.23-r4  
  
# Use baseimage-docker's init system  
# CMD ["/sbin/my_init"]  
# Use Supervisor  
CMD ["supervisord", "-c", "/etc/supervisor.conf", "-n"]  
  
#########################################  
## RUN INSTALL SCRIPT ##  
#########################################  
  
COPY * /tmp/  
RUN apk add --no-cache libstdc++ curl ca-certificates bash supervisor shadow
python2 glib && \  
for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION}
glibc-i18n-${GLIBC_VERSION}; do curl -sSL https://github.com/andyshinn/alpine-
pkg-glibc/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk;
done && \  
apk add --allow-untrusted /tmp/*.apk && \  
rm -v /tmp/*.apk && \  
( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true ) && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
# https://github.com/moby/moby/issues/9547  
chmod +x /tmp/install.sh && sleep 3s && /tmp/install.sh && \  
apk del curl glibc-i18n && \  
rm -rf /tmp/* /var/cache/apk/*  
  
  
#########################################  
## EXPORTS AND VOLUMES ##  
#########################################  
  
VOLUME /home/.dropbox /home/Dropbox  
  
HEALTHCHECK CMD test -e /proc/$(</home/.dropbox/dropbox.pid) || exit 1  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="$DOCKERFILE_PATH/Dockerfile" \  
org.label-schema.license="GPLv2" \  
org.label-schema.name="Dropbox ${VERSION}" \  
org.label-schema.vendor="https://bitbucket.org/double16" \  
org.label-schema.url="https://bitbucket.org/double16/dropbox-container" \  
org.label-schema.vcs-ref=$SOURCE_COMMIT \  
org.label-schema.vcs-type="$SOURCE_TYPE" \  
org.label-schema.vcs-url="https://bitbucket.org/double16/dropbox-
container.git"  

