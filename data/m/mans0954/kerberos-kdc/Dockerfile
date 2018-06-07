FROM debian  
MAINTAINER christopher.hoskin@gmail.com  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y apt-utils  
RUN apt-get install -y krb5-kdc  
  
RUN mkdir /var/log/kerberos  
  
RUN mkdir /etc/kdc  
RUN mv /etc/krb5.conf /etc/kdc/krb5.conf  
RUN ln -s /etc/kdc/krb5.conf /etc/krb5.conf  
  
EXPOSE 88  
CMD /usr/sbin/krb5kdc -n  

