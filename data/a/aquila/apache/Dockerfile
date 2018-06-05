# aquila/apache  
  
FROM ubuntu:xenial  
  
MAINTAINER Andreas Lang <andreas.lang@aquilainsight.com>  
  
ENV TERM=xterm \  
APACHE2_SERVER_NAME=ci.aquilainsight.com \  
DEBIAN_FRONTEND=noninteractive \  
SAML_USER_PROPERTY="user" \  
SAML_EMAIL_PROPERTY="mail" \  
SAML_DISPLAYNAME_PROPERTY="displayname" \  
MOD_SECURITY_ENABLED="true" \  
MOD_EVASIVE_ENABLED="true"  
  
ADD apache/owasp-modsecurity-crs-master.tar.gz /opt/owasp-modsecurity-crs-
master  
  
RUN apt-get update && apt-get install -y \  
apache2 \  
clamav \  
clamav-daemon \  
gcc \  
libapache2-mod-auth-mellon \  
libapache2-mod-evasive \  
libapache2-mod-security2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /etc/apache2/ssl \  
&& cp -r /opt/owasp-modsecurity-crs-master/* /etc/modsecurity/ \  
&& mv /etc/modsecurity/modsecurity_crs_10_setup.conf.example
/etc/modsecurity/modsecurity_crs_10_setup.conf \  
&& ls /etc/modsecurity/base_rules | xargs -I {} ln -s
/etc/modsecurity/base_rules/{} /etc/modsecurity/activated_rules/{} \  
&& ls /etc/modsecurity/optional_rules | xargs -I {} ln -s
/etc/modsecurity/optional_rules/{} /etc/modsecurity/activated_rules/{} \  
&& mkdir /var/log/mod_evasive \  
&& chown www-data:www-data /var/log/mod_evasive \  
&& freshclam \  
&& cd /opt/owasp-modsecurity-crs-master/util/av-scanning/runAV \  
&& ./comp \  
&& ln -s /opt/owasp-modsecurity-crs-master/util/av-scanning/runAV/runAV
/bin/runAV \  
&& mkdir -p /opt/modsecurity/var/upload/ \  
&& chown www-data:www-data /opt/modsecurity/var/upload/ \  
&& apt-get purge -y gcc \  
&& apt-get auto-remove -y  
  
RUN a2dissite 000-default \  
&& a2enmod env \  
evasive \  
headers \  
rewrite \  
security2 \  
ssl  
  
COPY apache/apache2.conf /etc/apache2/apache2.conf  
COPY apache/ssl-reverse-proxy-generic.conf /etc/apache2/ssl-reverse-proxy-
generic.conf  
COPY apache/reverse-proxy-generic.conf /etc/apache2/reverse-proxy-generic.conf  
COPY apache/aquilla-ssl.conf /etc/apache2/aquilla-ssl.conf  
COPY apache/security.conf /etc/apache2/conf-enabled/security.conf  
COPY apache/modsecurity.conf /etc/modsecurity/modsecurity.conf  
COPY apache/security2.conf /etc/apache2/mods-available/security2.conf  
COPY apache/sso.conf /etc/apache2/sso.conf.template  
COPY sso/mellon_create_metadata.sh /etc/apache2/  
  
ENV PGPASSFILE="/srv/.pgpass"  
RUN touch $PGPASSFILE \  
&& chmod 600 $PGPASSFILE \  
&& chown www-data:www-data $PGPASSFILE \  
&& echo "export PGPASSFILE=$PGPASSFILE" >> /etc/apache2/envvars \  
&& mkdir /etc/apache2/mellon-idp \  
&& mkdir /etc/apache2/mellon-sp  
  
  
COPY run-apache.sh /srv/run-apache.sh  
RUN chmod u+x /srv/run-apache.sh \  
&& ln -sf /dev/stdout /var/log/apache2/access.log \  
&& ln -sf /dev/stderr /var/log/apache2/error.log  
  
CMD /srv/run-apache.sh  

