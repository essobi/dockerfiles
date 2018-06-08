FROM marklee77/supervisor:jessie  
LABEL maintainer="Mark Stillwell <mark@stillwell.me>"  
  
RUN groupadd -g 200 openldap && \  
useradd -u 200 -g 200 -r openldap && \  
apt-get update && \  
apt-get -y install --no-install-recommends \  
ca-certificates \  
ldap-utils \  
pwgen \  
slapd && \  
rm -rf \  
/etc/ldap/ldap.conf \  
/etc/ldap/slapd.d/* \  
/var/cache/apt/* \  
/var/lib/apt/lists/* \  
/var/lib/ldap/*  
  
RUN mkdir -m 0755 -p /etc/ssl/slapd /etc/ldap/dbinit.d  
  
COPY root/etc/my_init.d/10-slapd-setup /etc/my_init.d/  
COPY root/usr/local/sbin/slapd-run /usr/local/sbin/  
RUN chmod 0755 /etc/my_init.d/10-slapd-setup /usr/local/sbin/slapd-run  
  
COPY root/etc/supervisor/conf.d/slapd.conf /etc/supervisor/conf.d/  
RUN chmod 0644 /etc/supervisor/conf.d/slapd.conf  
  
EXPOSE 389 636  
VOLUME ["/etc/ldap/slapd.d", "/var/lib/ldap"]  

