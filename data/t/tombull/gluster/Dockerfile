FROM tombull/confd:centos  
  
RUN yum --setopt=tsflags=nodocs -y update && \  
yum clean all && \  
yum --setopt=tsflags=nodocs -y install wget attr iputils iproute && \  
wget
http://download.gluster.org/pub/gluster/glusterfs/3.7/LATEST/EPEL.repo/glusterfs-
epel.repo -O /etc/yum.repos.d/glusterfs-epel.repo && \  
wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm && \  
rpm -ivh epel-release-7-5.noarch.rpm && \  
rm epel-release-7-5.noarch.rpm && \  
yum --setopt=tsflags=nodocs -y install glusterfs-server && \  
yum clean all && \  
systemctl enable rpcbind.service && \  
systemctl enable glusterd.service  
  
EXPOSE 111 24007 49152  
ENV GLUSTER_REPLICATION=2 \  
GLUSTER_VOLUME_NAME=gv0 \  
GLUSTER_LOCATION=/var/gluster/store \  
GLUSTER_PUBLIC_IP=1.1.1.1 \  
GLUSTER_PRIVATE_IP=1.1.1.1  
COPY docker-entrypoint.sh /  
COPY hosts.toml /etc/confd/conf.d  
COPY hosts.tmpl /etc/confd/templates/  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["confd"]  

