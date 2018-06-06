FROM debian:wheezy  
  
#######################################################################################  
  
# prepare apt and system (first clean is required to prevent gpg keys errors)  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get clean && \  
apt-get update -qq && \  
apt-get install -qqy locales apt-utils ca-certificates wget supervisor && \  
sed -i /etc/locale.gen -e 's/#[ \t]*\\(en_US.UTF-8.*\\)/\1/' && \  
dpkg-reconfigure locales && \  
apt-get upgrade -qqy && \  
apt-get clean  
  
# setting default locale  
ENV LC_ALL en_US.UTF-8  
  
#######################################################################################  
  
# install zarafa  
RUN apt-get update -qq -y && \  
apt-get install -qqy --no-install-recommends wget supervisor && \  
mkdir -p /root/packages && \  
cd /root/packages && \  
wget -q
http://download.zarafa.com/community/final/7.2/7.2.0-48204/zcp-7.2.0-48204-debian-7.0-x86_64-opensource.tar.gz
-O- | tar xz --strip-components=1 && \  
apt-ftparchive packages . | gzip -9c > Packages.gz && \  
echo "deb file:/root/packages /" > /etc/apt/sources.list.d/zarafa.list && \  
apt-get update -qq -y && \  
apt-get install -qqy --force-yes --no-install-recommends mysql-server zarafa
zarafa-webaccess zarafa-webapp && \  
rm /etc/apt/sources.list.d/zarafa.list && \  
rm -Rf /root/packages && \  
apt-get clean  
  
# Install additional Software  
# - postfix (from backports)  
# - system stuff  
# - ldap and php  
# - virus and spam  
# - (optional) better spam detection  
# - (optional) better scanning of attached archive files  
RUN cat /etc/apt/sources.list | sed -e 's/main/non-free/'
>/etc/apt/sources.list.d/debian-non-free.list && \  
echo "deb http://http.debian.net/debian wheezy-backports main"
>/etc/apt/sources.list.d/debian-backports.list && \  
apt-get -qq update && \  
apt-get -qqy -t wheezy-backports --no-install-recommends install postfix
postfix-ldap && \  
apt-get -qq update && apt-get -qqy install --no-install-recommends \  
rsyslog \  
slapd ldap-utils phpldapadmin php5-cli php-soap libapache2-mod-php5 \  
amavisd-new clamav-daemon spamassassin \  
razor pyzor \  
arj bzip2 cabextract cpio file gzip lhasa nomarch pax rar unrar ripole unzip
zip zoo && \  
apt-get clean  
  
  
#######################################################################################  
# configuration variable defaults  
  
# content of certificates for services (if empty snakeoil will be used)  
#ENV CONF_POSTFIX_SSL_CERT  
#ENV CONF_POSTFIX_SSL_KEY  
#ENV CONF_APACHE2_SSL_CERT  
#ENV CONF_APACHE2_SSL_KEY  
#ENV CONF_ZARAFA_SSL_CERT  
#ENV CONF_ZARAFA_SSL_KEY  
  
#ENV CONF_LDAP_PASSWORD  
#ENV CONF_LDAP_BASE_DN  
#ENV CONF_LDAP_DOMAIN  
#ENV CONF_MAIL_DOMAIN  
#ENV CONF_MYSQL_ROOT_PASSWORD  
#ENV CONF_MYSQL_ZARAFA_PASSWORD  
#ENV CONF_MAIL_LOCAL_ALIAS  
  
#######################################################################################  
# debugging  
RUN apt-get install -qqy --force-yes net-tools vim-nox lynx dnsutils  
  
#######################################################################################  
COPY files/ /  
RUN chmod +x /etc/supervisor/scripts/*  
RUN chmod +x /scripts/*  
ENTRYPOINT ["/scripts/docker-entrypoint.sh"]  
CMD ["/scripts/docker-command.sh"]  
#######################################################################################  
# expose ports  
EXPOSE 25  
EXPOSE 443  
EXPOSE 465  
EXPOSE 587  
EXPOSE 993  
#######################################################################################  
  

