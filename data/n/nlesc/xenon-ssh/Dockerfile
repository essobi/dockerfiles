FROM nlesc/xenon-alpine-base  
MAINTAINER Stefan Verhoeven "s.verhoeven@esciencecenter.nl"  
# install openssh and configure for rsa, dsa, and ecdsa keys  
# for ssh clients within this docker image,  
# - disable strict hostkey checking  
# - disable hashing of host names in known_hosts file  
RUN apk add --no-cache openssh && \  
ssh-keygen -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -N "" -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key && \  
ssh-keygen -N "" -t ed25519 -f /etc/ssh/ssh_host_ed25519_key && \  
echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \  
echo "HashKnownHosts no" >> /etc/ssh/ssh_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-De"]  
  
# define the test that tells us if the docker container is healthy  
HEALTHCHECK \--interval=1s CMD ssh -i /home/xenon/.ssh/id_rsa xenon@localhost
/bin/true || exit 1  

