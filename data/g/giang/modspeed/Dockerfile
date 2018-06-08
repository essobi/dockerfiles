FROM centos:7  
ADD https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-
stable_current_x86_64.rpm /tmp  
  
RUN yum -y install at httpd  
RUN rpm -U /tmp/mod-pagespeed-*.rpm

