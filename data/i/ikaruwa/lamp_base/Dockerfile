FROM ubuntu:latest  
LABEL name="lamp_base"  
LABEL version="1.0.0"  
LABEL release="0"  
LABEL architecture="Ubuntu 16.04 x86_64"  
LABEL vendor="Nick Fraker <nickdontspam@gmail.com>"  
LABEL vcs-type="git"  
LABEL vcs-url="https://github.com/nfraker/lamp_base"  
LABEL authoritative-source-url="https://hub.docker.com/r/ikaruwa/lamp_base"  
LABEL distribution-scope="public"  
  
# Setup environment  
EXPOSE 80 443  
CMD ["/bin/sh", "-c", "/startup.sh"]  
ENV TERM=xterm LANG=C.UTF-8  
# Update & install  
RUN apt-get update -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-
common  
RUN add-apt-repository ppa:ondrej/php -y  
RUN apt-get update -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 \  
libapache2-mod-php5.6 \  
php5.6 \  
php5.6-mcrypt \  
php5.6-mysql \  
php5.6-gd \  
php5.6-curl \  
php5.6-dev \  
php5.6-memcache \  
php5.6-pspell \  
php5.6-snmp \  
php5.6-mbstring \  
php5.6-dom \  
php5.6-xmlrpc \  
php5.6-cli \  
snmp \  
vim \  
bash-completion \  
mysql-client \  
mysql-server \  
supervisor \  
passwd \  
composer \  
unzip  
RUN apt-get clean  
  
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-
enabled/rewrite.load && \  
unlink /etc/apache2/mods-enabled/autoindex.load &&\  
sed -i 's/Options.*/Options FollowSymLinks/g' /etc/apache2/apache2.conf &&\  
sed -i 's/AllowOverride.*/AllowOverride All/g' /etc/apache2/apache2.conf  
  
# Start services  
RUN echo "service networking start && find /var/lib/mysql -type f -exec touch
{} \; && service mysql start && exec apache2ctl -D FOREGROUND" > /startup.sh
&& \  
chmod +x /startup.sh &&\  
mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/apache2 && \  
chown -R www-data:www-data /var/lock/apache2 /var/run/apache2 /var/log/apache2  
  
# Force resolv.conf  
RUN echo "nameserver 172.17.0.1" > /etc/resolv.conf &&\  
echo "nameserver 8.8.8.8" >> /etc/resolv.conf &&\  
echo "nameserver 8.8.4.4" >> /etc/resolv.conf  
  
# Fix some problematic MySQL configs  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/mysql.conf.d/mysqld.cnf &&
\  
echo '[mysqld]\nskip-host-cache\nskip-name-resolve' >
/etc/mysql/conf.d/docker.cnf && \  
sed -i 's/^password.*/password = rEnmwp1CsUrNWI2X/g' /etc/mysql/debian.cnf  
  
RUN find /var/lib/mysql -maxdepth 1 -mindepth 1 -exec rm -rf {} \; &&\  
mysqld --initialize-insecure &&\  
service mysql start &&\  
mysql -u root -e "CREATE USER 'debian-sys-maint'@'%' IDENTIFIED BY
'rEnmwp1CsUrNWI2X'; GRANT ALL PRIVILEGES ON *.* TO 'debian-sys-maint'@'%';
FLUSH PRIVILEGES;" && \  
find /var/lib/mysql -type f -exec touch {} \;  
  
# Forward Apache logs to stdout  
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \  
ln -sf /proc/self/fd/1 /var/log/apache2/error.log  

