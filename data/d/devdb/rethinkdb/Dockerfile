# Version 1.0  
FROM abh1nav/baseimage:latest  
  
MAINTAINER Abhinav Ajgaonkar <abhinav316@gmail.com>  
  
RUN \  
echo "deb http://download.rethinkdb.com/apt `lsb_release -cs` main" >
/etc/apt/sources.list.d/rethinkdb.list ; \  
wget -O- http://download.rethinkdb.com/apt/pubkey.gpg | apt-key add - ; \  
apt-get update; \  
apt-get install -y rethinkdb; \  
mkdir -p /etc/service/rethinkdb  
  
EXPOSE 8080 28015 29015  
COPY run /etc/service/rethinkdb/  
  
WORKDIR /root  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

