FROM mariadb:10.2  
RUN apt-get update && \  
apt-get install -y dnsutils net-tools && \  
apt-get clean  
  
COPY galera.cnf /etc/mysql/conf.d/galera.cnf  
COPY dcos-galera.sh /dcos-galera.sh  
  
ENTRYPOINT ["/dcos-galera.sh"]  

