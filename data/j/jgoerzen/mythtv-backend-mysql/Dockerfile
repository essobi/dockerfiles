FROM jgoerzen/mythtv-backend  
MAINTAINER John Goerzen <jgoerzen@complete.org>  
RUN mv /usr/sbin/policy-rc.d.disabled /usr/sbin/policy-rc.d  
RUN apt-get update && \  
apt-get -y --no-install-recommends install mysql-server && \  
apt-get -y -u dist-upgrade && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN mv /usr/sbin/policy-rc.d /usr/sbin/policy-rc.d.disabled  
  
# MySQL MUST be running before we install mythtv-database.  
# And it's lovely that the postinst has a bug when the root  
# password is empty, too.... (or, for that matter, when it contains spaces...)  
  
RUN /etc/init.d/mysql start && \  
while [ ! -e /var/run/mysqld/mysqld.sock ]; do sleep 1; done; sleep 1 && \  
apt-get update && \  
mv -vi /etc/apt/apt.conf.d/docker-clean /tmp && \  
apt-get -dy --no-install-recommends install mythtv-database && \  
echo "" | DEBIAN_FRONTEND=noninteractive DEBIAN_PRIORITY=critical \  
dpkg --unpack /var/cache/apt/archives/*.deb && \  
mv -vi /tmp/docker-clean /etc/apt/apt.conf.d/ && \  
sed -i 's/-p$admin_password/--password=$admin_password/g'
/var/lib/dpkg/info/mythtv-database.postinst && \  
dpkg --configure -a && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
/etc/init.d/mysql stop  
RUN /usr/local/bin/docker-wipelogs  
  
EXPOSE 6554 6543 6544 6549 5901  
CMD ["/usr/local/bin/boot-debian-base"]  
  

