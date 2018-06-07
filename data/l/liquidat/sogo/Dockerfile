FROM centos:centos7  
  
# Install EPEL repository and dependencies  
RUN rpm --import https://getfedora.org/static/352C64E5.txt && rpm -Uvh
https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm  
RUN yum -y update && yum -y install gcc-objc gnustep-base rpm-build gnustep-
make libwbxml-devel lasso-devel libmemcached-devel postgresql-devel mariadb-
devel make vim gnustep-base-devel openldap-devel curl-devel wget httpd
memcached && yum clean all  
  
# add proper user  
RUN useradd sogo  
  
# download SOPE and SOGO  
RUN wget https://sogo.nu/files/downloads/SOGo/Sources/SOPE-3.2.10.tar.gz &&
tar -xf SOPE*gz && rm -f SOPE*gz && cd SOPE* && ./configure --with-gnustep &&
make && make install && cd .. && rm -rf SOPE*  
RUN wget https://sogo.nu/files/downloads/SOGo/Sources/SOGo-3.2.10.tar.gz &&
tar -xf SOGo*gz && rm -f SOGo*gz && cd SOGo* && ./configure --enable-saml2 &&
make && make install && cp Apache/SOGo.conf /etc/httpd/conf.d/SOGo.conf && cp
Scripts/sogo-default /etc/sysconfig/sogo && cd .. && rm -rf SOGo*  
  
# add ld config  
ADD sogo-ld.conf /etc/ld.so.conf.d/sogo-ld.conf  
  
# add sogo configuration  
ADD sysconfig-sogo /etc/sysconfig/sogo  
  
# add docker entrypoint  
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["/bin/sh","-c","/usr/local/bin/docker-entrypoint.sh"]  
  
EXPOSE 80 443 20000  

