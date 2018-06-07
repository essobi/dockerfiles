FROM ubuntu:16.04  
  
RUN set -ex \  
&& apt-get update && apt-get install -y openssh-server \  
&& mkdir /var/run/sshd \  
&& echo 'root:screencast' | chpasswd \  
&& sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& echo "GatewayPorts yes" >> /etc/ssh/sshd_config \  
# SSH login fix. Otherwise user is kicked off after login  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
# install cleanup as per https://docs.docker.com/engine/userguide/eng-
image/dockerfile_best-practices/#apt-get  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

