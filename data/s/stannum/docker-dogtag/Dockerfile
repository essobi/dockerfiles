FROM centos:7  
MAINTAINER Tin L. Lam <tin@irrational.io>  
  
ENV container=docker  
  
RUN yum -y update && yum clean all && \  
rm -rf /var/lock && \  
# rm -rf /etc/systemd/system && \  
yum -y install 389-ds-base pki-ca pki-kra sudo && yum clean all  
  
COPY ./assets/ /  
  
RUN find /lib/systemd/system/sysinit.target.wants/ ! -name 'systemd-tmpfiles-
setup.service' -type l -exec rm -fv {} + \  
&& rm -fv \  
/lib/systemd/system/multi-user.target.wants/* \  
/etc/systemd/system/*.wants/* \  
/lib/systemd/system/local-fs.target.wants/* \  
/lib/systemd/system/sockets.target.wants/*udev* \  
/lib/systemd/system/sockets.target.wants/*initctl* \  
/lib/systemd/system/basic.target.wants/* \  
/lib/systemd/system/anaconda.target.wants/*  
  
RUN set -x \  
&& sed -i 's/checkHostname {/checkHostname {\nreturn();/g'
/usr/lib64/dirsrv/perl/DSUtil.pm \  
&& rm -f /etc/systemd/system/default.target \  
&& ln -s /usr/lib/systemd/system/container-up.target
/etc/systemd/system/default.target \  
&& mkdir -p /etc/systemd/system/container-up.target.wants \  
&& ln -s /etc/systemd/system/dogtag.service /etc/systemd/system/container-
up.target.wants/dogtag.service \  
&& chmod +x /usr/local/bin/dogtag_start.sh \  
&& systemctl set-default container-up.target \  
&& rm -rf /var/cache/yum  
  
EXPOSE 389 8373  
VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]  
CMD ["/usr/sbin/init"]  
STOPSIGNAL SIGRTMIN+3  

