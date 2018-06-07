FROM phusion/baseimage  
  
MAINTAINER Xadozuk <xadozuk@gmail.com>  
  
RUN add-apt-repository ppa:deluge-team/ppa && \  
apt-get update && \  
apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \  
apt-get install -y deluged deluge-webui && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY ssh/sshd_append /etc/ssh/sshd_append  
COPY my_init.d /etc/my_init.d  
COPY deluge /deluge  
COPY service /etc/service  
  
RUN mkdir -p /deluge/deluged /deluge/deluge-web /sftp/torrents && \  
chmod 755 /sftp && \  
ln -s /sftp/torrents /downloads && \  
useradd -Mr seedbox && \  
chown -R seedbox:seedbox /deluge /sftp/torrents && \  
sed -i "s/ChallengeResponseAuthentication no/ChallengeResponseAuthentication
yes/" /etc/ssh/sshd_config && \  
cat /etc/ssh/sshd_append >> /etc/ssh/sshd_config && \  
rm -f /etc/ssh/sshd_append /etc/service/sshd/down  
  
EXPOSE 22 8080 31000-31010 31000-31010/udp  
  
VOLUME ["/deluge", "/sftp/torrents"]  
  
CMD ["/sbin/my_init"]  

