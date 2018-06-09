FROM centos:7  
MAINTAINER "Florian Sachs" <florian.sachs@gmx.at>  
  
ENV container docker  
  
# Install epel  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
  
# Install runit  
RUN curl -s
https://packagecloud.io/install/repositories/imeyer/runit/script.rpm.sh | bash
&& yum -y install runit-2.1.1-7.el7.centos.x86_64  
  
# Reinstall glibc, so that locales work  
RUN yum -y reinstall glibc-common  
  
# Install scl  
RUN yum -y install centos-release-scl.noarch  
  
# Install rh-python34  
RUN yum -y install rh-python34  
  
# Install essentials  
RUN yum -y install wget tar net-tools telnet openssh-server openssh-clients
sudo git cron  
  
# Add my_init and setuser from the phusion-docker-baseimge  
ADD build /build  
RUN bash /build/build.sh  
RUN rm -fr /build  
  
RUN yum -y clean all && rm -fr /tmp/* /var/tmp/* /root/.cache /run/*  
  
CMD ["/sbin/my_init"]  

