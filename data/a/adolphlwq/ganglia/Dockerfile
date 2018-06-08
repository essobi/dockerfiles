FROM centos:6  
MAINTAINER wlu wlu@linkernetworks.com  
  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-6.noarch.rpm  
  
RUN yum install -y php-common php-cli php-gb php  
  
# install ganglia server and client  
RUN yum install -y rrdtool rrdtool-devel ganglia-web ganglia-gmetad \  
ganglia-gmond ganglia-gmond-python httpd apr-devel zlib-devel \  
libconfuse-devel expat-devel pcre-devel  
  
RUN mkdir -p /var/lib/ganglia && \  
chown nobody:nobody /var/lib/ganglia && \  
chmod 777 /var/lib/ganglia  
  
ADD supervisord.conf /etc/supervisord.conf  
RUN yum install -y python-setuptools && \  
easy_install supervisor && \  
yum clean all  
  
RUN yum install -y vim && \  
ln -f -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
ADD ganglia.conf /etc/httpd/conf.d/ganglia.conf  
  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  

