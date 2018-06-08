FROM relateiq/oracle-java7  
  
# pre-reqs  
RUN apt-get update && apt-get -y install python-software-properties python-
setuptools  
RUN easy_install supervisor  
  
# downloads  
RUN wget --progress=dot:mega
https://foundationdb.com/downloads/I_accept_the_FoundationDB_Community_License_Agreement/2.0.7/foundationdb-
clients_2.0.7-1_amd64.deb  
RUN wget --progress=dot:mega
https://foundationdb.com/downloads/I_accept_the_FoundationDB_Community_License_Agreement/sql-
layer/1.9.4/fdb-sql-layer-client-tools_1.9.4-1_all.deb  
RUN wget --progress=dot:mega
https://foundationdb.com/downloads/I_accept_the_FoundationDB_Community_License_Agreement/sql-
layer/1.9.4/fdb-sql-layer_1.9.4-1_all.deb  
RUN wget --progress=dot:mega
https://foundationdb.com/downloads/I_accept_the_FoundationDB_Community_License_Agreement/2.0.7/foundationdb-
server_2.0.7-1_amd64.deb  
  
#### fdb client  
RUN dpkg -i /foundationdb-clients_2.0.7-1_amd64.deb  
  
#### sql layer client  
RUN dpkg -i /fdb-sql-layer-client-tools_1.9.4-1_all.deb  
  
#### sql layer  
RUN dpkg -i /fdb-sql-layer_1.9.4-1_all.deb  
  
# backup config  
RUN mv /etc/foundationdb/sql /etc/fdb-sql  
  
#### fdb server  
# Prevent initialization by installer  
RUN mkdir -p /etc/foundationdb && touch /etc/foundationdb/fdb.cluster  
  
# fdb server  
RUN dpkg -i /foundationdb-server_2.0.7-1_amd64.deb  
  
RUN mv /etc/foundationdb/foundationdb.conf
/usr/lib/foundationdb/foundationdb.conf.orig  
RUN rm /etc/foundationdb/fdb.cluster  
RUN rm -rf /var/lib/foundationdb/data  
  
# VOLUME ["/etc/foundationdb", "/fdb-data"]  
# sql layer  
EXPOSE 15432  
# sql rest  
EXPOSE 8091  
# fdb server  
EXPOSE 4500  
ADD docker-sql-layer.sh /usr/lib/foundationdb/  
ADD docker-start.sh /usr/lib/foundationdb/  
ADD foundationdb.conf /etc/foundationdb/foundationdb.conf  
  
RUN mkdir -p /data  
RUN mkdir -p /logs  
RUN mkdir -p /var/log/supervisor  
  
ADD supervisord.conf /etc/  
CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisord.conf"]  

