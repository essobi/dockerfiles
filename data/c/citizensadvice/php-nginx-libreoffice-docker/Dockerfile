FROM centos:7  
  
ENV NODEJS_DOWNLOAD_SHA256
159e5485d0fb5c913201baae49f68fd428a7e3b08262e9bf5003c1b399705ca8  
  
RUN yum update -y && \  
yum install -y epel-release wget && \  
wget https://rpms.remirepo.net/enterprise/remi-release-7.rpm && \  
rpm -ivh remi-release-7.rpm && \  
yum update -y && \  
yum install -y python-pip php56 php56-php php56-php-devel php56-php-fpm
php56-php-gd \  
php56-php-intl php56-php-mbstring php56-php-mcrypt php56-php-mysqlnd \  
php56-php-opcache php56-php-pecl-apcu php56-php-soap php56-php-xml \  
php56-php-odbc php56-php-redis gcc-c++ git make patch \  
freetds unixODBC unixODBC-devel libtool-ltdl libtool-ltdl-devel nginx \  
ruby ruby-devel ruby-libs mysql zip unzip bind-utils nmap dnsmasq && \  
yum install -y libreoffice vim mailx sendmail && \  
yum clean -y all  
  
RUN mkdir /etc/dhcp/ && \  
echo 'prepend domain-name-servers 127.0.0.1;' >> /etc/dhcp/dhclient.conf && \  
ln -s /usr/bin/php56 /usr/bin/php && \  
ln -s /opt/remi/php56/root/usr/sbin/php-fpm /usr/bin/php-fpm && \  
ln -s /usr/bin/ruby /usr/share/ruby  
  
RUN pip install pyentrypoint && sed -i -e "/self._rm_dockerenv()/d"
/lib/python2.7/site-packages/pyentrypoint/command.py  
  
RUN wget
https://nodejs.org/download/release/v0.10.33/node-v0.10.33-linux-x64.tar.gz &&
\  
echo "$NODEJS_DOWNLOAD_SHA256 node-v0.10.33-linux-x64.tar.gz" | sha256sum -c -
&& \  
tar \--strip-components 1 -xzvf node-v* -C /usr/local && \  
npm -gf install grunt && \  
npm -gf install grunt-cli && \  
rm -f node-v0.10.33-linux-x64.tar.gz  
  
RUN pip install awscli \--upgrade --user  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php \-- --install-
dir=/usr/local/bin --filename=composer  

