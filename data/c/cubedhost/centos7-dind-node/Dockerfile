FROM cubedhost/centos7-node  
  
ENV DOCKER_CHANNEL stable  
ENV DOCKER_VERSION 17.03.2-ce  
  
# Docker deps  
RUN set -ex; \  
yum -y install \  
btrfs-progs \  
e2fsprogs \  
e2fsprogs-extra \  
iptables \  
xfsprogs \  
xz \  
ca-certificates \  
curl \  
tar \  
libressl \  
# Additional deps  
rsync \  
wget \  
which  
  
RUN set -ex; \  
export DOCKER_ARCH=$(arch); \  
curl -fL -o docker.tgz
"https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${DOCKER_ARCH}/docker-${DOCKER_VERSION}.tgz"
&& \  
tar xvf docker.tgz \  
\--strip-components 1 \  
\--directory /usr/local/bin/ && \  
rm docker.tgz; \  
dockerd -v; \  
docker -v  
  
# set up subuid/subgid so that "--userns-remap=default" works out-of-the-box  
RUN set -ex \  
&& groupadd dockremap \  
&& useradd -g dockremap dockremap \  
&& echo 'dockremap:165536:65536' >> /etc/subuid \  
&& echo 'dockremap:165536:65536' >> /etc/subgid  
  
ENV DIND_COMMIT 3b5fac462d21ca164b3778647420016315289034  
  
RUN set -ex; \  
wget -O /usr/local/bin/dind
"https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind" &&
\  
chmod +x /usr/local/bin/dind  
  
COPY dockerd-entrypoint.sh /usr/local/bin/  
RUN set -ex ;\  
chmod +x /usr/local/bin/dockerd-entrypoint.sh  
  
VOLUME /var/lib/docker  
EXPOSE 2375  
ENTRYPOINT ["dockerd-entrypoint.sh"]  
CMD []  

