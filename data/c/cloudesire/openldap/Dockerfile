FROM ubuntu:14.04  
MAINTAINER Cloudesire TEAM <dev@cloudesire.com>  
  
ENV HOME /root  
  
# Configure apt  
RUN apt-get -y update  
  
# Install slapd  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y slapd  
  
EXPOSE 389  
EXPOSE 636  
VOLUME /var/lib/ldap  
VOLUME /etc/ssl  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT /usr/sbin/slapd -h 'ldap:/// ldapi:/// ldaps:///' -F
/etc/ldap/slapd.d -d256  
# vim:ts=8:noet:  

