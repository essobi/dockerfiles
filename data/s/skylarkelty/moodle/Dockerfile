FROM skylarkelty/centos:latest  
MAINTAINER "Skylar Kelty" <s.kelty@kent.ac.uk>  
ADD ./shared/files/remi.repo /etc/yum.repos.d/remi.repo  
ADD ./shared/files/nginx.repo /etc/yum.repos.d/nginx.repo  
ADD ./shared/files/supervisord.service /etc/systemd/system/multi-
user.target.wants/supervisord.service  
RUN mkdir -p /etc/ssl/certs/  
RUN mkdir -p /etc/ssl/private/  
ADD ./shared/files/ssc /etc/ssl/certs/nginx-selfsigned.crt  
ADD ./shared/files/ssk /etc/ssl/private/nginx-selfsigned.key  
ADD ./shared/files/ssp /etc/ssl/certs/dhparam.pem  
RUN yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm \  
nginx ImageMagick aspell texlive-latex graphviz mimetex cronie python-
setuptools \  
&& yum clean all  
RUN curl https://packages.microsoft.com/config/rhel/7/prod.repo | tee
/etc/yum.repos.d/mssql-tools.repo  
RUN yum update -y && yum clean all  
RUN ACCEPT_EULA=Y yum install -y msodbcsql && yum clean all  
RUN easy_install supervisor  
RUN yum-config-manager --enable remi-php71 && \  
yum install -y php71 php71-php-fpm php71-php-opcache php71-php-cli \  
php71-php-gd php71-php-pdo php71-php-xml php71-php-intl php71-php-pear \  
php71-php-soap php71-php-xmlrpc php71-php-process php71-php-mysqlnd \  
php71-php-mbstring php71-php-ldap php71-php-mcrypt php71-php-sqlsrv \  
php71-php-pecl-memcache php71-php-pecl-memcached php71-php-pecl-solr2 \  
php71-php-pecl-mongodb php71-php-pecl-redis php71-php-pecl-zip php71-php-
xdebug \  
php71-php-pecl-event && yum clean all  
RUN ln -s /usr/bin/php71 /usr/bin/php && \  
ln -s /usr/bin/php71-cgi /usr/bin/php-cgi && \  
ln -s /usr/bin/php71-pear /usr/bin/php-pear && \  
ln -s /usr/bin/php71-phar /usr/bin/php-phar  
ADD ./shared/phpredmin /var/www/vhosts/moodle-dev.kent.ac.uk/phpredmin  
ADD ./shared/simplesamlphp /var/www/vhosts/moodle-
dev.kent.ac.uk/sp/simplesamlphp  
ADD ./shared/puppet /puppet  
RUN yum install -y puppet && \  
puppet apply --modulepath=/puppet/modules /puppet/manifests/site.pp && \  
yum remove -y puppet && yum clean all  
RUN date > /etc/docker-release  
  
# Reinstall glibc-common to make sure the locale required for unit testing is
installed  
RUN yum reinstall -q -y glibc-common  
RUN localedef --quiet -c -i /usr/share/i18n/locales/en_AU -f UTF-8 en_AU  
RUN localedef --quiet -c -i /usr/share/i18n/locales/en_GB -f UTF-8 en_GB  
RUN localedef --quiet -c -i /usr/share/i18n/locales/en_US -f UTF-8 en_US  
  
# Support Moodle-perf-comparison  
RUN yum install -y git mariadb && yum clean all  
  
# Support Snark dev.  
RUN yum install -y libreoffice libreoffice-pyuno libreoffice-ure && yum clean
all  
RUN curl -SsL
https://raw.githubusercontent.com/dagwieers/unoconv/master/unoconv >
/usr/local/bin/unoconv  
RUN chmod 0755 /usr/local/bin/unoconv  
  
EXPOSE 22 80 443  
CMD ["/usr/sbin/init"]  

