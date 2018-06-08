FROM phusion/baseimage:latest  
  
VOLUME /config  
COPY entrypoint.sh /entrypoint  
  
RUN apt-get update && \  
apt-get -y install openssh-server && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /var/run/sshd /etc/default/sshd && \  
rm -f /etc/ssh/ssh_host_*key* && \  
chmod +x /entrypoint  
  
COPY sshd_config /etc/default/sshd/sshd_config  
  
EXPOSE 22  
ENTRYPOINT ["/entrypoint"]  

