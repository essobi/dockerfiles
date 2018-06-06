FROM centos:6  
RUN \  
unlink /etc/localtime \  
&& ln -s /usr/share/zoneinfo/Japan /etc/localtime \  
&& localedef -f UTF-8 -i ja_JP ja_JP.UTF-8  
  
RUN \  
curl -s -o /tmp/opt-mysql4-4.0.30-1.x86_64.rpm \  
https://raw.githubusercontent.com/tukiyo/mysql4.0.30.el6/master/rpmbuild/RPMS/x86_64/opt-
mysql4-4.0.30-1.x86_64.rpm \  
&& yum localinstall -y /tmp/opt-mysql4-4.0.30-1.x86_64.rpm \  
&& adduser mysql \  
&& install -d -o mysql -g mysql -m 0755 /var/run/mysqld \  
&& /opt/mysql/bin/mysql_install_db --user=mysql  
  
COPY mysqld_start.sh /opt/mysqld_start.sh  
  
WORKDIR /opt/mysql/bin/  
EXPOSE 3306  
VOLUME "/var/lib/mysql"  
ENTRYPOINT /opt/mysqld_start.sh  

