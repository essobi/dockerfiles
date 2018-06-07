FROM nlesc/xenon-hdfs  
MAINTAINER Atze van der Ploeg "a.vanderploeg@esciencecenter.nl"  
RUN apk add --no-cache krb5-server krb5 supervisor  
  
# Copy the kerberos config.  
COPY krb5.conf /etc/krb5.conf  
COPY kadm5.acl /var/lib/krb5kdc/kadm5.acl  
COPY kdb.conf /var/lib/krb5kdc/kdb.conf  
COPY supervisord.conf /etc/supervisord.conf  
  
RUN printf "javagat\njavagat\n" | kdb5_util create -r esciencecenter.nl &&\  
kadmin.local -q "addprinc -pw javagat admin/admin@esciencecenter.nl" &&\  
kadmin.local -q "addprinc -pw javagat xenon@esciencecenter.nl" &&\  
kadmin.local -q "addprinc -randkey hdfs/localhost@esciencecenter.nl" &&\  
kadmin.local -q "addprinc -randkey HTTP/localhost@esciencecenter.nl" &&\  
kadmin.local -q "ktadd -norandkey -k /opt/hadoop/hdfs.keytab
hdfs/localhost@esciencecenter.nl HTTP/localhost@esciencecenter.nl" &&\  
chmod 400 /opt/hadoop/hdfs.keytab  
  
# Copy the updated HDFS config.  
COPY etc/hadoop/core-site.xml etc/hadoop/core-site.xml  
COPY etc/hadoop/hdfs-site.xml etc/hadoop/hdfs-site.xml  
COPY etc/hadoop/ssl-server.xml etc/hadoop/ssl-server.xml  
COPY etc/hadoop/ssl-client.xml etc/hadoop/ssl-client.xml  
  
# Copy keys and scripts.  
COPY keys/keystore.jks /opt/hadoop/keystore.jks  
COPY cmd.sh /cmd.sh  
COPY loginxenon.sh /loginxenon.sh  
  
# Make scripts executable  
RUN /bin/chmod +x /cmd.sh && \  
/bin/chmod +x /loginxenon.sh  
  
# hdfs://localhost:8020  
EXPOSE 749 464 88  
EXPOSE 50470  
EXPOSE 50475  
CMD /cmd.sh  
  
HEALTHCHECK \--interval=1s CMD test -f /opt/hadoop/up || exit 1  
  

