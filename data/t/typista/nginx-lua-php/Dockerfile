#http://qiita.com/hnakamur/items/0b72590136cece29faee  
FROM typista/nginx-lua  
#FROM typista/nginx-lua:0.7  
RUN wget https://raw.githubusercontent.com/typista/docker-nginx-lua-
php/master/files/entrypoint.sh -O /etc/entrypoint.sh && \  
chmod +x /etc/entrypoint.sh && \  
rpm -Uvh http://ftp.iij.ad.jp/pub/linux/fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm && \  
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm && \  
yum update -y && \  
yum install -y --enablerepo=remi,remi-php56,epel php php-cgi php-common && \  
yum install -y --enablerepo=remi,remi-php56,epel php-gd php-fpm php-opcache
php-devel php-mbstring php-mcrypt php-mysqlnd && \  
yum install -y --enablerepo=remi,remi-php56,epel php-phpunit-PHPUnit php-pecl-
xdebug php-pecl-xhprof && \  
yum install -y --enablerepo=epel pngquant && \  
touch /etc/yum.repos.d/dag.repo && \  
echo '[dag]' >> /etc/yum.repos.d/dag.repo && \  
echo 'name=Dag RPM Repository for redhat' >> /etc/yum.repos.d/dag.repo && \  
echo
'baseurl=http://ftp.riken.jp/Linux/dag/redhat/el$releasever/en/$basearch/dag'
>> /etc/yum.repos.d/dag.repo && \  
echo 'enabled=0' >> /etc/yum.repos.d/dag.repo && \  
echo 'gpgcheck=1' >> /etc/yum.repos.d/dag.repo && \  
echo 'gpgkey=http://dag.wieers.com/packages/RPM-GPG-KEY.dag.txt' >>
/etc/yum.repos.d/dag.repo && \  
yum --enablerepo=dag install -y gifsicle && \  
yum install -y libjpeg-turbo-devel libjpeg.x86_64 libjpeg-devel.x86_64
libpng.x86_64 libpng-devel.x86_64 giflib.x86_64 giflib-devel.x86_64
libxml2.x86_64 libxml2-devel.x86_64 libxslt.x86_64 libxslt-devel.x86_64
zlib.x86_64 zlib-devel.x86_64 freetype.x86_64 freetype-devel.x86_64 && \  
mkdir -p /var/run/nginx/ && \  
wget http://www.imagemagick.org/download/ImageMagick.tar.gz -O
/root/ImageMagick.tar.gz && \  
cd /root && \  
tar zxvf ImageMagick.tar.gz && \  
cd ImageMagick-6.9.0-2 && \  
./configure --prefix=/usr/local/ && \  
make && \  
make install && \  
ldconfig /usr/local/lib && \  
rm /root/ImageMagick.tar.gz && \  
pecl install imagick && \  
pecl install mongo  
#EXPOSE 80  
#ENTRYPOINT /etc/entrypoint.sh  

