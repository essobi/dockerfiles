FROM centos:7  
  
MAINTAINER Takashi Abe <abe@office303.co.jp>  
  
ENV container docker  
  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); rm -f
/lib/systemd/system/multi-user.target.wants/*; rm -f
/etc/systemd/system/*.wants/*; rm -f /lib/systemd/system/local-
fs.target.wants/*; rm -f /lib/systemd/system/sockets.target.wants/*udev*; rm
-f /lib/systemd/system/sockets.target.wants/*initctl*; rm -f
/lib/systemd/system/basic.target.wants/*; rm -f
/lib/systemd/system/anaconda.target.wants/*;  
  
VOLUME [ "/sys/fs/cgroup" ]  
  
RUN yum -y update  
  
RUN yum -y reinstall glibc-common  
RUN localedef -v -c -i ja_JP -f UTF-8 ja_JP.UTF-8; echo "";  
  
ENV LANG=ja_JP.utf8  
RUN rm -f /etc/localtime  
RUN ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
RUN yum -y install git cronie chrony  
  
RUN echo $'\n\  
server ntp.nict.jp iburst\n\  
\n\  
# Ignore stratum in source selection.\n\  
stratumweight 0\n\  
' > /etc/chrony.conf  
  
RUN systemctl enable crond && systemctl enable chronyd  
  
RUN yum clean all  
  
CMD date  
  
CMD ["/usr/sbin/init"]  

