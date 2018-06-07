FROM centos:7  
MAINTAINER Tobias Florek tob@butter.sh  
  
# for documentation only, it is meant to use host network  
EXPOSE 500 4500 50 51  
ENV container docker  
  
LABEL INSTALL="docker run --rm --privileged --entrypoint /bin/sh -v /:/host -e
HOST=/host -e LOGDIR=\${LOGDIR} -e CONFDIR=\${CONFDIR} -e DATADIR=\${DATADIR}
-e IMAGE=IMAGE -e NAME=NAME IMAGE /bin/install.sh"  
  
LABEL UNINSTALL="docker run --rm --privileged --entrypoint /bin/sh -v /:/host
-e HOST=/host -e IMAGE=IMAGE -e NAME=NAME IMAGE /bin/uninstall.sh"  
  
LABEL RUN="docker run -d --privileged --net=host -v
/lib/modules:/lib/modules:ro -v /etc/ipsec:/etc/ipsec -v
/etc/ipsec.d:/etc/ipsec.d -n NAME /sbin/init"  
  
RUN yum --setopt=tsflags=nodocs -y install libreswan \  
&& yum clean all \  
&& touch /etc/sysconfig/ipsec \  
&& mv /etc/ipsec.conf /root/ipsec.conf \  
&& mv /etc/ipsec.secrets /root/ipsec.secrets \  
&& mv /etc/sysconfig/ipsec /root/sysconfig.ipsec \  
&& ln -fs /etc/ipsec/ipsec.conf /etc/ipsec.conf \  
&& ln -fs /etc/ipsec/ipsec.secrets /etc/ipsec.secrets \  
&& ln -fs /etc/ipsec/sysconfig.ipsec /etc/sysconfig/ipsec \  
&& rm /etc/systemd/system/*.wants/* \  
&& systemctl enable ipsec  
  
VOLUME ["/lib/modules", "/etc/ipsec", "/etc/ipsec.d", "/sys/fs/cgroup"]  
CMD ["/usr/sbin/init"]  
  
ADD install.sh uninstall.sh /bin/  

