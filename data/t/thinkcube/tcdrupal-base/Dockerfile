#only ment for develpoment  
FROM centos:7  
MAINTAINER manjula@thinkcube.com  
  
RUN yum clean all  
  
WORKDIR /var/www/html  
  
RUN gpg --keyserver ha.pool.sks-keyservers.net \--recv-keys BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64.asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod 4755 /usr/local/bin/gosu  
  
RUN yum install epel-release http://rpms.remirepo.net/enterprise/remi-
release-7.rpm https://centos7.iuscommunity.org/ius-release.rpm -y \  
&& yum clean all  
  
RUN sed -i "0,/enabled=0/{s/enabled=0/enabled=1/}" /etc/yum.repos.d/remi.repo  
#install apache 2.4.20 from ius repo and install php 5.4.45 from remi repo  
RUN yum install httpd24u php php-gd php-mbstring php-pdo php-mysqlnd php-xml
php-pecl-uploadprogress vim wget -y \  
&& yum clean all  
  
#since we are not using a vhost and we need to process .htaccess file  
RUN sed -i ':a;N;$!ba;s/AllowOverride None/AllowOverride All/2'
/etc/httpd/conf/httpd.conf  
  
RUN echo "IncludeOptional vhost.d/*.conf" >> /etc/httpd/conf/httpd.conf \  
&& sed -i "s|User apache|User user|" /etc/httpd/conf/httpd.conf \  
&& sed -i "s|Group apache|Group user|" /etc/httpd/conf/httpd.conf \  
&& sed -i "s|#ServerName www.example.com:80|ServerName server|"
/etc/httpd/conf/httpd.conf \  
&& sed -i 's/^\\([^#]\\)/#\1/g' /etc/httpd/conf.d/welcome.conf  
  
RUN sed -i "s|;date.timezone =|date.timezone = Asia/Colombo|" /etc/php.ini  
  
RUN useradd --shell /bin/bash -u 1000 -o -c "" -m user \  
&& usermod -aG apache,root user  
  
RUN sed -i "1ialias ls='ls --color'" /home/user/.bashrc \  
&& sed -i "2ialias apachectl='gosu root httpd'" /home/user/.bashrc \  
&& sed -i "3ialias yum='gosu root yum'" /home/user/.bashrc  
  
RUN chmod 770 /var/log/httpd  
  
VOLUME ["/etc/httpd/vhost.d", "/var/www/html"]  
  
EXPOSE 80  
  
COPY run.sh /run.sh  
  
CMD ["/run.sh"]  
  

