FROM clubcedille/debian-supervisord  
# Use fixed Fusion Directory package for production  
ENV FUSIONDIRECTORY_DEB_PKG_VERSION=1.0.14* \  
SLDAP_DOMAIN=example.com \  
SLDAP_PASSWORD=toor \  
FUSIONDIRECTORY_PASSWORD=toor2 \  
LDAP_SERVER=configure-me \  
ENABLE_SSL=0  
  
EXPOSE 10080  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y --no-install-recommends gnupg && \  
gpg --keyserver keys.gnupg.net \--recv-keys E184859262B4981F && \  
gpg -a --export E184859262B4981F | apt-key add - && \  
echo 'deb http://repos.fusiondirectory.org/debian-jessie jessie main' >
/etc/apt/sources.list.d/fd.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends php-mdb2 \  
fusiondirectory=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-alias=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-apache2=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-applications=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-argonaut=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-autofs=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-cyrus=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-debconf=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-dhcp=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-dns=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-dovecot=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-dsa=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-ejbca=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-fai=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-freeradius=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-fusioninventory=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-gpg=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-ipmi=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-kolab2=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-mail=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-nagios=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-netgroups=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-opsi=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-personal=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-ppolicy=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-puppet=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-pureftpd=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-quota=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-repository=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-samba=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-sogo=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-squid=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-ssh=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-sudo=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-supann=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-sympa=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-systems=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-weblink=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-plugin-webservice=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
# fusiondirectory-webservice-shell=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-mixedgroups=${FUSIONDIRECTORY_DEB_PKG_VERSION} && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /opt/fusiondirectory  
WORKDIR /opt/fusiondirectory  
COPY apache.conf /etc/apache2/sites-available/000-default.conf  
COPY fusiondirectory.conf /opt/fusiondirectory/fusiondirectory.conf  
COPY /scripts /opt/fusiondirectory/bin  
  
RUN sed -i 's/Listen.*80/Listen 10080/g' /etc/apache2/ports.conf && \  
sed -i 's/Listen 443/Listen 10443/g' /etc/apache2/ports.conf && \  
echo 'Include external-conf.d/*.conf' >> /etc/apache2/apache2.conf && \  
mkdir /etc/apache2/external-conf.d && \  
mkdir -p /var/log/apache2 /var/run/apache2 && \  
./bin/config.sh && \  
chown -R www-data:www-data /etc/fusiondirectory /var/log/apache2
/var/run/apache2  
  
COPY config/httpd-external-conf.d/* /etc/apache2/external-conf.d/.  
  
#setcap 'cap_net_bind_service=+ep' /usr/sbin/apache2  
ENTRYPOINT ["./bin/start.sh"]  

