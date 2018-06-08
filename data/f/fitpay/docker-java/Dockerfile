FROM centos:7  
MAINTAINER Scott Stevelinck <scott@fit-pay.com>  
  
RUN yum update -y && yum clean all  
RUN yum install wget -y  
RUN cd /opt; wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u66-b17/jre-8u66-linux-x64.rpm"  
RUN rpm -Uvh /opt/jre-8u66-linux-x64.rpm  
  
ADD local_policy.jar /usr/java/latest/lib/security/local_policy.jar  
ADD US_export_policy.jar /usr/java/latest/lib/security/US_export_policy.jar  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  

