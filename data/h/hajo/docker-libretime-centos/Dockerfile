#  
# Dockerfile based on my work hajo/docker-libretime  
# ..moved to CentOS7  
FROM centos:7  
  
MAINTAINER Hans-Joachim dd8ne@web.de  
  
ENV container docker  
# force hostname  
ENV HOSTNAME localhost  
  
# Clean up systemd  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \  
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
#  
# Install OS Stuff  
#  
COPY help/* /  
RUN /prep_os.sh  
  
VOLUME [ "/sys/fs/cgroup", "/etc/airtime", "/var/lib/pgsql",
"/srv/airtime/stor", "/srv/airtime/watch" ]  
  
EXPOSE 80  
  
CMD ["/usr/sbin/init"]  

