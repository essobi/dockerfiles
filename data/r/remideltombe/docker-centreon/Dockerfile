FROM centos:6  
# add centreon repo  
RUN yum install wget -y  
RUN wget http://yum.centreon.com/standard/3.0/stable/ces-standard.repo -O
/etc/yum.repos.d/ces-standard.repo  
RUN wget http://yum.centreon.com/standard/3.0/stable/RPM-GPG-KEY-CES -O
/etc/pki/rpm-gpg/RPM-GPG-KEY-CES  
  
# disable selinux  
RUN setenforce 0; exit 0  
#RUN su -c "setenforce 0"  
# install centreon  
RUN yum install centreon-base-config-centreon-engine centreon -y  
  
# set php timezone  
RUN echo "date.timezone = Europe/Paris" >> /etc/php.ini  
  
# set httpd runing at startup  
RUN /sbin/chkconfig --add httpd  
RUN /sbin/chkconfig httpd on  
  
# start httpd  
RUN apachectl restart  

