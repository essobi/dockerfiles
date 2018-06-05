FROM centos:7  
MAINTAINER ManageIQ https://github.com/ManageIQ  
  
ARG REF=master  
  
ENV TERM=xterm  
  
## Atomic/OpenShift Labels  
LABEL name="manageiq-embedded-ansible" \  
vendor="ManageIQ" \  
version="Master" \  
release=${REF} \  
url="http://manageiq.org/" \  
summary="ManageIQ Embedded Ansible Image" \  
description="Embedded Ansible running as a container." \  
io.k8s.display-name="ManageIQ Embedded Ansible" \  
io.openshift.expose-services="443:https" \  
io.openshift.tags="Ansible,ManageIQ"  
## To cleanly shutdown systemd, use SIGRTMIN+3  
STOPSIGNAL SIGRTMIN+3  
  
COPY container-assets/ansible-tower.repo /etc/yum.repos.d  
  
## Install EPEL repo, yum necessary packages for the build without docs, clean
all caches  
RUN yum -y install epel-release \  
https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-
centos96-9.6-3.noarch.rpm && \  
  
yum -y install --setopt=tsflags=nodocs ansible-tower-server-3.2.3 \  
ansible-tower-setup-3.2.3 \  
nmap-ncat \  
iproute \  
sudo && \  
yum clean all  
  
## Expose required container ports  
EXPOSE 80 443  
## Systemd cleanup base image  
RUN (cd /lib/systemd/system/sysinit.target.wants && for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -vf $i; done) && \  
rm -vf /lib/systemd/system/multi-user.target.wants/* && \  
rm -vf /etc/systemd/system/*.wants/* && \  
rm -vf /lib/systemd/system/local-fs.target.wants/* && \  
rm -vf /lib/systemd/system/sockets.target.wants/*udev* && \  
rm -vf /lib/systemd/system/sockets.target.wants/*initctl* && \  
rm -vf /lib/systemd/system/basic.target.wants/* && \  
rm -vf /lib/systemd/system/anaconda.target.wants/*  
  
COPY container-assets/entrypoint /usr/bin  
COPY container-assets/initialize-tower.sh /usr/bin  
COPY container-assets/initialize-tower.service /usr/lib/systemd/system  
  
RUN systemctl enable initialize-tower  
  
VOLUME /sys/fs/cgroup  
  
ENTRYPOINT ["entrypoint"]  
CMD [ "/usr/sbin/init" ]  

