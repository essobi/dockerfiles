FROM debian:jessie  
  
MAINTAINER Christian Luginbühl <dinke@pimprecords.com>  
  
ENV OPENLDAP_VERSION 2.4.40  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
slapd=${OPENLDAP_VERSION}*  
  
RUN mv /etc/ldap /etc/ldap.dist  
  
RUN apt-get install -y ldap-account-manager  
RUN service apache2 start  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 389  
EXPOSE 80  
VOLUME ["/etc/ldap", "/var/lib/ldap"]  
  
COPY modules/ /etc/ldap.dist/modules  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["slapd", "-d", "32768", "-u", "openldap", "-g", "openldap"]  

