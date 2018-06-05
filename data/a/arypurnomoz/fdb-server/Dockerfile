# fdb-server: installs FDB server running in container  
FROM arypurnomoz/fdb-client  
  
RUN mkdir -p /etc/foundationdb && touch /etc/foundationdb/fdb.cluster  
  
ADD
https://foundationdb.com/downloads/f-afxudaxbxuuo/I_accept_the_FoundationDB_Community_License_Agreement/key-
value-store/3.0.5/foundationdb-server_3.0.5-1_amd64.deb /tmp/foundationdb-
server.deb  
RUN dpkg -i /tmp/foundationdb-server.deb  
  
RUN mv /etc/foundationdb/foundationdb.conf
/usr/lib/foundationdb/foundationdb.conf.orig  
RUN rm -rf /etc/foundationdb /var/lib/foundationdb/data  
VOLUME ["/etc/foundationdb", "/fdb-data"]  
  
EXPOSE 4500  
ADD docker-start.sh /usr/lib/foundationdb/  
  
RUN easy_install supervisor  
RUN mkdir -p /var/log/supervisor  
  
ADD supervisord.conf /etc/  
CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisord.conf"]  

