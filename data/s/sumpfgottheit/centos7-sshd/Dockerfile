FROM sumpfgottheit/centos7  
MAINTAINER Florian Sachs "florian.sachs@gmx.at"  
# Free the wheel group  
RUN echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# Add my User  
RUN useradd -G wheel -u 1808 -m saf  
  
RUN yum -y install vim ack  
RUN yum -y clean all  
ADD create-server-ssh-keys.sh /docker-entrypoint.d/create-server-ssh-keys.sh  
ADD write-docker-env-to-profile.sh /docker-entrypoint.d/write-docker-env-to-
profile.sh  
ADD add_root_authorized_keys.sh /docker-
entrypoint.d/add_root_authorized_keys.sh  
ADD supervisor.sshd.ini /etc/supervisord.d/sshd.ini  
RUN mkdir -m 0700 /root/.ssh  
VOLUME ["/ssh_host_keys"]  
CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf" ]  
  

