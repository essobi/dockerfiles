FROM kalilinux/kali-linux-docker  
  
RUN apt-get update -y && apt-get install -y nikto w3af metasploit openssh-
server  
RUN \  
mkdir -p /var/run/sshd ;\  
echo 'root:passw0rd' | chpasswd ;\  
\  
true  
  
ADD sshd_config /etc/ssh/sshd_config  
  
CMD ["/usr/sbin/sshd","-D"]  

