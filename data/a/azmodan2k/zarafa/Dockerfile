FROM azmodan2k/zarafabase:latest  
MAINTAINER azmodan2k "work@azmodan.com"  
# ORIGINAL MAINTAINER Tobias Mandjik <webmaster@leckerbeef.de>  
# noninteractive Installation (dont't touch this)  
ENV DEBIAN_FRONTEND noninteractive  
  
# Password Settings (root User and LDAP)  
ENV LB_ROOT_PASSWORD topSecret  
ENV LB_LDAP_PASSWORD topSecret  
  
# MySQL Settings  
ENV LB_MYSQL_PASSWORD topSecret  
  
# Uncomment to use external MySQL-Server  
# used password is LB_MYSQL_PASSWORD  
#  
# This feature is not supported at the  
# moment  
#ENV LB_EXT_MYSQL yes  
#ENV LB_EXT_MYSQL_SERVER 172.27.0.1  
#ENV LB_EXT_MYSQL_PORT 3306  
#ENV LB_EXT_MYSQL_USER root  
#ENV LB_EXT_MYSQL_DB zarafaExt  
# Maildomain Settings  
ENV LB_LDAP_DN dc=mydomain,dc=net  
ENV LB_MAILDOMAIN mydomain.net  
  
# Relayhost Settings  
ENV LB_RELAYHOST smtp.relayhost.com  
ENV LB_RELAYHOST_USERNAME FooMyAuthUser  
ENV LB_RELAYHOST_PASSWORD BarAuthPassword  
  
# SSL Settings  
ENV LB_SSL_COMPANY My Company Ltd.  
# COUNTRY MUST ONLY CONTAIN 2 LETTERS!  
ENV LB_SSL_COUNTRY US  
ENV LB_SSL_LOCATION Springflied  
  
# Zarafa License (25 Digits)  
# uncommented if you have a commercial license  
#ENV LB_ZARAFA_LICENSE 12345123451234512345  
# Install additional Software (+ decoders for amavis)  
RUN DEBIAN_FRONTEND=noninteractive apt-get -q update && apt-get -yqq install \  
rsyslog curl ssh fetchmail postfix postfix-ldap amavisd-new clamav-daemon \  
spamassassin razor pyzor slapd ldap-utils phpldapadmin php5-cli php-soap \  
arj bzip2 cabextract cpio file gzip lhasa nomarch pax unrar-free ripole unzip
\  
zip zoo rpm2cpio lzop xzdec lzma \  
sasl2-bin  
  
# Add configuration files  
ADD /config/amavis/15-content_filter_mode
/etc/amavis/conf.d/15-content_filter_mode  
ADD /config/amavis/20-debian_defaults /etc/amavis/conf.d/20-debian_defaults  
ADD /config/postfix/ldap-aliases.cf /etc/postfix/ldap-aliases.cf  
ADD /config/postfix/ldap-users.cf /etc/postfix/ldap-users.cf  
ADD /config/postfix/main.cf /etc/postfix/main.cf  
ADD /config/postfix/master.cf /etc/postfix/master.cf  
ADD /config/postfix/sasl/smtpd.conf /etc/postfix/sasl/smtpd.conf  
ADD /config/saslauthd/default/saslauthd /etc/default/saslauthd  
ADD /config/saslauthd/saslauthd.conf /etc/saslauthd.conf  
ADD /config/ldap/ldap.ldif /usr/local/bin/ldap.ldif  
ADD /config/ldap/fetchmail.ldif /etc/ldap/schema/fetchmail.ldif  
ADD /config/ldap/fetchmail.schema /etc/ldap/schema/fetchmail.schema  
ADD /config/apache/z-push.conf /etc/apache2/sites-available/z-push.conf  
ADD /config/apache/default-ssl.conf /etc/apache2/sites-available/default-
ssl.conf  
ADD /config/apache/000-default.conf /etc/apache2/sites-
available/000-default.conf  
  
# Add Scripts  
ADD /script/init.sh /usr/local/bin/init.sh  
ADD /script/fetchmail.sh /usr/local/bin/fetchmail.sh  
ADD /script/ssl-cert.sh /usr/local/bin/ssl-cert.sh  
  
RUN chmod 777 /usr/local/bin/init.sh /usr/local/bin/ssl-cert.sh  
RUN echo "yes" > /usr/local/bin/firstrun  
  
# Entry-Script  
ADD /script/entry.sh /usr/local/bin/entry.sh  
CMD ["/usr/local/bin/entry.sh"]  
  
# Expose Ports  
EXPOSE 236  
EXPOSE 237  
EXPOSE 22  
EXPOSE 80  
EXPOSE 443  
EXPOSE 389  
# Set Entrypoint  
ENTRYPOINT ["/bin/bash"]  

