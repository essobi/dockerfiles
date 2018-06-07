FROM totem/nodejs-base:0.10.42  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update --fix-missing && \  
apt-get install -y git \  
openssh-client \  
iptables \  
lxc \  
aufs-tools && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
##SSH Folder for known_hosts  
RUN mkdir -p /root/.ssh && chmod 500 /root/.ssh && chown -R root:root
/root/.ssh  
  
# Install Docker  
# Docker version might be overridden in supervisord-wrapper if host and client
version are different  
RUN curl --fail -fsSLO
https://get.docker.com/builds/Linux/x86_64/docker-1.11.2.tgz \  
&& tar --strip-components=1 -xvzf docker-1.11.2.tgz -C /usr/local/bin  
  
ADD .docker/wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/docker /usr/local/bin/wrapdocker  
  
#Confd  
ENV CONFD_VERSION 0.6.2  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-${CONFD_VERSION}-linux-
amd64 -o /usr/local/bin/confd && \  
chmod 555 /usr/local/bin/confd  
  
#Etcdctl  
ENV ETCDCTL_VERSION v0.4.6  
RUN curl -L
https://github.com/coreos/etcd/releases/download/$ETCDCTL_VERSION/etcd-$ETCDCTL_VERSION-
linux-amd64.tar.gz -o /tmp/etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz && \  
cd /tmp && gzip -dc etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz | tar -xof - && \  
cp -f /tmp/etcd-$ETCDCTL_VERSION-linux-amd64/etcdctl /usr/local/bin && \  
rm -rf /tmp/etcd-$ETCDCTL_VERSION-linux-amd64 && \  
rm -rf /tmp/etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz  
  
#Supervisor Config  
RUN pip install supervisor==3.1.2 supervisor-stdout && \  
mkdir -p /var/log/supervisor  
ADD bin/supervisord-wrapper.sh /usr/sbin/supervisord-wrapper.sh  
RUN chmod +x /usr/sbin/supervisord-wrapper.sh && ln -sf
/etc/supervisor/supervisord.conf /etc/supervisord.conf  
  
#Confd Defaults  
ADD bin/confd-wrapper.sh /usr/sbin/confd-wrapper.sh  
RUN chmod +x /usr/sbin/confd-wrapper.sh  
  
#Custom Scripts  
ADD bin/decrypt-ssh-keys.sh /usr/local/bin/  
ADD bin/decrypt-docker-cfg.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/decrypt-ssh-keys.sh /usr/local/bin/decrypt-docker-
cfg.sh  
  
# Add update git timestamp script  
ADD bin/update-git-ts.sh /usr/local/bin/update-git-ts.sh  
RUN chmod +x /usr/local/bin/update-git-ts.sh  
  
WORKDIR /opt/image-factory  
  
# Configure GitHub  
RUN ssh-keyscan -H github.com | tee -a /root/.ssh/known_hosts && chmod -R 400
/root/.ssh/*  
  
# Install Image Factory  
ADD package.json /opt/image-factory/  
ADD npm-shrinkwrap.json /opt/image-factory/  
RUN set -e; cd /opt/image-factory; npm install --production; npm cache clean  
ADD . /opt/image-factory  
  
#Etc Config  
ADD etc /etc  
  
# Image Factory / Docker  
EXPOSE 8080  
VOLUME /var/lib/docker  
  
ENTRYPOINT ["/usr/sbin/supervisord-wrapper.sh"]  
CMD [""]  

