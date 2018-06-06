FROM ubuntu:trusty  
MAINTAINER Feng Honglin <hfeng@tutum.co>  
  
RUN apt-get update && \  
apt-get -y --no-install-recommends install openssh-server socat autossh && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists && \  
mkdir -p /var/run/sshd && \  
mkdir -p /root/.ssh && \  
sed -i "s/#PasswordAuthentication yes/PasswordAuthentication no/g"
/etc/ssh/sshd_config  
  
ADD scripts /  
RUN chmod +x /*.sh  
  
# EXPOSE 22  
CMD ["/run.sh"]  

