FROM alpine:latest  
MAINTAINER polandj  
  
  
RUN apk update && apk add openssh  
  
RUN echo "Welcome to Alpine! <http://wiki.alpinelinux.org>" > /etc/motd  
  
RUN echo "PubkeyAcceptedKeyTypes=+ssh-dss" > /etc/ssh/ssh_config  
  
RUN echo "PasswordAuthentication no" > /etc/ssh/sshd_config \  
&& echo "Protocol 2" >> /etc/ssh/sshd_config  
  
RUN echo "KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group-
exchange-sha256" >> /etc/ssh/sshd_config \  
&& echo "Ciphers
chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr"
>> /etc/ssh/sshd_config \  
&& echo "MACs hmac-sha2-512-etm@openssh.com,hmac-
sha2-256-etm@openssh.com,hmac-
ripemd160-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-
sha2-256,hmac-ripemd160,umac-128@openssh.com" >> /etc/ssh/sshd_config  
  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
EXPOSE 22  
CMD ["sh", "/run.sh"]  

