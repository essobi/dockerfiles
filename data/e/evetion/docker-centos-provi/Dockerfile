FROM centos/systemd  
MAINTAINER 'Maarten Pronk' <docker@evetion.nl>  
ENV container docker  
RUN yum install sudo -y  
RUN sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
VOLUME [ '/sys/fs/cgroup' ]  
CMD ['/usr/sbin/init']  

