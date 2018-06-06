FROM centos:6.4  
MAINTAINER Takatsugu Shigeta, shigeta@cpan.org  
RUN yum -y update  
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum install -y gearmand  
ENTRYPOINT ["gearmand"]  
EXPOSE 4730

