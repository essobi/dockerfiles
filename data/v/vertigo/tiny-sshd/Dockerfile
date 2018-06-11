FROM centos:latest  
  
LABEL maintainer andre@vertigo.com.br  
  
RUN yum install openssh-server openssh-clients passwd sudo -y && \  
yum clean all  
  
ADD src/*.sh /opt/  
  
RUN useradd -u 5001 -G wheel -m user && \  
chmod +x /opt/*.sh && \  
echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
sed -i s/^#PasswordAuthentication.*/PasswordAuthentication\ yes/
/etc/ssh/sshd_config && \  
/opt/generatekeys.sh  
  
#RUN sed -i s/^#UsePAM.*/UsePAM\ yes/ /etc/ssh/sshd_config  
EXPOSE 22  
CMD ["/opt/startsshd.sh"]  
  

