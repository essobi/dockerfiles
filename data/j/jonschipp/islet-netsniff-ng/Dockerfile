# Netsniff-ng Sandbox - Upstream Latest  
#  
# VERSION 1.0  
FROM ubuntu  
MAINTAINER Jon Schipp <jonschipp@gmail.com>  
  
# Specify container username e.g. training, demo  
ENV VIRTUSER demo  
  
RUN apt-get update -qq  
RUN apt-get install -y language-pack-en git make ccache flex bison libnl-3-dev
libnl-genl-3-dev libgeoip-dev libnetfilter-conntrack-dev libncurses5-dev
liburcu-dev libnacl-dev libpcap-dev zlib1g-dev libcli-dev libnet1-dev  
RUN apt-get install -y telnet iptables git vim emacs nano tcpdump gawk rsyslog  
RUN apt-get install -y --no-install-recommends man-db  
RUN adduser --disabled-password --gecos "" $VIRTUSER  
RUN mkdir -p /usr/local/share/man/man8  
RUN su -l -c 'git clone http://github.com/netsniff-ng/netsniff-ng && cd
netsniff-ng && ./configure && make' $VIRTUSER  
RUN cd /home/$VIRTUSER/netsniff-ng && make install  
RUN su -l -c 'git clone http://github.com/jonschipp/gencfg' $VIRTUSER  
RUN echo "export TMOUT=1800; readonly TMOUT" > /etc/profile.d/timeout.sh &&
chmod 555 /etc/profile.d/timeout.sh  
RUN setcap cap_net_raw,cap_net_admin=eip /sbin/xtables-multi  
RUN setcap cap_net_raw,cap_net_admin=eip /usr/local/sbin/netsniff-ng  
RUN setcap cap_net_raw,cap_net_admin=eip /usr/local/sbin/trafgen  
RUN setcap cap_net_raw,cap_net_admin=eip /usr/local/sbin/mausezahn  
RUN setcap cap_net_raw,cap_net_admin=eip /usr/local/sbin/ifpps  
RUN setcap cap_net_raw,cap_net_admin=eip /usr/local/sbin/flowtop  
RUN setcap cap_net_raw,cap_net_admin=eip /usr/local/sbin/astraceroute  
RUN setcap cap_net_raw,cap_net_admin=eip /usr/local/sbin/curvetun  

