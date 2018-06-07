FROM konstruktoid/alpine  
  
RUN apk update && \  
apk upgrade && \  
apk add --update acf-openssh  
  
COPY files/sshd_config /etc/ssh/sshd_config  
  
RUN ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa && \  
ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa  
  
ENTRYPOINT ["/usr/sbin/sshd"]  
CMD ["-D"]  

