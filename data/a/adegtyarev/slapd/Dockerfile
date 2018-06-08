FROM ubuntu:xenial  
MAINTAINER Alexey Degtyarev <alexey@renatasystems.org>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt update -q && \  
apt install locales && \  
locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales  
  
RUN apt install -y \  
ca-certificates \  
ldap-utils \  
ldapscripts \  
ldapvi \  
slapd \  
vim-nox  
  
RUN apt clean && \  
rm -fr /var/lib/apt/lists/*  
  
ENV LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
TERM=xterm  
  
COPY init-db.sh /  
  
EXPOSE 389 636  
VOLUME ["/etc/ldap/slapd.d", "/var/lib/ldap"]  
  
ENTRYPOINT ["slapd"]  
  
CMD ["-h", "ldap:/// ldapi:/// ldaps:///", "-u", "openldap", "-g", "openldap",
"-dStats,Stats2"]  

