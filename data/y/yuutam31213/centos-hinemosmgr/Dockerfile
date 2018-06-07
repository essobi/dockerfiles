#  
# Base DockerFile  
#  
FROM centos:latest  
  
LABEL maintainer="Yuuta Maeda"  
  
# system update  
RUN yum -y update && yum clean all  
  
# set locale  
RUN rm -f /etc/rpm/macros.image-language-conf && \  
sed -i '/^override_install_langs=/d' /etc/yum.conf && \  
yum -y reinstall glibc-common && \  
yum clean all  
  
ENV LANG="ja_JP.UTF-8" \  
LANGUAGE="ja_JP:ja" \  
LC_ALL="ja_JP.UTF-8"  
# update yum  
RUN yum update -y && yum clean all  
  
# epel repo  
RUN yum install -y epel-release && yum clean all  
  
# yum install  
RUN yum install -y wget  
  
#------------------------------------------------  
# Java  
RUN yum install -y java-1.8.0-openjdk && yum install -y java-1.8.0-openjdk-
devel  
  
#------------------------------------------------  
# Hinemos  
RUN yum install -y rsyslog  
RUN yum install -y vim-common  
RUN yum install -y net-snmp  
RUN yum install -y net-snmp-utils  
RUN yum install -y net-tools  
RUN yum install -y sysstat  
RUN yum install -y tcpdump  
RUN yum install -y lsof  
RUN yum install -y sblim-wbemcli  
RUN yum install -y unzip  
RUN yum install -y vlgothic-p-fonts  
  
#------------------------------------------------  
# Hinemos Mgr&Web  
#RUN rpm -ivh
https://github.com/hinemos/hinemos/releases/download/v6.1.0/hinemos-6.1-manager-6.1.0-1.el7.x86_64.rpm  
#RUN service hinemos_manager start  
#RUN rpm -ivh
https://github.com/hinemos/hinemos/releases/download/v6.1.0/hinemos-6.1-web-6.1.0-1.el7.x86_64.rpm  
#RUN service hinemos_web start  
RUN locale  
  
CMD ["/sbin/init"]  

