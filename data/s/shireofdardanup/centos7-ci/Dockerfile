FROM centos:7  
LABEL maintainer="Stephen Eaton - seaton@dardanup.wa.gov.au"  
ENV container=docker  
ENV PROMETHEUS_VERSION 2.0.0  
# Install systemd -- See https://hub.docker.com/_/centos/  
RUN yum -y update; yum clean all; \  
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
RUN yum makecache fast \  
&& yum -y install deltarpm epel-release initscripts \  
&& yum -y update \  
&& yum -y install \  
ansible \  
sudo \  
which \  
python-pip \  
&& yum clean all  
  
RUN pip install ansible-lint  
  
# Disable requiretty.  
RUN sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
  
# Install Ansible inventory file.  
RUN echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts  
  
# get prometheus release and install promtool  
RUN yum install -y wget  
RUN wget -O prometheus.tar.gz
https://github.com/prometheus/prometheus/releases/download/v$PROMETHEUS_VERSION/prometheus-$PROMETHEUS_VERSION.linux-
amd64.tar.gz  
RUN mkdir /prometheus  
RUN tar -xvf prometheus.tar.gz -C /prometheus --strip-components 1
\--wildcards */promtool  
  
VOLUME ["/sys/fs/cgroup"]  
CMD ["/usr/sbin/init"]  

