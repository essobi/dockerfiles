FROM phusion/baseimage:0.9.18  
MAINTAINER Yifan Gao "git@gaoyifan.com"  
ENV SUDO_FORCE_REMOVE yes  
  
RUN rm -f /etc/service/sshd/down  
  
RUN apt-get update && apt-get install -qqy nslcd sudo-ldap ca-certificates
docker.io  
  
ADD nslcd.conf /etc/nslcd.conf  
  
ADD ldap.conf /etc/ldap/ldap.conf  
  
ADD nsswitch.conf /etc/nsswitch.conf  
  
ADD ca-certificates.crt /etc/ssl/certs/ca-certificates.crt  
  
ADD sshd_config /etc/ssh/sshd_config  
  
ADD common-session /etc/pam.d/common-session  
  
ADD rc.local /etc/rc.local  
  
CMD /sbin/my_init  

