FROM ubuntu:trusty  
  
MAINTAINER mnagaku <mnagaku@gmail.com>  
  
RUN echo "Asia/Tokyo" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata && locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
ENV LC_ALL en_US.UTF-8  
  
RUN sed -i".bak" -e 's/\/\/archive.ubuntu.com/\/\/ftp.jaist.ac.jp/g'
/etc/apt/sources.list &&\  
apt-get update && apt-get upgrade -y &&\  
apt-get -y install wget nginx php5-fpm php-apc php5-gd &&\  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* &&\  
echo 'server {\n listen 80 default_server;\n listen [::]:80 default_server
ipv6only=on;\n\n root /var/www/dokuwiki;\n index index.html index.php;\n\n #
Make site accessible from http://localhost/\n server_name localhost;\n\n
location / {\n try_files $uri $uri/ /index.php;\n }\n\n location ~
/(data|conf|bin|inc)/ {\n deny all;\n }\n\n location ~ /\.ht {\n deny all;\n
}\n\n location ~ \.php$ {\n fastcgi_split_path_info ^(.+\.php)(/.+)$;\n #
NOTE: You should have "cgi.fix_pathinfo = 0;" in php.ini\n\n fastcgi_pass
unix:/var/run/php5-fpm.sock;\n fastcgi_param SCRIPT_FILENAME
$document_root$fastcgi_script_name;\n fastcgi_index index.php;\n include
fastcgi_params;\n }\n}\n' > /etc/nginx/sites-available/default && echo
"cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini &&\  
wget http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz &&\  
tar xvzf dokuwiki-stable.tgz &&\  
mv `(ls -1 | grep dokuwiki-2)` dokuwiki&&\  
mkdir /var/www && mv dokuwiki /var/www &&\  
rm -f http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz &&\  
chown -R www-data:www-data /var/www  
  
EXPOSE 80  
  
CMD /usr/sbin/php5-fpm && nginx && sleep 15m && rm -f
/var/www/dokuwiki/install.php ; tail -f /dev/null  

