FROM dockerfile/supervisor  
  
RUN \  
apt-get update && \  
apt-get install -y openssh-server && \  
mkdir -p /var/run/sshd && \  
echo "root:password" | chpasswd && \  
sed -i.bak -e 's/PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
  
ADD ssh.conf /etc/supervisor/conf.d/ssh.conf  
  
EXPOSE 22  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

