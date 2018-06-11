############################################################  
# Dockerfile to build Apache container images  
# Based on CentOS  
############################################################  
  
FROM centos:latest  
  
MAINTAINER Muhammad Zeeshan Munir <MZMunirr@gmail.com>  
  
RUN mkdir -p ~/test  
  
#ADD https://github.com/ZeeshanMunir/Docker/blob/master/simple.sh /tmp  
ADD https://github.com/ZeeshanMunir/Docker/blob/master/simple.sh ~/test/  
  
#RUN rpm -ivh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
#RUN firewall-cmd --add-service=http; firewall-cmd --permanent --add-
service=http  
RUN yum -y install httpd; yum clean all #systemctl enable httpd.service
#httpd-devel  
  
EXPOSE 80  
  
CMD ["--port 80"]  
  
ENTRYPOINT ["/usr/sbin/httpd"]  
CMD ["-D", "FOREGROUND"]  

