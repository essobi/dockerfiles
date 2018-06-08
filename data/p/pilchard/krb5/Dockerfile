# Author: pilchard  
FROM centos  
MAINTAINER pilchard <ludundun@126.com>  
  
LABEL Description="centos Dev"  
ENV KRB5_CONFIG=/etc/kerberos/conf/krb5.conf  
  
RUN \  
yum install -y krb5-server krb5-workstation && \  
yum autoremove -y  
ADD kadm5.acl kdc.conf principal principal.kadm5 principal.kadm5.lock
principal.ok .k5.YI.COM /var/kerberos/krb5kdc/  
  
CMD "bash"

