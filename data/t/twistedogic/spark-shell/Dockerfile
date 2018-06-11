FROM twistedogic/spark-base  
MAINTAINER Jordan Li  
  
RUN \  
echo "# Install OpenSSH Server" ;\  
apt-get -q -y install openssh-server ;\  
mkdir -p /var/run/sshd ;\  
echo 'root:passw0rd' | chpasswd ;\  
\  
true  
  
COPY supervisord.conf /etc/supervisord.conf  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

