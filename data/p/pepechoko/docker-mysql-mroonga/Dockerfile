FROM centos:centos6  
MAINTAINER pepechoko  
  
# rpmforge && epel install  
RUN \  
rpm --import http://apt.sw.be/RPM-GPG-KEY.dag.txt && \  
rpm -ivh http://apt.sw.be/redhat/el6/en/x86_64/rpmforge/RPMS/rpmforge-
release-0.5.3-1.el6.rf.x86_64.rpm && \  
rpm -ivh http://ftp-
srv2.kddilabs.jp/Linux/distributions/fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
RUN yum install -y \  
supervisor \  
which  
  
RUN \  
rpm -ivh http://packages.groonga.org/centos/groonga-release-1.1.0-1.noarch.rpm
&& \  
rpm -ivh http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm  
  
# RUN yum install -y --disablerepo=* --enablerepo=groonga \  
RUN yum install -y --enablerepo=epel,mysql56 \  
mysql \  
mysql-devel \  
mysql-server \  
mysql-utilities \  
mysql-community-mroonga \  
groonga-tokenizer-mecab \  
mecab \  
mecab-devel \  
mecab-ipadic \  
groonga-libs \  
groonga-tokenizer-mecab \  
groonga-normalizer-mysql  
  
RUN mkdir -p \  
/var/log/mysql \  
/var/log/supervisor  
  
#RUN \  
# service mysqld start && \  
# sleep 5s && \  
# mysql -e "GRANT ALL ON *.* to 'root'@'%'; FLUSH PRIVILEGES"  
# VOLUME /var/lib/mysql  
RUN \  
rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3306  
# CMD ["mysqld"]  
#CMD ["/usr/bin/mysqld_safe"]  
CMD ["mysqld_safe"]  

