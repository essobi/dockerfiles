FROM ergomentum/centos:7.4.171015192854  
MAINTAINER \  
Ergomentum <build@ergomentum.org>  
  
LABEL \  
vendor="Ergomentum" \  
license="Apache 2.0"  
  
# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1213602  
RUN \  
touch /var/lib/rpm/* && \  
yum install mariadb-server && \  
yum clean all && \  
install -d '/docker-entrypoint-initdb.d' -o mysql -g mysql && \  
echo -e 'skip-host-cache\nskip-name-resolve\nlocal-infile=0' | \  
awk '{ print } $1 == "[mysqld]" && c == 0 { c = 1; system("cat") }' \  
/etc/my.cnf > /etc/my.cnf.tmp && \  
mv /etc/my.cnf{.tmp,} && \  
rm -f /var/log/mariadb/mariadb.log && \  
ln -s /dev/stderr /var/log/mariadb/mariadb.log  
  
VOLUME \  
["/docker-entrypoint-initdb.d"]  
  
COPY \  
entrypoint.sh /  
  
ENTRYPOINT \  
["/entrypoint.sh"]  
  
USER \  
mysql  
  
EXPOSE \  
3306  

