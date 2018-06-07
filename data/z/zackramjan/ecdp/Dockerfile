FROM centos:latest  
MAINTAINER "zack ramjan" <zack.hr@gREMOVEmail.com>  
ENV container docker  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
RUN yum -y install wget  
RUN yum -y install mariadb-server  
RUN yum -y install mariadb  
RUN yum -y install tomcat  
RUN yum -y install git  
RUN yum -y install unzip  
RUN systemctl enable mariadb  
RUN systemctl enable tomcat  
RUN mkdir /ecdp  
ADD dbdump_tcga.sql.gz /ecdp/dbdump_tcga.sql.gz  
ADD ecdp_setup.sh /ecdp/ecdp_setup.sh  
RUN /bin/sh /ecdp/ecdp_setup.sh  
VOLUME [ "/sys/fs/cgroup" ]  
VOLUME [ "/hostmount" ]  
CMD ["/usr/sbin/init"]  
  
#how i run:  
# docker run -ti -d --privileged --name=ecdp_docker -v /root/ecdp:/hostmount
-v /sys/fs/cgroup:/sys/fs/cgroup:ro -p 3306:3306 -p 8080:8080 ecdp  
#connect to live instance  
#docker exec -it ecdp_docker /bin/bash  

