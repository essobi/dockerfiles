## -*- docker-image-name: "mcreations/fusiondirectory-ldap" -*-  
  
FROM mcreations/openwrt-ldap  
MAINTAINER Reza Rahimi <rahimi@m-creations.net>  
  
ENV FUSIONDIRECTORY_VERSION 1.0.8.2  
  
ADD image/root/ /  
  
RUN opkg update && opkg install php5-cli perl perlbase-module perlbase-getopt
perlbase-pod && \  
wget -O /tmp/fusiondirectory-${FUSIONDIRECTORY_VERSION}.tar.gz
--progress=dot:giga
https://github.com/fusiondirectory/fusiondirectory/archive/fusiondirectory-${FUSIONDIRECTORY_VERSION}.tar.gz
&& \  
tar -xzf /tmp/fusiondirectory-${FUSIONDIRECTORY_VERSION}.tar.gz -C /tmp/ && \  
wget -O /tmp/fusiondirectory-plugins-${FUSIONDIRECTORY_VERSION}.tar.gz
--progress=dot:giga https://github.com/fusiondirectory/fusiondirectory-
plugins/archive/fusiondirectory-${FUSIONDIRECTORY_VERSION}.tar.gz && \  
tar -xzf /tmp/fusiondirectory-plugins-${FUSIONDIRECTORY_VERSION}.tar.gz -C
/tmp/ && \  
wget -O /tmp/schema2ldif-1.0.tar.gz
https://github.com/fusiondirectory/schema2ldif/archive/1.0.tar.gz && \  
tar -xzf /tmp/schema2ldif-1.0.tar.gz -C /tmp/ && \  
/tmp/schema2ldif-1.0/bin/schema2ldif /tmp/fusiondirectory-
fusiondirectory-${FUSIONDIRECTORY_VERSION}/contrib/openldap/samba.schema >
/etc/openldap/schema-ldif-includes/01-samba.ldif && \  
/tmp/schema2ldif-1.0/bin/schema2ldif /tmp/fusiondirectory-
fusiondirectory-${FUSIONDIRECTORY_VERSION}/contrib/openldap/core-fd.schema >
/etc/openldap/schema-ldif-includes/02-core-fd.ldif && \  
/tmp/schema2ldif-1.0/bin/schema2ldif /tmp/fusiondirectory-
fusiondirectory-${FUSIONDIRECTORY_VERSION}/contrib/openldap/core-fd-
conf.schema > /etc/openldap/schema-ldif-includes/03-core-fd-conf.ldif && \  
/tmp/schema2ldif-1.0/bin/schema2ldif /tmp/fusiondirectory-
fusiondirectory-${FUSIONDIRECTORY_VERSION}/contrib/openldap/recovery-fd.schema
> /etc/openldap/schema-ldif-includes/04-recovery-fd.ldif && \  
/tmp/schema2ldif-1.0/bin/schema2ldif /tmp/fusiondirectory-
fusiondirectory-${FUSIONDIRECTORY_VERSION}/contrib/openldap/ldapns.schema >
/etc/openldap/schema-ldif-includes/05-ldapns.ldif && \  
/tmp/schema2ldif-1.0/bin/schema2ldif /tmp/fusiondirectory-
fusiondirectory-${FUSIONDIRECTORY_VERSION}/contrib/openldap/rfc2307bis.schema
> /etc/openldap/schema-ldif-includes/06-rfc2307bis.ldif && \  
for f in `ls /tmp/fusiondirectory-plugins-
fusiondirectory-${FUSIONDIRECTORY_VERSION}/*/contrib/openldap/*.schema | grep
-v conf` ; do bn=$(basename $f .schema); /tmp/schema2ldif-1.0/bin/schema2ldif
$f &> /etc/openldap/schema-ldif-includes/80-$bn.ldif; done &&\  
for f in `ls /tmp/fusiondirectory-plugins-
fusiondirectory-${FUSIONDIRECTORY_VERSION}/*/contrib/openldap/*.schema | grep
conf` ; do bn=$(basename $f .schema); /tmp/schema2ldif-1.0/bin/schema2ldif $f
&> /etc/openldap/schema-ldif-includes/81-$bn.ldif; done &&\  
rm -rf /tmp/schema2ldif-1.0 && \  
rm -rf /tmp/fusiondirectory-fusiondirectory-${FUSIONDIRECTORY_VERSION} && \  
rm -rf /tmp/fusiondirectory-plugins-fusiondirectory-${FUSIONDIRECTORY_VERSION}
&& \  
opkg remove --force-depends perlbase-getopt perlbase-pod perlbase-module perl  
  
  
EXPOSE 389  
  
CMD ["/start-slapd-fd"]  

