FROM debian:jessie  
  
#phusion/baseimage:latest  
ENV LDAP_DOMAIN=example.com  
ENV LDAP_PASSWORD=PassworD1  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update -qq && apt-get install -y slapd ldap-utils -qq  
RUN rm -rf /etc/ldap/slapd.d && rm -rf /var/lib/ldap/* && mkdir
/etc/ldap/slapd.d  
  
ADD ./run.sh /  
ADD ./install.sh /  
ADD ./ldif /etc/ldap/init  
  
RUN chmod +x /run.sh /install.sh  
  
EXPOSE 389 636  
VOLUME /etc/ldap/slapd.d /var/lib/ldap  
  
ENTRYPOINT ["/run.sh", "-h ldapi:/// ldap:/// ldaps:///"]  
  
CMD []  
  

