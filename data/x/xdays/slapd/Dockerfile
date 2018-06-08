FROM ubuntu:14.04  
MAINTAINER xdays <easedays@gmail.com>  
  
ENV PASSOWRD=changeme  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && apt-get install -y slapd ldap-utils && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 636  
VOLUME /var/lib/ldap  
  
CMD ["slapd", "-h", "ldaps:/// ldapi:///", "-u", "openldap", "-g", "openldap",
"-d", "0"]  

