FROM centos:7.0.1406  
MAINTAINER "slemesle" <seven.lemesle@wescale.fr>  
ENV container docker  
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*; \  
yum install -y curl sysvinit-tools \  
initscripts sudo crontabs cronie cronie-anacron  
RUN curl -L https://bootstrap.saltstack.com -o install_salt.sh  
RUN sh install_salt.sh -F -Z -P -X stable  
RUN mkdir -p /etc/salt/minion.d  
RUN mkdir -p /app/cd-factory; touch /etc/sysctl.conf  
RUN systemctl enable salt-minion.service;  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
CMD ["/usr/sbin/init"]  

