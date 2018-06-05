# Billmanager-advanced  
#  
# VERSION 0.0.1  
FROM debian:jessie  
  
ENV CORE_DIR /usr/local/mgr5  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
RUN apt-get update && apt-get install -y wget && \  
wget http://dl.ispsystem.com/install.sh && \  
sh install.sh --release beta --ignore-hostname --silent --disable-fail2ban
--noinstall && \  
apt-get -y install coremanager vim && apt-get clean && rm -rf ${CORE_DIR}/var
&& \  
apt-get -y update && apt-get -y install billmanager-advanced vim && apt-get -y
clean && \  
service mysql stop && \  
rm -rf /var/lib/mysql && \  
echo > ${CORE_DIR}/etc/billmgr.conf.d/db.conf && \  
rm -f ${CORE_DIR}/etc/manager.{key,crt} && rm -f ${CORE_DIR}/etc/ihttpd.conf
&& \  
sed -i -r 's/^(password\s*=).*/\1/' /etc/mysql/debian.cnf && \  
sed -i -r 's/^(user\s*=).*/\1/' /etc/mysql/debian.cnf && \  
mkdir -p /var/lib/mysql && mysql_install_db && service mysql start &&
mysqladmin create billmgr5 && \  
${CORE_DIR}/sbin/mgrctl -m billmgr whoami || ${CORE_DIR}/sbin/mgrctl -m
billmgr whoami || ${CORE_DIR}/sbin/mgrctl -m billmgr whoami && \  
rm -f ${CORE_DIR}/etc/billmgr.lic  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 1500  
CMD ["billmgr"]  

