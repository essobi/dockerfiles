FROM ubuntu:16.04  
MAINTAINER Akihiro Uchida <uchida@turbare.net>  
RUN apt-get update\  
&& apt-get install -y --no-install-recommends openssh-server sudo python
python-apt\  
&& apt-get clean  
RUN mkdir /var/run/sshd\  
&& sed -i 's|^PermitRootLogin\s+.*|PermitRootLogin yes|' /etc/ssh/sshd_config\  
&& sed -i 's|session\s*required\s*pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN echo 'root:root' | chpasswd\  
&& useradd -m ubuntu\  
&& usermod -a -G sudo ubuntu\  
&& echo 'ubuntu:ubuntu' | chpasswd  
CMD ["/usr/sbin/sshd", "-D"]  

