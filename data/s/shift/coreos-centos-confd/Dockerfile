# Dockerfile for adding confd to a base image  
FROM shift/coreos-centos-etcd:latest  
  
MAINTAINER Vincent Palmer <shift-gh@someone.section.me>  
  
RUN curl -L https://api.github.com/repos/kelseyhightower/confd/releases | grep
-v alpha | grep -v beta | sed -n 's|.*\"tag_name\": \"v\\(.*\\)\".*|\1|p' |
head -n 1 > /tmp/confd_version  
RUN curl -L https://github.com/kelseyhightower/confd/releases/download/v`cat
/tmp/confd_version`/confd-`cat /tmp/confd_version`-linux-amd64 -o
/usr/local/bin/confd  
RUN chmod 0755 /usr/local/bin/confd  
RUN mkdir -p /etc/confd/conf.d /etc/confd/templates  

