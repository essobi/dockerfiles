FROM centos:6.8  
MAINTAINER miko@cafelounge.net  
  
# script  
COPY run-parts /usr/bin/  
COPY init /boot/  
# networking & timezone && user  
RUN echo "NETWORKING=yes" > /etc/sysconfig/network \  
&& echo 'ZONE="Asia/Tokyo"' > /etc/sysconfig/clock \  
&& yum reinstall -y glibc-common \  
&& cd /tmp \  
&& curl -OL http://rpms.famillecollet.com/enterprise/remi-release-6.rpm \  
&& yum -y install epel-release iptables yum-plugin-ovl \  
&& yum -y localinstall remi-release-6.rpm \  
&& rpm -e \--nodeps redhat-logos \  
&& yum clean all \  
&& rm -rf /tmp/*.rpm /var/tmp/* /var/lib/yum/* /var/cache/yum/* \  
&& rm -rf /etc/init/*tty* \  
&& curl -o /usr/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64" \  
&& chmod +x /usr/bin/gosu \  
&& localedef \--delete-from-archive $(localedef --list-archive | grep -v -i -e
"^en" -e "^ja" | xargs ) \  
&& mv /usr/lib/locale/locale-archive.tmpl /usr/lib/locale/locale-archive.dist
\  
&& mv /usr/lib/locale/locale-archive /usr/lib/locale/locale-archive.tmpl \  
&& /usr/sbin/build-locale-archive \  
&& mv -f /usr/lib/locale/locale-archive.dist /usr/lib/locale/locale-
archive.tmpl \  
&& ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& rm -f /sbin/sln \  
&& rm -rf /etc/ld.so.cache \  
&& rm -rf /var/cache/ldconfig/* \  
&& chkconfig iptables off \  
&& chkconfig network off \  
&& chkconfig udev-post off \  
&& mkdir -p /etc/{cron.daily,cron.weekly,cron.monthly} \  
&& chmod 755 /usr/bin/run-parts \  
&& chmod 700 /boot/init  
# environment  
ENV HOME=/root LANG=ja_JP.utf-8  
WORKDIR /root  
# entrypoint  
ENTRYPOINT ["/boot/init"]  
  
# command  
CMD ["3"]  

