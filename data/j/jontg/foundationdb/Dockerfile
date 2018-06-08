FROM ubuntu:14.10  
RUN echo 'deb http://archive.ubuntu.com/ubuntu precise main universe' >
/etc/apt/sources.list && \  
echo 'deb http://archive.ubuntu.com/ubuntu precise-updates universe' >>
/etc/apt/sources.list && \  
apt-get update  
  
#Prevent daemon start during install  
RUN dpkg-divert --local \--rename --add /sbin/initctl && rm /sbin/initctl &&
ln -s /bin/true /sbin/initctl  
  
#Supervisord  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y supervisor && mkdir -p
/var/log/supervisor  
CMD ["/usr/bin/supervisord", "-n"]  
  
#Utilities  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget ca-certificates  
  
#Hack to avoid install problem  
RUN mkdir /etc/foundationdb && touch /etc/foundationdb/fdb.cluster  
  
#FoundationDB Client  
RUN wget
https://foundationdb.com/downloads/token/adfb8e3f-e29c-4ea7-a4f9-b470ecd9a6be/key-
value-store/3.0.7/foundationdb-clients_3.0.7-1_amd64.deb && \  
dpkg -i foundationdb-clients_3.0.7-1_amd64.deb && \  
rm foundationdb-clients_*.deb  
  
#FoundationDB Server  
RUN wget
https://foundationdb.com/downloads/token/5976b448-cd09-4de1-8681-73a156dbbb6a/key-
value-store/3.0.7/foundationdb-server_3.0.7-1_amd64.deb && \  
dpkg -i foundationdb-server_3.0.7-1_amd64.deb && \  
rm foundationdb-server_*.deb  
  
#Setup proper ownership and permissions  
ADD etc /etc/foundationdb  
RUN chown -f foundationdb:foundationdb /etc/foundationdb/fdb.cluster && \  
chmod -f 0644 /etc/foundationdb/fdb.cluster  
  
ADD supervisord-foundationdb.conf /etc/supervisor/conf.d/  
ADD docker-start.sh /usr/lib/foundationdb/  
  
EXPOSE 4500  
RUN rm -rf /tmp/*  

