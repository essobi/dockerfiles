FROM debian:jessie  
MAINTAINER Dave Conroy <dave at tiredofit dot ca>  
  
### Set Environment Variables  
ENV LDAP_LOG_LEVEL=256 \  
LDAP_ORGANISATION="Example Inc." \  
LDAP_DOMAIN=example.org \  
LDAP_BASE_DN= \  
LDAP_ADMIN_PASSWORD=admin \  
LDAP_CONFIG_PASSWORD=config \  
LDAP_READONLY_USER=false \  
LDAP_READONLY_USER_USERNAME=readonly \  
LDAP_READONLY_USER_PASSWORD=readonly \  
LDAP_BACKEND=hdb \  
LDAP_TLS=true \  
LDAP_TLS_CRT_FILENAME=ldap.crt \  
LDAP_TLS_KEY_FILENAME=ldap.key \  
LDAP_TLS_CA_CRT_FILENAME=ca.crt \  
LDAP_TLS_ENFORCE=false \  
LDAP_TLS_CIPHER_SUITE="SECURE256:+SECURE128:-VERS-TLS-ALL:+VERS-
TLS1.2:-RSA:-DHE-DSS:-CAMELLIA-128-CBC:-CAMELLIA-256-CBC" \  
LDAP_TLS_VERIFY_CLIENT=try \  
LDAP_SSL_HELPER_PREFIX=ldap \  
LDAP_REPLICATION=false \  
LDAP_REMOVE_CONFIG_AFTER_SETUP=true \  
LDAP_BACKUP_CONFIG_CRON_PERIOD="0 4 * * *" \  
LDAP_BACKUP_DATA_CRON_PERIOD="0 4 * * *" \  
LDAP_BACKUP_TTL=15 \  
ZABBIX_HOSTNAME=openldap  
  
### Container Setup  
COPY install/debian/dpkg_nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc  
COPY install/debian/dpkg_nolocales /etc/dpkg/dpkg.cfg.d/01_nolocales  
COPY install/debian/complex-bash-env /usr/sbin/complex-bash-env  
  
RUN chmod +x /usr/sbin/complex-bash-env && \  
export INITRD=no && \  
dpkg-divert --local --rename --add /sbin/initctl && \  
ln -sf /bin/true /sbin/initctl && \  
dpkg-divert --local --rename --add /usr/bin/ischroot && \  
ln -sf /bin/true /usr/bin/ischroot && \  
export LC_ALL=C && \  
export DEBIAN_FRONTEND=noninteractive && \  
  
apt-get update && \  
apt-get install -y --no-install-recommends \  
apt-utils \  
locales  
  
RUN apt-get dist-upgrade -y --no-install-recommends && \  
  
locale-gen C.UTF-8 && \  
dpkg-reconfigure locales && \  
/usr/sbin/update-locale LANG=C.UTF-8  
#Setup OpenLDAP user  
RUN groupadd -r openldap && useradd -r -g openldap openldap  
  
### Package Install  
RUN apt-get -y update && \  
LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes \--no-
install-recommends \  
ca-certificates \  
cron \  
curl \  
jq \  
ldap-utils \  
nano \  
nginx \  
openssl \  
python-ldap \  
python-minimal \  
slapd \  
vim-tiny \  
zabbix-agent && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/dpkg/dpkg.cfg.d/02apt-
speedup  
  
## OpenLDAP Setup  
RUN rm -rf /var/lib/ldap  
RUN rm -rf /etc/ldap/slapd.d  
ADD assets/slapd /assets/slapd/  
## OpenLDAP Backup  
ADD assets/cron /assets/cron/  
ADD install/slapd-backup/ /usr/sbin/  
## Log Helpers  
ADD install/loghelper /usr/sbin  
  
## SSL Helpers  
ADD install/ssl-tools /usr/sbin  
ADD assets/ssl-tools /assets/ssl-tools/  
RUN curl -o /usr/sbin/cfssl -SL https://pkg.cfssl.org/R1.2/cfssl_linux-amd64
&& \  
chmod 700 /usr/sbin/cfssl && \  
curl -o /usr/sbin/cfssljson -SL https://pkg.cfssl.org/R1.2/cfssljson_linux-
amd64 && \  
chmod 700 /usr/sbin/cfssljson && \  
chmod +x /usr/sbin/*  
  
## Nginx  
COPY install/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY install/nginx/placeholder.html /www/html/index.html  
  
## Zabbix  
ADD install/sbin/ /usr/sbin  
ADD install/zabbix/ /etc/zabbix  
RUN mkdir -p /var/log/zabbix && \  
chmod +x /etc/zabbix/zabbix_agentd.conf.d/*.sh && \  
chown -R zabbix:root /var/log/zabbix  
  
## Networking  
EXPOSE 80 389 636 10050  
## Entrypoint  
COPY install/run.sh /run.sh  
RUN chmod +x /run.sh  
CMD ["/run.sh"]  
  

