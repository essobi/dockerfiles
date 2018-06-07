FROM ubuntu:16.10  
  
MAINTAINER David Weisgerber <david@fourconnected.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
VOLUME ["/data"]  
  
# Setup ssh and install supervisord  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install samba and dependencies to make it an Active Directory Domain
Controller  
RUN apt-get install -y build-essential libacl1-dev libattr1-dev \  
libblkid-dev libreadline-dev python-dev libpam0g-dev \  
python-dnspython gdb pkg-config libpopt-dev libldap2-dev \  
dnsutils libbsd-dev attr krb5-user docbook-xsl libcups2-dev acl python-xattr  
RUN apt-get install -y samba smbclient krb5-kdc winbind libnss-winbind  
  
ADD init.sh /init.sh  
RUN chmod 755 /init.sh  
  
EXPOSE 22 53 389 88 135 139 138 445 464 3268 3269  
CMD ["/init.sh"]  

