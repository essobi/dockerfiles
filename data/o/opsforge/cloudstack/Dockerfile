# Dockerfile of Apache CloudStack mgmt. server on Trusty  
FROM ubuntu:14.04  
MAINTAINER opsforge.io  
LABEL name="cloudstack"  
LABEL version="0.8.0"  
  
ENV mysqlpass 'Standard1'  
USER root  
  
EXPOSE 8080  
VOLUME ["/export"]  
  
RUN apt-get update && \  
apt-get install openntpd wget dnsutils curl nfs-kernel-server openntpd
openssh-client -y && \  
apt-get clean  
  
RUN echo "deb http://cloudstack.apt-get.eu/ubuntu trusty 4.9" >>
/etc/apt/sources.list.d/cloudstack.list && \  
wget -O - http://cloudstack.apt-get.eu/release.asc | apt-key add - && \  
apt-get update && \  
apt-get install cloudstack-management -y && \  
apt-get clean  
  
RUN mkdir -p /etc/sysconfig && \  
/bin/bash -c "echo -e \"LOCKD_TCPPORT=32803\n\  
MOUNTD_PORT=892\n\  
RQUOTAD_PORT=875\n\  
STATD_PORT=662\n\  
TATD_OUTGOING_PORT=2020\" >> /etc/sysconfig/nfs"  
  
RUN mkdir -p /export/primary && \  
mkdir -p /export/secondary && \  
chmod -R 0777 /export && \  
echo "/export *(rw,async,no_root_squash,no_subtree_check)" >> /etc/exports &&
\  
exportfs -a && \  
cloudstack-setup-management && \  
mkdir -p /var/lib/cloudstack/management/.ssh && \  
ssh-keygen -f /var/lib/cloudstack/management/.ssh/id_rsa -N '' && \  
chown -R cloud:cloud /var/lib/cloudstack/management  
  
RUN mkdir -p /usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver && \  
wget -P /usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver
http://download.cloud.com.s3.amazonaws.com/tools/vhd-util && \  
chmod 0755 /usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver/vhd-
util  
  
COPY start.sh /root/start.sh  
  
RUN chmod 0755 /root/start.sh  
  
CMD ["/root/start.sh"]  

