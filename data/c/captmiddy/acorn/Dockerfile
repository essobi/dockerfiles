FROM amazonlinux  
MAINTAINER "Anthony Moulen <amoulen@g.harvard.edu>"  
RUN yum -y install git php56 mod24_ssl mysql-server php56-mysqlnd python
python-setuptools php56-xml php56-xmlrpc && \  
easy_install-2.6 supervisor && \  
chkconfig httpd on ; chkconfig mysqld on && \  
echo "NETWORKING=yes" >/etc/sysconfig/network && \  
service mysqld start && \  
mysqladmin -u root password 'docrootpw1'  
ADD application /acorn/application  
ADD public /acorn/public  
ADD acorn_sessions /acorn/acorn_sessions  
ADD library /acorn/library  
ADD logs /acorn/logs  
ADD test /acorn/test  
ADD .htaccess /acorn/.htaccess  
ADD acorn_setup.sh /acorn/acorn_setup.sh  
ADD acorn_tables.sql /acorn/acorn_tables.sql  
ADD docker/supervisord.conf /etc/supervisord.conf  
ADD docker/acornhost.conf /etc/httpd/conf.d/vhost_acorn.conf  
ADD docker/config.php /acorn/public/config.php  
ADD docker/dockerenv.sh /acorn/dockerenv.sh  
ADD docker/index_update.php /acorn/index_update.php  
ADD docker/genssl.sh /acorn/genssl.sh  
ADD docker/acornhostssl.conf /etc/httpd/conf.d/vhost_acorn_ssl.conf  
WORKDIR /acorn  
RUN service mysqld start && \  
chmod a+rw application && \  
chmod a+x *.sh && \  
source ./dockerenv.sh ; \  
./acorn_setup.sh -s && \  
chmod a+rw application/config.ini && \  
sed -i 's/^require/#INSERTCHANGE\nrequire/' public/index.php && \  
sed -i '/#INSERTCHANGE/r index_update.php' public/index.php && \  
./genssl.sh > keylog.txt 2>&1  
EXPOSE 8443 80  
CMD ["/usr/local/bin/supervisord", "--configuration=/etc/supervisord.conf"]  

