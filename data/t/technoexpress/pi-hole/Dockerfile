FROM centos:7  
MAINTAINER Lawrence Stubbs <technoexpressnet@gmail.com>  
  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& yum install wget dialog git iproute net-tools newt bind-utils nmap-ncat
which \  
bc dnsmasq lighttpd lighttpd-fastcgi unzip cronie sudo php php-cli php-common
-y \  
&& yum update -y  
  
# Fixes issue with running systemD inside docker builds  
# From https://github.com/gdraheim/docker-systemctl-replacement  
COPY systemctl.py /usr/bin/systemctl.py  
RUN cp -f /usr/bin/systemctl /usr/bin/systemctl.original \  
&& chmod +x /usr/bin/systemctl.py \  
&& cp -f /usr/bin/systemctl.py /usr/bin/systemctl  
COPY etc /etc/  
COPY var /var/  
  
RUN export USER=pihole && adduser pihole -m -s /usr/sbin/nologin && touch
/etc/pihole/local.list \  
&& wget -qO basic-install.sh https://install.pi-hole.net \  
&& bash basic-install.sh --unattended \  
&& rm -f basic-install.sh  
  
# Install Webmin repositorie and Webmin  
RUN yum -y install perl perl-Net-SSLeay openssl perl-IO-Tty perl-Encode-Detect
\  
&& yum -y install
http://prdownloads.sourceforge.net/webadmin/webmin-1.870-1.noarch.rpm  
  
RUN yum install yum-versionlock -y && yum versionlock systemd \  
&& yum remove nmap-ncat -y \  
&& rpm -i https://nmap.org/dist/ncat-7.60-1.x86_64.rpm \  
&& ln -s /usr/bin/ncat /usr/bin/nc  
  
RUN systemctl stop firewalld \  
&& systemctl.original disable dbus firewalld \  
&& (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \  
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*; \  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*; \  
rm -f /lib/systemd/system/anaconda.target.wants/*; \  
rm -f /etc/dbus-1/system.d/*; \  
rm -f /etc/systemd/system/sockets.target.wants/*;  
  
RUN sed -i 's#10000#9000#' /etc/webmin/miniserv.conf \  
&& sed -i "s#':53 '#:\$DNSPORT #" /etc/.pihole/pihole \  
&& sed -i "s#':53 '#:\$DNSPORT #" /usr/local/bin/pihole \  
&& sed -i "s#--dport 53#--dport \$DNSPORT#g" /etc/.pihole/automated\
install/basic-install.sh \  
&& sed -i "s@"\${PI_HOLE_GIT_URL}\"@" \${PI_HOLE_GIT_URL} \"\nsed -i \"s#':53
'#:\\\\\\\\\$DNSPORT #\" \${PI_HOLE_FILES_DIR}/pihole\nsed -i \"s#--dport
53#--dport \\\\\\\\\$DNSPORT#g\" \${PI_HOLE_FILES_DIR}/automated\\\\\
install/basic-install.sh@g" /etc/.pihole/advanced/Scripts/update.sh \  
&& sed -i "s@"\${PI_HOLE_GIT_URL}\"@" \${PI_HOLE_GIT_URL} \"\nsed -i \"s#':53
'#:\\\\\\\\\$DNSPORT #\" \${PI_HOLE_FILES_DIR}/pihole\nsed -i \"s#--dport
53#--dport \\\\\\\\\$DNSPORT#g\" \${PI_HOLE_FILES_DIR}/automated\\\\\
install/basic-install.sh@g" /opt/pihole/update.sh \  
&& systemctl.original enable dnsmasq.service lighttpd.service crond.service
webmin.service containerstartup.service \  
&& chmod +x /etc/containerstartup.sh \  
&& mv -f /etc/containerstartup.sh /containerstartup.sh \  
&& echo "root:pi-hole" | chpasswd  
  
ENV IPV4 0.0.0.0  
ENV IPV6 ::0  
ENV DNS1 8.8.8.8  
ENV DNS2 8.8.4.4  
ENV DNSPORT 53  
ENV INTERFACE eth0  
ENV WEBMINPORT 9000  
  
EXPOSE 80 53/udp 53/tcp 4711-4720/tcp 9000/tcp 9000/udp  
  
ENTRYPOINT ["/usr/bin/systemctl","default","--init"]  

