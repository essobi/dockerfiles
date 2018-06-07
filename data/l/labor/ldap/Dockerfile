FROM ubuntu:trusty  
  
MAINTAINER seu <seu@panopticon.re>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list && \  
apt-get update -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y slapd ldap-utils && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mv /etc/ldap /etc/ldap.dist && \  
mkdir /etc/ldap && \  
mkdir /etc/ldap/schema  
  
EXPOSE 389  
COPY labor.schema /etc/ldap/schema/  
COPY core.schema /etc/ldap/schema/  
  
COPY bootstrap.ldif /etc/ldap/  
  
COPY slapd.conf /etc/ldap/  
  
RUN slapadd -c -n1 -l /etc/ldap/bootstrap.ldif -f /etc/ldap/slapd.conf  
RUN chown -R openldap:openldap /var/lib/ldap /etc/ldap  
  
CMD ["slapd", \  
"-d", "acl,config,filter,stats,conns", \  
"-u", "openldap", \  
"-g", "openldap", \  
"-f", "/etc/ldap/slapd.conf"]  

