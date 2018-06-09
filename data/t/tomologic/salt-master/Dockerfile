FROM debian:8  
COPY salt-apt-repository.list /etc/apt/sources.list.d/salt-apt-repository.list  
COPY debian-salt-team-joehealy.gpg.key /root/debian-salt-team-joehealy.gpg.key  
  
RUN apt-key add /root/debian-salt-team-joehealy.gpg.key  
  
RUN apt-get update && \  
apt-get -y install salt-master salt-minion --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/srv/salt", "/srv/pillar"]  
  
CMD ["salt"]  

