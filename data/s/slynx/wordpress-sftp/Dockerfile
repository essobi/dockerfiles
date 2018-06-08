FROM debian:9.3  
MAINTAINER scurow  
  
RUN apt-get update && \  
apt-get -y install openssh-server && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /var/run/sshd && \  
rm -f /etc/ssh/ssh_host_*key*  
  
COPY sshd_config /etc/ssh/sshd_config  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
EXPOSE 22  
ENTRYPOINT ["/entrypoint.sh"]

