FROM openshift/jenkins-slave-maven-centos7:latest  
MAINTAINER Ladislav Thon <lthon@redhat.com>  
  
USER root  
  
RUN yum -y install epel-release && \  
yum -y install jq && \  
yum clean all -y  
  
COPY startup /usr/local/bin/  
  
USER 1001  
  
ENTRYPOINT ["/usr/local/bin/startup"]  

