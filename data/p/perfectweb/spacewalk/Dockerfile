FROM centos:7.2.1511  
MAINTAINER Alin Jurj <office@perfectweb.ro>  
  
USER root  
WORKDIR /root  
  
# ports  
EXPOSE 80 443 5222 68 69  
ADD conf/answers.txt /root/answers.txt  
ADD conf/jpackage50.repo /etc/yum.repos.d/jpackage50.repo  
  
# add repositories  
RUN rpm -Uvh http://yum.spacewalkproject.org/2.4/RHEL/7/x86_64/spacewalk-
repo-2.4-3.el7.noarch.rpm  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
  
# install  
RUN yum install -y spacewalk-setup-postgresql yum-versionlock supervisor  
RUN yum versionlock cglib-2.1.3-4.jpp5  
RUN yum update -y  
RUN yum install -y spacewalk-postgresql  
  
# supervisor  
ADD conf/supervisord.conf /etc/supervisord.d/supervisord.conf  
  
USER postgres  
RUN /usr/bin/pg_ctl initdb -D /var/lib/pgsql/data/  
RUN /usr/bin/pg_ctl start -D /var/lib/pgsql/data/ -w -t 300  
  
USER root  
RUN spacewalk-setup --disconnected --answer-file=/root/answers.txt --skip-db-
diskspace-check --run-cobbler  
  
# clean  
RUN yum clean all ; rm -rf /tmp/*  
  
ENTRYPOINT supervisord -c /etc/supervisord.d/supervisord.conf && tail -f
/var/log/**/*.log  

