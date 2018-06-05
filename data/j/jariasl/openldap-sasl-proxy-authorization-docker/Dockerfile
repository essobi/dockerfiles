FROM ubuntu:16.04  
MAINTAINER Jorge Arias <mail@jorgearias.cl>  
  
ARG LDAP_SERVERS=ldap://ad.example.com:389/  
ARG LDAP_SEARCH_BASE=CN=DomainUsers,DC=example,DC=com  
ARG LDAP_TIMEOUT=10  
ARG LDAP_FILTER=(sAMAccountName=%U)  
ARG LDAP_BIND_DN=CN=Administrator,CN=Users,DC=example,DC=com  
ARG LDAP_PASSWORD=ADpassword  
  
ARG LDAP_DN_BASE=dc=my-domain,dc=com  
ARG LDAP_ORGANIZATION=Example  
ARG LDAP_ROOT_DN=cn=Manager,dc=my-domain,dc=com  
ARG LDAP_DATABASE=hdb  
ARG LDAP_ROOT_PW=secret  
  
ENV OPENLDAP_VERSION 2.4.44  
RUN apt-get update && apt-get install -y \  
curl \  
build-essential \  
groff-base \  
libdb-dev \  
libssl1.0.0 libssl-dev libiodbc2 libiodbc2-dev libsasl2-2 libsasl2-dev \  
sasl2-bin  
  
RUN sed -i 's/MECHANISMS="pam"/MECHANISMS="ldap"/' /etc/default/saslauthd \  
&& sed -i 's/START=no/START=yes/' /etc/default/saslauthd \  
&& touch /etc/saslauthd.conf \  
&& echo "mech_list: plain" >> /usr/lib/sasl2/slapd.conf \  
&& echo "pwcheck_method: saslauthd" >> /usr/lib/sasl2/slapd.conf \  
&& echo "saslauthd_path: /var/run/saslauthd/mux" >> /usr/lib/sasl2/slapd.conf  
  
COPY saslauthd.conf /etc/saslauthd.conf  
  
RUN sed -i 's|ldap:\/\/ad.example.com:389\/|'"$LDAP_SERVERS"'|'
/etc/saslauthd.conf \  
&& sed -i 's/CN=DomainUsers,DC=example,DC=com/'"$LDAP_SEARCH_BASE"'/'
/etc/saslauthd.conf \  
&& sed -i 's/ldap_timeout: 10/ldap_timeout: '"$LDAP_TIMEOUT"'/'
/etc/saslauthd.conf \  
&& sed -i 's/(sAMAccountName=%U)/'"$LDAP_FILTER"'/' /etc/saslauthd.conf \  
&& sed -i 's/CN=Administrator,CN=Users,DC=example,DC=com/'"$LDAP_BIND_DN"'/'
/etc/saslauthd.conf \  
&& sed -i 's/ADpassword/'"$LDAP_PASSWORD"'/' /etc/saslauthd.conf  
  
RUN service saslauthd start  
  
RUN curl -LJO http://mirror.eu.oneandone.net/software/openldap/openldap-
release/openldap-${OPENLDAP_VERSION}.tgz \  
&& gunzip -c openldap-${OPENLDAP_VERSION}.tgz | tar xf - \  
&& rm openldap-${OPENLDAP_VERSION}.tgz  
  
WORKDIR openldap-${OPENLDAP_VERSION}  
  
RUN ./configure --enable-spasswd --with-cyrus-sasl --enable-memberof \  
&& make depend \  
&& make \  
&& make install \  
&& make clean  
  
RUN touch /usr/local/etc/openldap/create.ldif \  
cp /usr/local/var/openldap-data/DB_CONFIG.example /usr/local/var/openldap-
data/DB_CONFIG  
  
COPY slapd.conf /usr/local/etc/openldap/slapd.conf  
RUN sed -i 's/suffix\s\\+"dc=my-domain,dc=com"/suffix \"'"$LDAP_DN_BASE"'\"/'
/usr/local/etc/openldap/slapd.conf \  
&& sed -i 's/cn=Manager,dc=my-domain,dc=com/'"$LDAP_ROOT_DN"'/'
/usr/local/etc/openldap/slapd.conf \  
&& sed -i 's/database\s\\+mdb/database '"$LDAP_DATABASE"'/'
/usr/local/etc/openldap/slapd.conf \  
&& sed -i 's/rootpw\s\\+secret/rootpw '"$LDAP_ROOT_PW"'/'
/usr/local/etc/openldap/slapd.conf  
  
COPY create.ldif /usr/local/etc/openldap/create.ldif  
  
RUN sed -i 's/dn: dc=my-domain,dc=com/dn: '"$LDAP_DN_BASE"'/'
/usr/local/etc/openldap/create.ldif \  
&& sed -i 's/o: Example/o: '"$LDAP_ORGANIZATION"'/'
/usr/local/etc/openldap/create.ldif  
  
RUN slapadd -l /usr/local/etc/openldap/create.ldif  
  
WORKDIR /  
  
EXPOSE 389  
VOLUME ["/usr/local/etc/openldap", "/usr/local/var/openldap-data"]  
  
COPY docker-entrypoint.sh /sbin/docker-entrypoint.sh  
  
RUN chmod 755 /sbin/docker-entrypoint.sh  
  
ENTRYPOINT ["/sbin/docker-entrypoint.sh"]  
  

