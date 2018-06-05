FROM centos:7  
MAINTAINER Lawrence Stubbs <technoexpressnet@gmail.com>  
  
# Install Required Dependencies  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& yum -y install curl perl fail2ban sendmail mailx fail2ban-hostsdeny
denyhosts \  
iptables-utils iptables-services unzip git vim crontabs cronie wget net-tools
\  
sysvinit-tools which whois initscripts  
  
RUN yum -y install python2-pip \  
&& pip install --upgrade pip \  
&& pip install pyinotify  
  
COPY etc /etc/  
  
# Fixes issue with running systemD inside docker builds  
# From https://github.com/gdraheim/docker-systemctl-replacement  
COPY systemctl.py /usr/bin/systemctl.py  
# Installed Webmin repositorie and Webmin  
RUN cp -f /usr/bin/systemctl /usr/bin/systemctl.original \  
&& chmod +x /usr/bin/systemctl.py \  
&& cp -f /usr/bin/systemctl.py /usr/bin/systemctl \  
&& wget http://www.webmin.com/jcameron-key.asc -q && rpm --import jcameron-
key.asc \  
&& yum install webmin yum-versionlock sudo -y && rm jcameron-key.asc \  
&& yum versionlock systemd  
  
# disable units failing in container  
RUN systemctl.original mask auditd firewalld \  
libvirtd fwupd nfs-config rtkit-daemon \  
udisks2 upower  
  
# disable units obviously slowing down startup  
RUN systemctl.original mask NetworkManager lm_sensors  
  
# disable some rather useless units for a bit faster startup  
RUN systemctl.original mask blk-availability colord \  
dmraid-activation dracut-shutdown gssproxy \  
iscsi-shutdown lvm2-lvmetad lvm2-monitor \  
ModemManager netcf-transaction \  
selinux-autorelabel-mark \  
systemd-hwdb-update systemd-update-done  
  
# avoid dbus issue  
RUN mkdir -p /var/lib/dbus  
  
RUN systemctl.original disable dbus firewalld \  
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
  
RUN mkdir -p /var/log/asterisk \  
&& mkdir -p /var/log/httpd \  
&& mkdir -p /var/log/nginx \  
&& mkdir -p /var/log/horde \  
&& mkdir -p /var/log/sogo \  
&& mkdir -p /var/log/squid \  
&& mkdir -p /var/log/named \  
&& mkdir -p /var/log/freeswitch \  
&& mkdir -p /var/log/stunnel4 \  
&& mkdir -p /var/log/ejabberd \  
&& mkdir -p /var/log/directadmin \  
&& touch /var/log/asterisk/full /var/log/secure /var/log/auth.log
/var/log/maillog /var/log/httpd/access_log /var/log/httpd/error_log
/var/log/fail2ban.log /var/log/nginx/access*.log /var/log/openwebmail.log
/var/log/horde/horde.log /var/log/sogo/sogo.log /var/log/monit
/var/log/squid/access.log /var/log/3proxy.log /var/log/named/security.log
/var/log/nsd.log /var/log/freeswitch/freeswitch.log
/var/log/stunnel4/stunnel.log /var/log/ejabberd/ejabberd.log
/var/log/directadmin/login.log /var/log/mysqld.log  
  
RUN sed -i "s#10000#19999#" /etc/webmin/miniserv.conf \  
&& systemctl.original disable sendmail.service \  
&& systemctl.original enable iptables.service denyhosts.service
fail2ban.service crond.service webmin.service containerstartup.service \  
&& chmod +x /etc/containerstartup.sh \  
&& mv -f /etc/containerstartup.sh /containerstartup.sh \  
&& echo "root:fail2ban" | chpasswd  
  
ENV container docker  
ENV WEBMINPORT 19999  
EXPOSE 19999/tcp 19999/udp  
  
CMD ["/usr/bin/systemctl","default","--init"]

