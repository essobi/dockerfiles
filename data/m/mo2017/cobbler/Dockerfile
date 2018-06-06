FROM centos:7.3.1611  
MAINTAINER "Xiao Mo" <root@xiaomo.red>  
  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8 \  
&& yum install yum-utils epel-release wget pykickstart curl file util-linux -y
\  
&& yum-config-manager --add-repo
http://download.opensuse.org/repositories/home:/libertas-
ict:/cobbler28/CentOS_7/home:libertas-ict:cobbler28.repo \  
&& yum makecache \  
&& yum -y install cobbler-2.8.2-6.1 cobbler-web-2.8.2-6.1 tftp-server dhcp
openssl supervisor \  
&& yum clean all \  
&& rm -rf /var/cache/yum/*  
  
RUN wget -O /var/lib/cobbler/loaders/README
http://cobbler.github.io/loaders/README \  
&& wget -O /var/lib/cobbler/loaders/COPYING.elilo
http://cobbler.github.io/loaders/COPYING.elilo \  
&& wget -O /var/lib/cobbler/loaders/COPYING.yaboot
http://cobbler.github.io/loaders/COPYING.yaboot \  
&& wget -O /var/lib/cobbler/loaders/COPYING.syslinux
http://cobbler.github.io/loaders/COPYING.syslinux \  
&& wget -O /var/lib/cobbler/loaders/elilo-ia64.efi
http://cobbler.github.io/loaders/elilo-3.8-ia64.efi \  
&& wget -O /var/lib/cobbler/loaders/yaboot
http://cobbler.github.io/loaders/yaboot-1.3.17 \  
&& wget -O /var/lib/cobbler/loaders/pxelinux.0
http://cobbler.github.io/loaders/pxelinux.0-3.86 \  
&& wget -O /var/lib/cobbler/loaders/menu.c32
http://cobbler.github.io/loaders/menu.c32-3.86 \  
&& wget -O /var/lib/cobbler/loaders/grub-x86.efi
http://cobbler.github.io/loaders/grub-0.97-x86.efi \  
&& wget -O /var/lib/cobbler/loaders/grub-x86_64.efi
http://cobbler.github.io/loaders/grub-0.97-x86_64.efi \  
&& wget -O /var/lib/cobbler/distro_signatures.json
https://cobbler.github.io/signatures/2.8.x/latest.json  
  
COPY tftp /etc/xinetd.d/tftp  
COPY docker-entrypoint.sh /usr/local/bin/  
COPY supervisord.d/conf.ini /etc/supervisord.d/conf.ini  
  
ENV Cobbler_SERVER_IP=null \  
Cobbler_PASSWORD=root \  
Cobbler_DHCP_SUBNET=null \  
Cobbler_DHCP_ROUTER=null \  
Cobbler_DHCP_DNS=114.114.114.114 \  
Cobbler_DHCP_RANGE=null \  
Cobbler_DHCP_NETMASK=null  
  
VOLUME /etc/cobbler /var/lib/cobbler /var/www/cobbler /var/log/cobbler
/var/lib/tftpboot  
  
CMD ["docker-entrypoint.sh"]  

