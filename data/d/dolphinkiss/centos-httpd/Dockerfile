FROM centos:7.3.1611  
RUN yum install -y httpd mod_ssl mod_proxy mod_proxy_http strace less htop
lsof tree unzip expect \  
&& yum clean all  
  
CMD ["httpd", "-DFOREGROUND", "-e", "info"]  

