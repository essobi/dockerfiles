FROM centos:7  
MAINTAINER "Skylar Kelty" <s.kelty@kent.ac.uk>  
ENV container docker  
RUN rm /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/London /etc/localtime  
RUN yum -y -q reinstall glibc-common && yum install -y epel-release vim wget
bzip2 && yum upgrade -y && yum clean all  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
VOLUME [ "/sys/fs/cgroup" ]  
CMD ["/usr/sbin/init"]  

