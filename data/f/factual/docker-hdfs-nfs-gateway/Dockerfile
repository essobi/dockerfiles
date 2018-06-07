FROM factual/docker-cdh5-base  
  
RUN apt-get update && apt-get install -y hadoop-hdfs-nfs3 ldap-auth-client
nscd  
  
ADD bootstrap.sh /etc/my_init.d/099_bootstrap  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 4242 2049

