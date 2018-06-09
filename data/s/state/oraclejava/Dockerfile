# Docker base image with Oracle Java  
FROM fedora:20  
MAINTAINER Dan Harvey <dan@state.com>  
  
RUN yum update -y -q; yum clean all  
RUN yum install -y wget; yum clean all  
  
RUN export RPM_URL=http://download.oracle.com/otn-
pub/java/jdk/7u65-b17/jre-7u65-linux-x64.rpm; \  
wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" $RPM_URL; \  
yum localinstall -y $(basename ${RPM_URL}); \  
yum clean all; \  
rm $(basename ${RPM_URL})  

