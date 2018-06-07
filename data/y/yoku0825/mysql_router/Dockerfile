FROM centos:centos7  
MAINTAINER yoku0825  
WORKDIR /root  
  
RUN yum upgrade -y  
RUN test -d /tmp/setup || mkdir /tmp/setup  
RUN ln -sf /usr/share/zoneinfo/Japan /etc/localtime  
  
RUN yum install -y http://dev.mysql.com/get/mysql57-community-release-
el7-7.noarch.rpm  
RUN yum install -y mysql-router  
  
COPY . /tmp/setup  
  
ENTRYPOINT ["/usr/sbin/mysqlrouter", "--extra-config=/tmp/setup/router.ini"]  

