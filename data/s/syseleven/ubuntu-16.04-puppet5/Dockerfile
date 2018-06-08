# docker build -f Dockerfile-ubuntu-16.04-puppet5 -t
syseleven/ubuntu-16.04-puppet5 .  
FROM ubuntu:16.04  
MAINTAINER Stefan Andres <s.andres@syseleven.de>  
ENV container docker  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install --no-install-recommends -y ruby ruby-dev
wget \  
# install puppet  
&& wget https://apt.puppetlabs.com/puppet5-release-xenial.deb -O
/tmp/puppet.deb \  
&& dpkg -i /tmp/puppet.deb && apt-get update \  
&& apt-get -y install --no-install-recommends puppet-agent \  
# install sys11 deps  
&& apt-get -y install --no-install-recommends rsyslog nagios-nrpe-server
nagios-plugins-basic vim-tiny nagios-plugins-standard nagios-nrpe-plugin \  
pwgen apt-transport-https software-properties-common cron-apt python bc git
rsync \  
# install kitchen deps  
&& apt-get -y install --no-install-recommends sudo openssh-server curl lsb-
release net-tools locales \  
&& locale-gen en_US.UTF-8 && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
\  
&& apt-get -y upgrade  
  
  
RUN apt-get -y install --no-install-recommends systemd dbus && \  
systemctl mask dev-mqueue.mount dev-hugepages.mount \  
systemd-remount-fs.service sys-kernel-config.mount \  
sys-kernel-debug.mount sys-fs-fuse-connections.mount \  
display-manager.service graphical.target systemd-logind.service \  
getty@tty1.service puppet mcollective  
  
ADD dbus.service /etc/systemd/system/dbus.service  
ADD myinit /myinit  
RUN systemctl enable dbus.service  
  
VOLUME ["/sys/fs/cgroup"]  
VOLUME ["/run"]  
  
CMD ["/lib/systemd/systemd"]  

