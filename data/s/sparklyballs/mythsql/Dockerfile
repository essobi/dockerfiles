FROM phusion/baseimage:0.9.16  
# Set correct environment variables  
ENV HOME="/root" DEBIAN_FRONTEND=noninteractive TERM=xterm  
  
ADD mariadb.sh /etc/service/mariadb/run  
  
EXPOSE 3306  
  
VOLUME /db  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
  
apt-get update -q && \  
# Install Dependencies  
apt-get install -qy mariadb-server && \  
# Tweak my.cnf  
sed -i -e 's#\\(bind-address.*=\\).*#\1 0.0.0.0#g' /etc/mysql/my.cnf && \  
sed -i -e 's#\\(log_error.*=\\).*#\1 /db/mysql_safe.log#g' /etc/mysql/my.cnf
&& \  
sed -i -e 's/\\(user.*=\\).*/\1 nobody/g' /etc/mysql/my.cnf && \  
# set startup executable  
chmod +x /etc/service/mariadb/run && \  
# clean up  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
/usr/share/man /usr/share/groff /usr/share/info \  
/usr/share/lintian /usr/share/linda /var/cache/man && \  
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) &&
\  
(( find /usr/share/doc -empty|xargs rmdir || true ))  

