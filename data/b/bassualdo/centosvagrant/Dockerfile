FROM centos  
  
RUN yum -y install epel-release && yum -y update && yum clean all  
RUN yum -y install openssh-server \  
openssh-clients \  
passwd \  
sudo\  
wget \  
supervisor;\  
yum clean all  
  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''  
  
# Create and configure vagrant user  
RUN useradd --create-home -s /bin/bash vagrant  
RUN echo -n 'vagrant:vagrant' | chpasswd  
WORKDIR /home/vagrant  
  
# Configure SSH access  
ADD
https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub \  
/home/vagrant/.ssh/authorized_keys  
RUN chown -R vagrant:vagrant /home/vagrant/.ssh  
RUN chmod 0600 /home/vagrant/.ssh/authorized_keys  
RUN chmod 0700 /home/vagrant/.ssh  
  
# Enable passwordless sudo for the "vagrant" user  
RUN mkdir -p /etc/sudoers.d  
RUN install -b -m 0440 /dev/null /etc/sudoers.d/vagrant  
RUN echo 'vagrant ALL=NOPASSWD: ALL' >> /etc/sudoers.d/vagrant  
  
RUN mkdir /var/run/sshd  
  
RUN echo "[unix_http_server]" > /etc/supervisord.conf && \  
echo "file=/tmp/supervisor.sock" >> /etc/supervisord.conf && \  
echo "" >> /etc/supervisord.conf && \  
echo "[supervisord]" >> /etc/supervisord.conf && \  
echo "nodaemon=true" >> /etc/supervisord.conf && \  
echo "" >> /etc/supervisord.conf && \  
echo "[rpcinterface:supervisor]" >> /etc/supervisord.conf && \  
echo "supervisor.rpcinterface_factory =
supervisor.rpcinterface:make_main_rpcinterface" >> /etc/supervisord.conf && \  
echo "" >> /etc/supervisord.conf && \  
echo "[supervisorctl]" >> /etc/supervisord.conf && \  
echo "serverurl=unix:///tmp/supervisor.sock" >> /etc/supervisord.conf && \  
echo "" >> /etc/supervisord.conf && \  
echo "[program:sshd]" >> /etc/supervisord.conf && \  
echo "command=/usr/sbin/sshd -D -e" >> /etc/supervisord.conf  
  
#CMD ["/usr/sbin/sshd", "-D","-e"]  
CMD ["/usr/bin/supervisord"]  
EXPOSE 22  

