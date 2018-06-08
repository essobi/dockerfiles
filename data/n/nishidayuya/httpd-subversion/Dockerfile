FROM debian:stretch  
MAINTAINER Yuya.Nishida.  
  
ENV LANG C.UTF-8  
RUN apt-get update && \  
apt-get install -y sudo subversion subversion-tools apache2 libapache2-mod-svn
&& \  
a2enmod dav_svn && \  
touch /etc/apache2/ht{users,groups} && \  
chgrp www-data /etc/apache2/ht{users,groups} && \  
chmod 640 /etc/apache2/ht{users,groups} && \  
mkdir -p /var/lib/svn{,-dumped}  
COPY entrypoint.sh /usr/local/bin/  
COPY dav_svn.conf /etc/apache2/mods-available/  
WORKDIR /var/lib/svn  
  
VOLUME ["/var/lib/svn", "/var/lib/svn-dumped"]  
  
EXPOSE 80  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["apachectl", "-DFOREGROUND"]  

