FROM ubuntu:14.04  
RUN apt-get update \  
&& apt-get install -y net-tools nano curl openssh-server  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Generate different certs per image  
RUN sed -i 's/[# ]*PasswordAuthentication .*/PasswordAuthentication yes/'
/etc/ssh/sshd_config \  
&& sed -i 's/[# ]*PubkeyAuthentication .*/PubkeyAuthentication no/'
/etc/ssh/sshd_config \  
&& sed -i 's/[# ]*PermitRootLogin .*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
VOLUME /etc/ssh

