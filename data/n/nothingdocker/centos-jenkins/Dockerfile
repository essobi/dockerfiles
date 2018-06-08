# Version 1.0.1  
FROM nothingdocker/centos-node  
RUN yum install -y gcc gcc-c++ make cmake git;  
RUN yum install -y https://pkg.jenkins.io/redhat-
stable/jenkins-2.7.4-1.1.noarch.rpm;  
RUN yum install -y java-1.8.0-openjdk  
RUN yum install -y initscripts;  
RUN yum clean all;  
  
RUN mkdir -p /data  
  
COPY ./jenkins /etc/sysconfig/  
COPY entrypoint.sh /entrypoint.sh  
  
EXPOSE 8080  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/init"]  
  

