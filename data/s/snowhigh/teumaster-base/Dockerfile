FROM ubuntu:xenial  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y openssh-server vim python-dev iproute git python-virtualenv
libevent-dev python-libvirt beanstalkd sudo && \  
apt-get clean  
  
RUN wget https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:!Q@W3e4r' | chpasswd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN mkdir -m 700 /root/.ssh && rm -f /etc/ssh/sshd_config  
ADD sshd_config /etc/ssh/  
  
# Regenerating host key of sshd  
RUN rm -rf /etc/ssh/ssh_host* && \  
ssh-keygen -q -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa && \  
ssh-keygen -q -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa && \  
ssh-keygen -q -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa && \  
ssh-keygen -q -f /etc/ssh/ssh_host_ed25519_key -N '' -t ed25519  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

