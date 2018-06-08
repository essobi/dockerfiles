FROM fedora:25  
MAINTAINER Daniel Winter  
  
ENV container docker  
  
RUN dnf -y update && dnf clean all  
  
RUN dnf -y install systemd && dnf clean all && \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
# ansible and other requirements  
RUN dnf makecache fast \  
&& dnf -y install \  
ansible \  
sudo \  
which \  
python2-dnf \  
&& dnf -y install @server-product-environment \  
&& dnf clean all  
  
# disable requiretty  
RUN sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
  
RUN cp /usr/lib/systemd/system/dbus.service /etc/systemd/system/; sed -i
's/OOMScoreAdjust=-900//' /etc/systemd/system/dbus.service  
  
# ansible inventory file  
RUN echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts  
  
VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]  
CMD ["/usr/sbin/init"]

