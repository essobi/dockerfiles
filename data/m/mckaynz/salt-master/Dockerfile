FROM ubuntu  
MAINTAINER McKay Software <opensource@mckaysoftware.co.nz>  
  
VOLUME /etc/salt/master.d  
VOLUME /etc/salt/pki  
VOLUME /srv/salt  
VOLUME /var/cache/salt  
VOLUME /var/logs/salt  
  
EXPOSE 4505 4506  
ENTRYPOINT ["/usr/bin/salt-master"]  
CMD ["--log-level=error"]  
  
RUN export DEBIAN_FRONTEND=noninteractive &&\  
apt update && apt install -y wget python-pip tmux fish git vim && pip install
progressbar &&\  
echo "set-option -g default-shell '/usr/bin/fish'" >> /root/.tmux.conf &&\  
wget -O - https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-
GPG-KEY.pub | apt-key add - &&\  
echo "deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial main"
> /etc/apt/sources.list.d/saltstack.list &&\  
apt update && apt install -y salt-master &&\  
apt remove -y wget && apt autoremove -y &&\  
rm -rf /var/lib/apt/lists/*  

