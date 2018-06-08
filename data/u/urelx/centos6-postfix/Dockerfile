FROM centos:centos6  
MAINTAINER Yuu Yamanaka <yuu@relx.jp>  
  
RUN yum update -y && yum install -y rsyslog postfix  
  
ADD start.sh /start.sh  
RUN sed -i -e 's/^inet_interfaces = localhost/inet_interfaces = all/'
/etc/postfix/main.cf  
ONBUILD ADD postfix/ /etc/postfix/  
  
EXPOSE 25  
VOLUME ["/var/log","/var/spool/postfix"]  
  
CMD ["/start.sh"]  

