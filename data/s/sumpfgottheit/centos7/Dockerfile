FROM centos:7  
MAINTAINER Florian Sachs "florian.sachs@gmx.at"  
ADD set_bash_environment.sh /etc/profile.d/  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7  
RUN yum -y install wget tar net-tools telnet openssh-server openssh-clients
supervisor sudo  
RUN yum -y update  
RUN yum -y clean all  
RUN rm -fr /var/log/*  
RUN mkdir /var/log/supervisor  
  
RUN rm -f /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Vienna /etc/localtime  
  
RUN sed -r -i
's#logfile=/var/log/supervisor/supervisord.log#logfile=/var/log/supervisord.log#'
/etc/supervisord.conf  
  
RUN mkdir /docker-entrypoint.d /logs /docker-entrypoint-ext.d  
ADD docker-entrypoint.sh /  
RUN chmod 0755 /docker-entrypoint.sh  
ADD copy-logstash.conf.sh /docker-entrypoint.d/copy-logstash.conf.sh  
  
VOLUME ["/docker-entrypoint-ext.d", "/logs"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

