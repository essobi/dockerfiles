FROM debian:jessie  
  
MAINTAINER Xtremxpert <xtremxpert@xtremxpert.com>  
  
ENV MAX_UPLOAD="50M" \  
DEBIAN_FRONTEND="noninteractive" \  
# LANG="fr_CA.UTF-8" \  
# LC_ALL="fr_CA.UTF-8" \  
# LANGUAGE="fr_CA.UTF-8" \  
TZ="America/Toronto" \  
TERM="xterm"  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
apache2 \  
ca-certificates \  
curl \  
dialog\  
gettext \  
libapache2-mod-php5 \  
locales \  
logrotate \  
man \  
manpages \  
mc \  
nano \  
# ncurse \  
# openssh-server \  
php5 \  
php5-curl \  
php5-gd \  
php5-mysqlnd \  
php5-sqlite \  
php5-tidy \  
php5-xsl \  
rsync \  
supervisor \  
tar \  
tzdata\  
# unrar \  
unzip \  
vim \  
wget \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
echo $TZ > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
echo 'alias ll="ls -lah --color=auto"' >> /etc/bash.bashrc && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
echo "fr_CA.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen && \  
update-locale LANG=fr_CA.UTF-8  
  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd
/var/log/supervisor  
  
RUN sed -i 's#AllowOverride none#AllowOverride All#' /etc/apache2/apache2.conf
&& \  
sed -i 's#^DocumentRoot ".*#DocumentRoot "/var/www/htdocs"#g'
/etc/apache2/apache2.conf && \  
sed -i 's#output_buffering = 4096#output_buffering = Off#'
/etc/php5/apache2/php.ini && \  
sed -i \  
-e "s/^upload_max_filesize\s*=\s*2M/upload_max_filesize = $MAX_UPLOAD/" \  
-e "s/^post_max_size\s*=\s*8M/post_max_size = $MAX_UPLOAD/" \  
/etc/php5/apache2/php.ini  
  
RUN a2dismod mpm_event && \  
a2enmod mpm_prefork \  
ssl \  
rewrite && \  
a2ensite default-ssl && \  
ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log  
  
COPY files/test.php /var/www/html/  
COPY files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 80  
EXPOSE 443  
  
CMD ["/usr/bin/supervisord"]  

