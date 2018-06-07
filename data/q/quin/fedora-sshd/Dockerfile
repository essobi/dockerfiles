FROM quin/fedora-systemd:latest  
  
ENV SSHUSER fedora  
ENV SSHAUTHORIZEDKEY ""  
  
COPY sshuser_setup /bin  
COPY sshuser_setup.service /etc/systemd/system  
  
RUN dnf -y install openssh-server; dnf clean all; systemctl enable sshd;
systemctl enable sshuser_setup  
  
RUN cat /etc/ssh/sshd_config|sed -e "s/PasswordAuthentication
yes/PasswordAuthentication no/" -e "s/PermitRootLogin yes/PermitRootLogin
no/"> /tmp/sshd_config_new && mv /tmp/sshd_config_new /etc/ssh/sshd_config  
  
EXPOSE 22  

