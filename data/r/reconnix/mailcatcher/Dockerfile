### Dockerfile  
FROM reconnix/base:latest  
MAINTAINER Russ McKendrick <russ.mckendrick@reconnix.com>  
  
RUN yum group install -y "Development Tools" && yum install -y rubygems
libsqlite3-dev ruby-devel openssl openssl-devel sqlite sqlite-devel  
RUN gem install mailcatcher --no-ri --no-rdoc  
CMD mailcatcher --smtp-port 25 --http-port 80 --ip `ip addr show dev eth0
scope global | grep inet | awk '{print $2;}' | cut -d/ -f1` -f

