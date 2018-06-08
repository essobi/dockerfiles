FROM centos:7  
MAINTAINER Aaron Picht <apicht@users.noreply.github.com>  
  
RUN yum update -y && \  
yum install -y
https://download.okta.com/static/agents/ProvisioningAgent/OktaProvisioningAgent-01.02.02.x86_64.rpm
&& \  
yum clean all  
  
RUN mv /opt/OktaProvisioningAgent/conf/settings.conf
/opt/OktaProvisioningAgent/settings-default.conf  
  
ADD start.sh /start.sh  
  
VOLUME ["/opt/OktaProvisioningAgent/conf"]  
  
CMD ["/start.sh"]  

