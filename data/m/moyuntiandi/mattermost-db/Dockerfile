FROM mattermost/mattermost-prod-db:3.10.0  
  
RUN apt-get update && apt-get install -y wget gcc make bzip2 postgresql-
server-dev-9.4 libpq-dev &&\  
wget -q -O - http://www.xunsearch.com/scws/down/scws-1.2.2.tar.bz2 | tar xjf -
&&\  
cd scws-1.2.2 &&\  
./configure && make install &&\  
cd ../ && rm -rf scws-1.2.2 &&\  
wget -q -O - https://github.com/amutu/zhparser/archive/0.1.4.tar.gz | tar xzf
- &&\  
cd zhparser-0.1.4 &&\  
SCWS_HOME=/usr/local make && make install &&\  
cd ../ && rm -rf zhparser-0.1.4 &&\  
apt-get remove \--purge -y wget gcc make bzip2 postgresql-server-dev-9.4
libpq-dev &&\  
apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*

