FROM centos:centos6  
  
##########################################################################  
### change timezone  
RUN (ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
sed -i -e 's#Europe/London#Asia/Tokyo#' /etc/sysconfig/clock)  
  
##########################################################################  
RUN yum install -y sudo passwd openssh-server openssh-clients tar screen \  
crontabs strace telnet perl libpcap git  
  
# start sshd to generate host keys  
RUN (service sshd start && \  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \  
sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config && \  
sed -i 's/enabled=0/enabled=1/' /etc/yum.repos.d/CentOS-Base.repo)  
  
  
# Create User  
RUN (useradd worker && \  
echo "worker:cqctest" | chpasswd && \  
echo "root:cqctest" | chpasswd && \  
su worker -c "mkdir -p /home/worker/.ssh" && \  
su worker -c "chmod 700 /home/worker/.ssh" && \  
su worker -c "mkdir -p /home/worker/tmp")  
  
RUN echo "worker ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/worker  
  
# script to start services  
ADD startservice.sh /home/worker/startservice.sh  
RUN chmod 755 /home/worker/startservice.sh  
  
EXPOSE 22  
CMD ["/home/worker/startservice.sh"]  

