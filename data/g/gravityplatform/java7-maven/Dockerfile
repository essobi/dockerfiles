FROM maven:3.3.3-jdk-7  
RUN \  
apt-get update && \  
apt-get install -y \  
openssh-server && \  
mkdir -p /var/run/sshd && \  
rm -f /etc/ssh/ssh_host_* && \  
apt-get clean  
  
EXPOSE 22  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["bash", "entrypoint.sh"]  
CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]  

