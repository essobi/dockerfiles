FROM centos:centos5  
#MAINTAINER Ushio Shugo <ushio.s@gmail.com>  
# using epel  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-
release-5-4.noarch.rpm  
Run yum -y update  
  
RUN yum -y install postfix cyrus-sasl cyrus-sasl-plain mailx  
  
ADD ./root/etc/postfix/main.cf /etc/postfix/main.cf  
ADD ./root/etc/postfix/header_checks /etc/postfix/header_checks  
  
RUN postconf -e 'relayhost = [smtp.mailgun.org]:587'  
RUN postconf -e 'smtp_sasl_auth_enable = yes'  
  
EXPOSE 25  
CMD ["sh", "-c", "postconf -e \"smtp_sasl_password_maps =
static:$POSTFIX_USER:$POSTFIX_PWD\"; postconf -e \"myhostname =
$POSTFIX_HOSTNAME\"; service postfix start; tail -F /var/log/mail.log"]  

