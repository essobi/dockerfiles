FROM centos:6  
MAINTAINER Thatcher Peskens <thatcher@koffiedik.net>, domainer  
  
# install epel  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# patch the system  
RUN yum clean all  
RUN yum -y update  
  
# set timezone to PRC  
RUN mv /etc/localtime /etc/localtime.bak  
RUN ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
# install NTP  
RUN yum -y install ntp  
RUN chkconfig ntpd on  
RUN service ntpd start  
  
# install util  
RUN yum -y install wget which vim-enhanced unzip expect  
  
### selinux is disabled by default, so we don't need the following  
# enable sendmail for httpd  
#RUN setsebool -P httpd_can_sendmail 1  
# enable network connection from httpd (literally php curl)  
#RUN setsebool -P httpd_can_network_connect on  
# install jdk  
RUN yum -y install java-1.7.0-openjdk.x86_64  
  
# install tomcat  
RUN yum -y install tomcat6 tomcat6-webapps tomcat6-admin-webapps tomcat6-docs-
webapp tomcat6-javadoc  
# set decoding in URI  
RUN sed -ri '/<Connector port="8080"
protocol="HTTP\/1.1"/a\\\URIEncoding="UTF-8"'
/usr/share/tomcat6/conf/server.xml  
RUN chkconfig tomcat6 on  
RUN service tomcat6 start  
  
# install httpd  
RUN yum -y install httpd mod_ssl  
# disable logs, enable name-based virtual hosting, disable SSLv3 because of
POODLE vulnerability  
RUN sed -ri -e 's/^ServerTokens OS/ServerTokens Prod/' -e 's/^ServerSignature
On/ServerSignature Off/' -e 's/^CustomLog logs/#CustomLog logs/' -e
's/^ErrorLog logs/#ErrorLog logs/' -e '$a\\\NameVirtualHost
*:80\nNameVirtualHost *:443\n\nSSLProtocol All -SSLv2 -SSLv3'
/etc/httpd/conf/httpd.conf  
RUN chkconfig httpd on  
RUN service httpd start  
  
# install php  
RUN yum -y install php php-pdo php-mysql php-gd php-imap php-ldap php-odbc
php-pear php-xml php-xmlrpc php-mbstring php-mcrypt php-bcmath php-mhash
libmcrypt  
# set timezone, enable short tag  
RUN sed -ri -e 's/^;date.timezone =/date.timezone = PRC/' -e
's/^short_open_tag = Off/short_open_tag = On/' /etc/php.ini  
  
# install mysql  
RUN yum -y install mysql mysql-server  
#RUN echo "NETWORKING=yes" > /etc/sysconfig/network  
RUN chkconfig mysqld on  
RUN service mysqld start  
  
# install redis  
RUN yum -y install gcc gcc-c++ tcl  
RUN (cd ~ && wget http://download.redis.io/redis-stable.tar.gz -O - | tar xz)  
RUN (cd ~/redis-stable/deps && make hiredis jemalloc linenoise lua && cd .. &&
make && make test && make install)  
  
# setup redis  
RUN mkdir -p /etc/redis /var/redis  
RUN cp ~/redis-stable/utils/redis_init_script /etc/init.d/redis  
RUN cp ~/redis-stable/redis.conf /etc/redis/6379.conf  
RUN sed -ri -e 's/^pidfile \/var\/run\/redis.pid/pidfile
\/var\/run\/redis_6397.pid/' -e 's/^daemonize no/daemonize yes/' -e
's/^logfile ""/logfile "\/var\/log\/redis.log"/' -e 's/^dir .\//dir
\/var\/redis/' -e 's/^# bind 127.0.0.1/bind 127.0.0.1/' /etc/redis/6379.conf  
RUN sed -ri '2i\\# chkconfig: 2345 90 10\n# description: Redis is a persistent
key-value database' /etc/init.d/redis  
  
RUN chkconfig redis on  
RUN service redis start  
EXPOSE 6379  
# install phpredis  
RUN yum -y install php-devel  
RUN (cd ~ && wget https://github.com/nicolasff/phpredis/archive/master.zip)  
RUN (cd ~ && unzip master.zip && cd ~/phpredis-master && phpize && ./configure
&& make && make test && make install)  
RUN echo "extension=redis.so" > /etc/php.d/redis.ini  
  
# install vncserver  
RUN yum -y install tigervnc-server  
RUN yum -y groupinstall Desktop  
RUN yum -y install firefox xterm  
RUN useradd vncuser  
RUN sed -ri '$a\\\VNCSERVERS="1:vncuser"\nVNCSERVERARGS[1]="-geometry
1024x768"' /etc/sysconfig/vncservers  
# not recommend to start up vncserver by default  
# RUN chkconfig vncserver on  
# RUN service vncserver restart  
# install supervisord  
RUN yum -y install python-pip && pip install "pip>=1.4,<1.5" \--upgrade  
RUN pip install supervisor  
  
# install sshd  
RUN yum -y install openssh-server openssh-clients passwd  
  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && ssh-keygen -q
-N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN sed -ri 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config && echo
'root:changeme' | chpasswd  
  
ADD phpinfo.php /var/www/html/  
ADD supervisord.conf /etc/  
EXPOSE 22 80  
CMD ["supervisord", "-n"]  

