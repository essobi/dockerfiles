FROM marklee77/slapd:jessie  
LABEL maintainer="Mark Stillwell <mark@stillwell.me>"  
  
RUN apt-key adv --keyserver pool.sks-keyservers.net --recv-key
0xD744D55EACDA69FF && \  
echo "deb http://repos.fusiondirectory.org/fusiondirectory-current/debian-
jessie jessie main" > \  
/etc/apt/sources.list.d/fusiondirectory.list && \  
echo "deb http://repos.fusiondirectory.org/fusiondirectory-extra/debian-jessie
jessie main" >> \  
/etc/apt/sources.list.d/fusiondirectory.list && \  
apt-get update && \  
apt-get -y install --no-install-recommends \  
fusiondirectory \  
fusiondirectory-schema \  
fusiondirectory-plugin-alias \  
fusiondirectory-plugin-alias-schema \  
fusiondirectory-plugin-audit \  
fusiondirectory-plugin-audit-schema \  
fusiondirectory-plugin-certificates \  
fusiondirectory-plugin-community \  
fusiondirectory-plugin-community-schema \  
fusiondirectory-plugin-dns \  
fusiondirectory-plugin-dns-schema \  
fusiondirectory-plugin-dovecot \  
fusiondirectory-plugin-dovecot-schema \  
fusiondirectory-plugin-dsa \  
fusiondirectory-plugin-dsa-schema \  
fusiondirectory-plugin-gpg \  
fusiondirectory-plugin-gpg-schema \  
fusiondirectory-plugin-ldapdump \  
fusiondirectory-plugin-ldapmanager \  
fusiondirectory-plugin-mail \  
fusiondirectory-plugin-mail-schema \  
fusiondirectory-plugin-mixedgroups \  
fusiondirectory-plugin-netgroups \  
fusiondirectory-plugin-netgroups-schema \  
fusiondirectory-plugin-newsletter \  
fusiondirectory-plugin-newsletter-schema \  
fusiondirectory-plugin-personal \  
fusiondirectory-plugin-personal-schema \  
fusiondirectory-plugin-postfix \  
fusiondirectory-plugin-postfix-schema \  
fusiondirectory-plugin-ppolicy \  
fusiondirectory-plugin-ppolicy-schema \  
fusiondirectory-plugin-quota \  
fusiondirectory-plugin-quota-schema \  
fusiondirectory-plugin-ssh \  
fusiondirectory-plugin-ssh-schema \  
fusiondirectory-plugin-sudo \  
fusiondirectory-plugin-sudo-schema \  
fusiondirectory-plugin-sympa \  
fusiondirectory-plugin-sympa-schema \  
fusiondirectory-plugin-systems \  
fusiondirectory-plugin-systems-schema \  
fusiondirectory-plugin-weblink \  
fusiondirectory-plugin-weblink-schema \  
fusiondirectory-schema \  
fusiondirectory-smarty3-acl-render \  
fusiondirectory-theme-oxygen \  
fusiondirectory-webservice-shell \  
libapache2-mod-php5 \  
php-mdb2 && \  
rm -rf \  
/etc/fusiondirectory/fusiondirectory.conf \  
/etc/fusiondirectory/fusiondirectory.passwd \  
/var/cache/apt/* \  
/var/lib/apt/lists/*  
  
COPY root/etc/ldap/dbinit.d/10-fusiondirectory /etc/ldap/dbinit.d/  
RUN chmod 0755 /etc/ldap/dbinit.d/10-fusiondirectory  
COPY root/etc/supervisor/conf.d/apache2.conf /etc/supervisor/conf.d/  
RUN chmod 0644 /etc/supervisor/conf.d/apache2.conf  
  
EXPOSE 80  

