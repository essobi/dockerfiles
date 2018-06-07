FROM centos:centos7  
  
MAINTAINER Mikael Keto  
  
# add nginx repository and gpg key  
ADD nginx.repo /etc/yum.repos.d/nginx.repo  
ADD RPM-GPG-KEY-nginx /etc/pki/rpm-gpg/RPM-GPG-KEY-nginx  
  
# install nginx  
RUN yum -y install nginx && yum clean all && rm -rf /var/cache/yum  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
ENTRYPOINT ["nginx"]  
CMD ["-g", "daemon off;"]  

