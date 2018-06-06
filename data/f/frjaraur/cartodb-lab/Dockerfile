FROM ubuntu:trusty  
  
MAINTAINER FRJARAUR "frjaraur@gmail.com"  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
ENV LDAPDATA /var/lib/ldap  
RUN groupadd -r openldap && useradd -r -g openldap openldap  
  
RUN apt-get update && \  
echo "slapd slapd/root_password password password" |debconf-set-selections &&
\  
echo "slapd slapd/root_password_again password password" |debconf-set-
selections && \  
echo "slapd slapd/internal/adminpw password password" |debconf-set-selections
&& \  
echo "slapd slapd/internal/generated_adminpw password password" |debconf-set-
selections && \  
echo "slapd slapd/password2 password password" |debconf-set-selections && \  
echo "slapd slapd/password1 password password" |debconf-set-selections && \  
echo "slapd slapd/domain string cartodb.com" |debconf-set-selections && \  
echo "slapd shared/organization string cartodb" |debconf-set-selections && \  
echo "slapd slapd/backend string HDB" |debconf-set-selections && \  
echo "slapd slapd/purge_database boolean true" |debconf-set-selections && \  
echo "slapd slapd/move_old_database boolean true" |debconf-set-selections && \  
echo "slapd slapd/allow_ldap_v2 boolean false" |debconf-set-selections && \  
echo "slapd slapd/no_configuration boolean false" |debconf-set-selections && \  
apt-get update && apt-get install -y slapd ldap-utils supervisor && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY ldapfiles/acls.ldif /ldap_utils/acls.ldif  
COPY ldapfiles/objects.ldif /ldap_utils/objects.ldif  
COPY ldapfiles/changeme.sh /ldap_utils/changeme.sh  
COPY ldapfiles/recreateldap.sh /ldap_utils/recreateldap.sh  
COPY ldapfiles/supervisord.conf /etc/supervisor/supervisord.conf  
  
COPY ldapfiles/addldapuser.sh /ldap_utils/addldapuser.sh  
COPY ldapfiles/delldapuser.sh /ldap_utils/delldapuser.sh  
COPY ldapfiles/passwdldapuser.sh /ldap_utils/passwdldapuser.sh  
  
# Set OpenLDAP data and config directories in a data volume  
VOLUME ["$LDAPDATA", "/etc/ldap/slapd.d"]  
  
EXPOSE 389  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD [ "daemon","supervisord","-n", "-c", "/etc/supervisor/supervisord.conf" ]  

