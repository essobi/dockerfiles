FROM centos:7  
MAINTAINER ManageIQ https://github.com/ManageIQ/manageiq-appliance-build  
  
## Set build ARGs  
ARG REF=master  
  
## Set ENV, LANG only needed if building with docker-1.8  
ENV TERM=xterm \  
IMAGE_VERSION=${REF}  
  
## Atomic/OpenShift Labels  
LABEL name="ansible-tower" \  
vendor="ManageIQ" \  
version="Master" \  
release=${REF} \  
url="http://manageiq.org/" \  
summary="Ansible Tower Image" \  
description="Ansible Tower running as a container." \  
io.k8s.display-name="ManageIQ Ansible Tower" \  
description="Ansible Tower running as a container." \  
io.openshift.expose-services="443:https" \  
io.openshift.tags="Ansible,Tower,ManageIQ"  
## To cleanly shutdown systemd, use SIGRTMIN+3  
STOPSIGNAL SIGRTMIN+3  
  
COPY docker-assets/ansible-tower.repo /etc/yum.repos.d  
  
## Install EPEL repo, yum necessary packages for the build without docs, clean
all caches  
RUN yum -y install epel-release \  
https://download.postgresql.org/pub/repos/yum/9.4/redhat/rhel-7-x86_64/pgdg-
centos94-9.4-3.noarch.rpm && \  
  
yum -y install --setopt=tsflags=nodocs ansible-tower-server \  
ansible-tower-setup \  
ansible-tower-ui \  
nmap-ncat \  
iproute && \  
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
  
COPY docker-assets/entrypoint /usr/bin  
COPY docker-assets/initialize-tower.sh /usr/bin  
COPY docker-assets/initialize-tower.service /usr/lib/systemd/system  
  
RUN systemctl enable initialize-tower  
  
ENTRYPOINT ["entrypoint"]  
CMD [ "/usr/sbin/init" ]  

