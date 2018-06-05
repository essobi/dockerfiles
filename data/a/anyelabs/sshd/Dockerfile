FROM centos/systemd  
  
MAINTAINER "Anye Labs"  
RUN yum install -y openssh-server openssh-clients passwd net-tools && \  
yum clean all  
  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' && \  
mkdir /var/run/sshd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
sed -ri 's/UsePAM yes/# UsePAM yes/g' /etc/ssh/sshd_config  
RUN systemctl enable sshd.service  
  
ENV ROOTPWD toor-eq-R00T  
RUN echo "root:${ROOTPWD}" | chpasswd  
  
RUN mkdir -p /data/  
VOLUME /data  
  
EXPOSE 22  
CMD ["/usr/sbin/init"]  

