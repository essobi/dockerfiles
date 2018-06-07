FROM centos:latest  
  
MAINTAINER ja  
  
RUN yum clean all && \  
sed -i 's/gpgcheck=1/gpgcheck=0/g' /etc/yum.conf && \  
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
yum update -q -y && \  
yum install -q -y httpd && \  
yum clean all  
  
COPY index.html /var/www/html/  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/httpd"]  
  
CMD ["-D","FOREGROUND"]

