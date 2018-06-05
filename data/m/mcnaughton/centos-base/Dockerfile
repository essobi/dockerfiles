FROM centos:latest  
MAINTAINER Taylor Buley (taylor.buley@mcnaughton.media)  
  
RUN groupadd -g 1855 application \  
&& /usr/sbin/useradd --uid 1855 --create-home --home-dir
/usr/local/application \--shell /bin/bash -g application application \  
&& /usr/sbin/usermod -g application root \  
&& chown -R application:application /usr/local/ \  
&& chown -R application:application /usr/src/ \  
&& chown -R application:application /usr/lib/ \  
&& chown -R application:application /usr/bin/ \  
&& chown -R root:application /var/log \  
&& chown -R application:application /srv \  
&& chmod 765 /srv \  
&& chmod +s /srv  
  
RUN yum -y -q update \  
&& yum -y -q install which epel-release freetype fontconfig bzip2 tar gcc
gcc-c++ cmake git deltarpm \  
"Development Tools" unzip gitmake \  
&& yum -y -q update \  
&& yum -y -q upgrade \  
&& yum install -y -q openssl openssl-devel curl wget --enablerepo=epel  
  
ENV container=docker  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
  
VOLUME [ "/sys/fs/cgroup", "/run" ]  
  
CMD ["/usr/sbin/init"]  

