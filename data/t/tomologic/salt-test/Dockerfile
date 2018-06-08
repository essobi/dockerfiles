FROM debian:8  
RUN echo "deb http://repo.saltstack.com/apt/debian/7/amd64/latest wheezy main"
> /etc/apt/sources.list.d/salt-apt-repository.list  
COPY SALTSTACK-GPG-KEY.pub /root/SALTSTACK-GPG-KEY.pub  
  
RUN apt-key add /root/SALTSTACK-GPG-KEY.pub  
  
RUN apt-get update && \  
apt-get -y install salt-minion --no-install-recommends && \  
service salt-minion stop && \  
rm -rf /var/lib/apt/lists/*  
  
COPY minion /etc/salt/minion  
COPY run-salt-tests.sh /usr/bin/run-salt-tests.sh  
  
VOLUME ["/srv/salt", "/srv/pillar"]  
  
ENTRYPOINT ["run-salt-tests.sh"]  

