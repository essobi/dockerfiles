FROM ubuntu:14.04  
  
RUN apt-get update&&\  
apt-get upgrade -y &&\  
apt-get install -y openssh-server &&\  
apt-get clean&&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /var/run/sshd && \  
sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin no/' /etc/ssh/sshd_config &&
\  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \  
sed -ri 's/Subsystem sftp \/usr\/lib\/openssh\/sftp-server/Subsystem sftp
\/usr\/lib\/openssh\/sftp-server -u 0/g' /etc/ssh/sshd_config && \  
echo "Match User www-data" >> /etc/ssh/sshd_config && \  
echo " ChrootDirectory /var/www" >> /etc/ssh/sshd_config && \  
echo " AllowTCPForwarding no" >> /etc/ssh/sshd_config && \  
echo " PermitTunnel no" >> /etc/ssh/sshd_config && \  
echo " X11Forwarding no" >> /etc/ssh/sshd_config && \  
echo " ForceCommand internal-sftp" >> /etc/ssh/sshd_config && \  
echo "Match User mysql" >> /etc/ssh/sshd_config && \  
echo " AllowTCPForwarding yes" >> /etc/ssh/sshd_config && \  
echo " PermitTunnel no" >> /etc/ssh/sshd_config && \  
echo " X11Forwarding no" >> /etc/ssh/sshd_config  
  
COPY start /usr/sbin/start  
COPY tunnelshell /bin/tunnelshell  
RUN chmod +x /usr/sbin/start /bin/tunnelshell  
EXPOSE 22  
  
RUN useradd \--create-home \--shell /bin/tunnelshell mysql  
  
RUN mkdir /var/www  
RUN chown root:root /var/www  
RUN chmod go-w /var/www  
  
ENTRYPOINT ["/usr/sbin/start"]  

