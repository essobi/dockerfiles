FROM alpine:3.5  
MAINTAINER Dallas Harris  
  
  
# This is the release of https://github.com/hashicorp/docker-base to pull in
order  
# to provide HashiCorp-built versions of basic utilities like dumb-init and
gosu.  
ENV DOCKER_BASE_VERSION=0.0.4  
ENV
DOCKER_BASE_SHA256SUM=5262aa8379782d42f58afbda5af884b323ff0b08a042e7915eb1648891a8da00  
  
# Set up certificates and our base tools.  
RUN apk add --no-cache ca-certificates openssl && \  
cd /tmp && \  
wget -O docker-base.zip https://releases.hashicorp.com/docker-
base/${DOCKER_BASE_VERSION}/docker-base_${DOCKER_BASE_VERSION}_linux_amd64.zip
&& \  
echo "${DOCKER_BASE_SHA256SUM} docker-base.zip" | sha256sum -c && \  
unzip -d / docker-base.zip && \  
rm docker-base.zip  
  
ENV PORT 22  
ENV RECONNECT_OPTIONS
reconnect,ServerAliveInterval=15,ServerAliveCountMax=20480  
ENV MOUNT_OPTIONS allow_other,StrictHostKeyChecking=no  
ENV MOUNTPOINT /mnt/sshfs-1  
RUN apk update && apk add sshfs && rm -rf /var/cache/apk/*  
RUN rm /sbin/halt /sbin/poweroff /sbin/reboot  
  
ADD entry.sh /usr/local/bin/entry.sh  
RUN chmod 755 /usr/local/bin/entry.sh  
  
HEALTHCHECK \--interval=5s --timeout=5s \  
CMD mountpoint -q $MOUNTPOINT || exit 1  
  
ENTRYPOINT ["/usr/local/bin/entry.sh"]  

