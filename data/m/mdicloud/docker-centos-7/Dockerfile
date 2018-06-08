FROM centos:7  
MAINTAINER Martin Diederich <martin.diederich@gmail.com>  
  
# set env vars  
ENV container docker  
ENV LC_ALL C  
  
# systemd tweaks  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
# install  
RUN yum -y update  
RUN yum -y install epel-release systemd  
  
# install typical requirements for testing  
RUN yum -y install ca-certificates python python-httplib2 sudo unzip curl net-
tools nc  
  
# install goss  
RUN curl -L https://github.com/aelsabbahy/goss/releases/download/v0.2.6/goss-
linux-amd64 -o /usr/local/bin/goss  
RUN chmod +rx /usr/local/bin/goss  
  
# install docker-detect-proxy.sh  
RUN curl -L https://raw.githubusercontent.com/mdicloud/docker-
helper/master/docker-detect-proxy.sh -o /usr/local/bin/docker-detect-proxy.sh  
RUN chmod +rx /usr/local/bin/docker-detect-proxy.sh  
  
# map volumes  
VOLUME ["/sys/fs/cgroup"]  
  
# cleanup  
RUN yum clean all  
  
# finally run script on startup  
ENTRYPOINT ["/usr/local/bin/docker-detect-proxy.sh"]  
CMD ["/sbin/init"]  

