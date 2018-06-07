FROM phusion/baseimage:latest  
  
MAINTAINER Dmitry K "d.p.karpov@gmail.com"  
ENV D_TIME_ZONE Europe/Moscow  
ENV D_CODEPAGE UTF-8  
ENV D_LANG ru_RU  
  
ENV ETCD_VER v2.0.8  
# this forces dpkg not to call sync() after package extraction and speeds up
install  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
# we don't need and apt cache in a container  
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
#EnableProposed  
RUN echo deb http://archive.ubuntu.com/ubuntu/ trusty-proposed restricted main
multiverse universe >> /etc/apt/sources.list  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && apt-get upgrade -y && \  
apt-get install -y wget python-software-properties software-properties-common
&& \  
apt-add-repository multiverse && \  
apt-add-repository universe && \  
add-apt-repository ppa:ubuntu-wine/ppa && \  
add-apt-repository ppa:x2go/stable && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections; echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo
debconf-set-selections && \  
apt-get install -y --no-install-recommends \  
gnome-session-flashback gnome-core language-pack-gnome-ru language-selector-
common \  
hyphen-ru mythes-ru myspell-ru libreoffice-help-ru libreoffice-l10n-ru
thunderbird-locale-ru cups cups-bsd cups-common \  
sshfs x2goserver x2goserver-xsession x2goserver-printing cups-x2go \  
unrar wine1.7 winetricks \  
mc \  
oracle-java7-installer \  
libpam-ldap nscd \  
libfuse2 && \  
cd /tmp ; apt-get download fuse && \  
cd /tmp ; dpkg-deb -x fuse_* . && \  
cd /tmp ; dpkg-deb -e fuse_* && \  
cd /tmp ; rm fuse_*.deb && \  
cd /tmp ; echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst && \  
cd /tmp ; dpkg-deb -b . /fuse.deb && \  
cd /tmp ; dpkg -i /fuse.deb && rm -rf /fuse.deb && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /var/tmp/* && \  
rm -rf /tmp/* \  
/src \  
/etc/cron.weekly/apt-xapian-index  
  
RUN rm -rf /etc/service/*  
  
# Upstart and DBus have issues inside docker. We work around in order to
install firefox.  
RUN dpkg-divert --local \--rename --add /sbin/initctl && ln -sf /bin/true
/sbin/initctl  
  
# Set locale (fix the locale warnings)  
RUN localedef -v -c -i ${D_LANG} -f ${D_CODEPAGE} ${D_LANG}.${D_CODEPAGE} || :  
RUN update-locale LANG=${D_LANG}.${D_CODEPAGE}  
RUN echo "${TIME_ZONE}" > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
RUN mkdir -p /var/run/sshd  
  
RUN mkdir /src  
  
ADD startup.sh /etc/service/x2go/run  
RUN chmod +x /etc/service/x2go/run  
  
ADD discovery.sh /etc/service/discovery/run  
RUN chmod +x /etc/service/discovery/run  
  
ADD nscd.sh /etc/service/nscd/run  
RUN chmod +x /etc/service/nscd/run  
  
ADD ./00_regen_ssh_host_keys.sh /etc/my_init.d/00_regen_ssh_host_keys.sh  
RUN chmod +x /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
RUN curl -sSL
https://github.com/coreos/etcd/releases/download/${ETCD_VER}/etcd-${ETCD_VER}-linux-
amd64.tar.gz -o /etcd-${ETCD_VER}-linux-amd64.tar.gz && \  
cd /; tar -xf etcd-${ETCD_VER}-linux-amd64.tar.gz && \  
cp /etcd-${ETCD_VER}-linux-amd64/etcdctl /usr/local/bin/ && \  
rm -rf /etcd-${ETCD_VER}-linux-amd64*  
  
EXPOSE 22  
CMD ["/sbin/my_init"]  
  

