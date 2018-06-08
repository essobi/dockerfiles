FROM gitlab/gitlab-ce:latest  
  
MAINTAINER Leonard Marschke <github@marschke.me>  
  
# Make SSH secure (check out https://github.com/arthepsy/ssh-audit)  
RUN echo "KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group-
exchange-sha256" >> /assets/sshd_config  
RUN echo "Ciphers
chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr"
>> /assets/sshd_config  
RUN echo "MACs hmac-sha2-512-etm@openssh.com,hmac-
sha2-256-etm@openssh.com,umac-128-etm@openssh.com" >> /assets/sshd_config  
  
RUN sed -i '/ssh_host_ecdsa_key/ d' /assets/sshd_config  

