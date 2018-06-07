FROM debian:jessie  
  
MAINTAINER Daniel Binkhuysen <daniel@binkhuysen.com>  
  
ENV OPENLDAP_VERSION 2.4.40  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
slapd=${OPENLDAP_VERSION}* && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN mv /etc/ldap /etc/ldap.dist  
  
COPY modules/ /etc/ldap.dist/modules  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 0755 /sbin/entrypoint.sh  
  
VOLUME ["/etc/ldap", "/var/lib/ldap"]  
EXPOSE 389  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["slapd", "-d", "32768", "-u", "openldap", "-g", "openldap"]  

