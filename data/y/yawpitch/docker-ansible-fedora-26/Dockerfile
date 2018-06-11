FROM fedora:26  
LABEL maintainer="Michael Morehouse (yawpitch)"  
ENV container=docker  
  
# Update and enable systemd.  
RUN dnf -y update && dnf -y install systemd && dnf clean all && \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
# Install Ansible and other requirements.  
RUN dnf -y install \  
redhat-rpm-config \  
make \  
iputils \  
python-devel \  
python-pip \  
python-wheel \  
openssl-devel \  
sudo \  
which \  
python2-dnf \  
unzip \  
tar \  
gcc \  
libffi-devel \  
glibc \  
glibc-devel \  
findutils \  
&& dnf clean all  
  
# Install Ansible  
RUN pip install --upgrade pip  
RUN pip install ansible  
  
# Disable requiretty.  
RUN sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
  
# Install Ansible inventory file.  
COPY hosts /etc/ansible/hosts  
  
# Set cgroup volume  
VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]  
  
# Set initial cmd  
CMD ["/usr/lib/systemd/systemd"]  

