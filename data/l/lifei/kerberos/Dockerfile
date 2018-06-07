FROM phusion/baseimage  
MAINTAINER Li Fei "lifei.vip@outlook.com"  
RUN sed -i
's/http:\/\/archive\\.ubuntu\\.com\/ubuntu\//http:\/\/mirrors.sohu.com\/ubuntu\//'
/etc/apt/sources.list  
RUN sed -i 's/deb-src/# deb-src/' /etc/apt/sources.list  
RUN apt-get update  
  
RUN apt-get install -y krb5-user krb5-kdc krb5-admin-server krb5-kdc-ldap
supervisor krb5-kdc-ldap && apt-get clean  
  
COPY kerberos-init.sh /usr/local/bin/kerberos-init.sh  
COPY start.sh /etc/my_init.d/00_kerberos_init.sh  
RUN chmod a+x /usr/local/bin/kerberos-init.sh
/etc/my_init.d/00_kerberos_init.sh  
RUN rm /etc/krb5.conf  

