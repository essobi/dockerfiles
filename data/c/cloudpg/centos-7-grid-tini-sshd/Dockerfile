FROM cloudpg/centos-7-grid-tini  
  
RUN yum --setopt=tsflags=nodocs -y update \  
&& yum --setopt=tsflags=nodocs -y install openssh-server sudo \  
&& yum clean all \  
&& mkdir /var/run/sshd \  
# Setup ssh keys  
&& ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa \  
&& ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa \  
&& ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa \  
&& ssh-keygen -f /etc/ssh/ssh_host_ed25519_key -N '' -t ed25519 \  
&& sed -i -e 's/#ClientAliveInterval\ 0/ClientAliveInterval\ 600/g'
/etc/ssh/sshd_config \  
# Create admin user  
&& adduser admin \  
&& echo 'admin:passwd' | chpasswd \  
&& usermod -aG wheel admin  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]

