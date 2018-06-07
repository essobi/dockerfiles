FROM centos:centos6.6  
MAINTAINER yoku0825  
WORKDIR /root  
  
RUN yum upgrade -y  
RUN test -d /tmp/setup || mkdir /tmp/setup  
RUN ln -sf /usr/share/zoneinfo/Japan /etc/localtime  
  
RUN yum install -y http://dev.mysql.com/get/mysql57-community-release-
el6-7.noarch.rpm  
RUN yum install -y mysql-utilities  
RUN yum install -y patch  
  
COPY . /tmp/setup  
RUN patch /etc/mysql/fabric.cfg /tmp/setup/fabric.cfg.patch  
  
ENTRYPOINT ["/usr/bin/mysqlfabric"]  

