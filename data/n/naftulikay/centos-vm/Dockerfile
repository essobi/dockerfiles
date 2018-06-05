FROM centos:7  
MAINTAINER Naftuli Kay <me@naftuli.wtf>  
# with credits upstream: https://hub.docker.com/r/geerlingguy/docker-
centos7-ansible/  
# systemd wants this: http://red.ht/2sPKSZA  
ENV container=docker  
  
# install ansible and system utilities  
RUN yum makecache fast >/dev/null \  
&& yum -y install deltarpm epel-release initscripts >/dev/null \  
&& yum -y update >/dev/null \  
&& yum -y install ansible sudo which less >/dev/null \  
&& yum clean all >/dev/null \  
# remove the machine id from the container; also disable targets that won't
work in a container  
&& rm -f /etc/machine-id \  
/usr/lib/systemd/system/sysinit.target.wants/systemd-firstboot.service \  
/usr/lib/systemd/system/local-fs.target.wants/systemd-remount-fs.service \  
/usr/lib/systemd/system/sysinit.target.wants/systemd-machine-id-commit.service
\  
/etc/systemd/system/getty.target.wants/getty@tty1.service  
  
# disable requiretty.  
RUN sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
  
# our own utility for awaiting systemd "boot" in the container  
COPY bin/systemd-await-target /usr/bin/systemd-await-target  
COPY bin/wait-for-boot /usr/bin/wait-for-boot  
  
# install local inventory file.  
RUN echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts  
  
# systemd stuff  
VOLUME ["/sys/fs/cgroup"]  
ENTRYPOINT ["/usr/sbin/init"]  

