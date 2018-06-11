FROM centos:7.3.1611  
RUN yum install -y epel-release \  
&& yum update -y \  
&& yum install -y certbot openssh-clients  
  
VOLUME ["/etc/letsencrypt"]  
WORKDIR /etc/nginx  
  
ENTRYPOINT ["certbot"]  

