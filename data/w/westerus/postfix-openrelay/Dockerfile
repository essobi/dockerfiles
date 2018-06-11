#Dockerfile for a Postfix email open relay service  
FROM centos:6.6  
MAINTAINER John Wehr johnwehr@gmail.com  
  
RUN yum update -y  
RUN yum install -y rsyslog epel-release cyrus-sasl cyrus-sasl-plain cyrus-
sasl-md5 mailx perl supervisor postfix  
RUN sed -i -e 's/inet_interfaces = localhost/inet_interfaces = all/g'
/etc/postfix/main.cf  
RUN sed -i -e 's/#mynetworks = 168.100.189.0\/28, 127.0.0.0\/8/mynetworks =
0.0.0.0\/0/g' /etc/postfix/main.cf  
COPY /rootfs/entry-point.sh /  
RUN chmod +x /entry-point.sh  
RUN newaliases  
  
EXPOSE 25  
CMD ["/entry-point.sh"]  

