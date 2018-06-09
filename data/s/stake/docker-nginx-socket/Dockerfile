FROM centos:centos6  
  
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
RUN localedef -f UTF-8 -i ja_JP ja_JP  
  
# Update base images.  
RUN yum distribution-synchronization -y  
  
# Setup nginx  
RUN rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-
centos-6-0.el6.ngx.noarch.rpm  
RUN yum install -y nginx  
  
# Setup supervisord  
RUN yum install -y python-setuptools  
RUN easy_install supervisor  
  
# Cleaining up.  
RUN yum clean all  
  
# configuration nginx + go  
ADD ./nginx/nginx.conf /etc/nginx/nginx.conf  
RUN rm /etc/nginx/conf.d/*  
ADD ./nginx/goapp.conf /etc/nginx/conf.d/goapp.conf  
ADD ./gotest /usr/local/sbin/gotest  
RUN chmod 644 /etc/nginx/nginx.conf /etc/nginx/conf.d/goapp.conf  
RUN chmod 755 /usr/local/sbin/gotest  
  
# configuration supervisord  
ADD ./supervisord/supervisord.conf /etc/supervisord.conf  
ADD ./run.sh /run.sh  
RUN chmod 755 /run.sh  
  
# Define moutable directory  
VOLUME ["/var/log/nginx"]  
  
# Expose the Ports used by  
EXPOSE 80  
CMD ["/bin/bash", "/run.sh"]

