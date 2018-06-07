FROM python:2.7  
ENV SSH_SERVER_KEYS /etc/ssh/host_keys/  
  
ADD entrypoint.sh /bin/  
  
EXPOSE 22  
RUN apt-get -y update && apt-get -y install openssh-server && \  
mkdir -p ${SSH_SERVER_KEYS} && \  
echo "HostKey ${SSH_SERVER_KEYS}ssh_host_rsa_key" >> /etc/ssh/sshd_config && \  
echo "HostKey ${SSH_SERVER_KEYS}ssh_host_dsa_key" >> /etc/ssh/sshd_config && \  
echo "HostKey ${SSH_SERVER_KEYS}ssh_host_ecdsa_key" >> /etc/ssh/sshd_config &&
\  
echo "HostKey ${SSH_SERVER_KEYS}ssh_host_ed25519_key" >> /etc/ssh/sshd_config
&& \  
sed -i "s/#PermitRootLogin.*/PermitRootLogin\ yes/" /etc/ssh/sshd_config  
  
VOLUME ["${SSH_SERVER_KEYS}"]  
  
ENTRYPOINT ["/bin/entrypoint.sh"]  
  
CMD ["/usr/sbin/sshd", "-D", "-e"]  

