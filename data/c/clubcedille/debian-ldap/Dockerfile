FROM clubcedille/debian-supervisord  
MAINTAINER Michael Faille <michael@faille.io>  
  
# Default configuration: can be overridden at the docker command line  
ENV LDAP_SERVER configure-me  
ENV SLDAP_ROOTPASS toor  
ENV SLDAP_ORGANISATION Acme Widgets Inc.  
ENV SLDAP_DOMAIN example.com  
  
ENV FUSIONDIRECTORY_DEB_PKG_VERSION *  
  
RUN echo "# fusiondirectory repository \n\  
deb http://repos.fusiondirectory.org/debian-wheezy wheezy main \n\  
\n\  
# fusiondirectory debian-extra repository \n\  
deb http://repos.fusiondirectory.org/debian-extra wheezy main" >
/etc/apt/sources.list.d/fusion.list && \  
gpg --keyserver keys.gnupg.net --recv-key 62B4981F && \  
gpg --export -a "Fusiondirectory Archive Manager
<contact@fusiondirectory.org>" | apt-key add -  
  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y slapd ldap-utils \  
fusiondirectory-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-systems-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-mail-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-audit-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-alias-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-ssh-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-sudo-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-fusioninventory-
schema=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-dns-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-dsa-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-ppolicy-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-personal-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}  
RUN schema2ldif /etc/ldap/schema/fusiondirectory/rfc2307bis.schema >
/etc/ldap/schema/fusiondirectory/rfc2307bis.ldif && \  
sed -i "s|include: file:///etc/ldap/schema/nis.ldif|include:
file:///etc/ldap/schema/fusiondirectory/rfc2307bis.ldif|g"
/usr/share/slapd/slapd.init.ldif  
  
# Add configurations  
ADD slapd /opt/slapd  
  
ADD supervisor-slapd.conf /etc/supervisor/conf.d/slapd.conf  
  
# To prevent this error : "TERM environment variable not set."  
ENV TERM xterm  
  
EXPOSE 389  

