FROM debian:jessie  
MAINTAINER avinash.s@yukthi.com  
  
RUN apt-get update  
RUN apt-get -y dist-upgrade  
RUN echo "slapd slapd/no_configuration boolean true" | debconf-set-selections  
RUN apt-get -y install slapd ldap-utils slapd-smbk5pwd  
RUN apt-get -y install ldap-utils  
  
RUN mkdir /var/run/slapd  
RUN chown openldap:openldap /var/run/slapd  
  
RUN apt-get clean  
  
COPY /run-slapd /  
CMD ["/run-slapd"]  

