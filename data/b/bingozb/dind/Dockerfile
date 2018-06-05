FROM alpine:3.7  
MAINTAINER bingo <bingov5@icloud.com>  
  
RUN apk add --no-cache \  
ca-certificates  
  
RUN [ ! -e /etc/nsswitch.conf ] && echo 'hosts: files dns' >
/etc/nsswitch.conf  
  
ENV DOCKER_CHANNEL edge  
ENV DOCKER_VERSION 18.02.0-ce  
ENV DOCKER_HOST_ADDRESS "docker:2375"  
ENV DOCKER_HOST "tcp://$DOCKER_HOST_ADDRESS"  
RUN set -ex; \  
apk add --no-cache --virtual .fetch-deps \  
curl \  
tar \  
; \  
\  
apkArch="$(apk --print-arch)"; \  
case "$apkArch" in \  
x86_64) dockerArch='x86_64' ;; \  
armhf) dockerArch='armel' ;; \  
aarch64) dockerArch='aarch64' ;; \  
ppc64le) dockerArch='ppc64le' ;; \  
s390x) dockerArch='s390x' ;; \  
*) echo >&2 "error: unsupported architecture ($apkArch)"; exit 1 ;;\  
esac; \  
\  
if ! curl -fL -o docker.tgz
"https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${dockerArch}/docker-${DOCKER_VERSION}.tgz";
then \  
echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from
'${DOCKER_CHANNEL}' for '${dockerArch}'"; \  
exit 1; \  
fi; \  
\  
tar --extract \  
\--file docker.tgz \  
\--strip-components 1 \  
\--directory /usr/local/bin/ \  
; \  
rm docker.tgz; \  
\  
apk del .fetch-deps; \  
\  
dockerd -v; \  
docker -v  
  
RUN set -eux; \  
apk add --no-cache \  
btrfs-progs \  
e2fsprogs \  
e2fsprogs-extra \  
iptables \  
xfsprogs \  
xz \  
pigz \  
; \  
if zfs="$(apk info --no-cache --quiet zfs)" && [ -n "$zfs" ]; then \  
apk add --no-cache zfs; \  
fi  
  
RUN set -x \  
&& addgroup -S dockremap \  
&& adduser -S -G dockremap dockremap \  
&& echo 'dockremap:165536:65536' >> /etc/subuid \  
&& echo 'dockremap:165536:65536' >> /etc/subgid  
  
ENV DIND_COMMIT 3b5fac462d21ca164b3778647420016315289034  
  
RUN set -ex; \  
apk add --no-cache --virtual .fetch-deps libressl; \  
wget -O /usr/local/bin/dind
"https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind"; \  
chmod +x /usr/local/bin/dind; \  
apk del .fetch-deps  
  
COPY dockerd-entrypoint.sh /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/dockerd-entrypoint.sh  
  
VOLUME /var/lib/docker  
EXPOSE 2375  
ENTRYPOINT ["dockerd-entrypoint.sh"]

