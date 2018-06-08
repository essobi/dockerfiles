FROM centos:7  
MAINTAINER Aaron Picht <apicht@users.noreply.github.com>  
  
RUN yum update -y && \  
yum install -y https://download.okta.com/static/ldap-
agent/OktaLDAPAgent-05.04.02.x86_64.rpm && \  
yum clean all  
  
RUN mv /opt/Okta/OktaLDAPAgent/conf/logback.xml
/opt/Okta/OktaLDAPAgent/logback-default.xml  
  
ADD start.sh /start.sh  
  
VOLUME ["/opt/Okta/OktaLDAPAgent/conf"]  
  
CMD ["/start.sh"]  

