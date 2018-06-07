FROM centos  
  
COPY ./mongodb/mongodb.repo /etc/yum.repos.d/mongodb-enterprise-2.6.repo  
COPY ./mongodb/mongodb.pem /etc/ssl/mongodb.pem  
  
RUN set -xe \  
&& mkdir -p /data/db \  
&& yum install -y mongodb-enterprise-2.6.9 \  
mongodb-enterprise-server-2.6.9 \  
mongodb-enterprise-shell-2.6.9 \  
mongodb-enterprise-mongos-2.6.9 \  
mongodb-enterprise-tools-2.6.9  
  
EXPOSE 27017  
ENTRYPOINT ["/usr/bin/mongod", "--sslMode", "requireSSL", "--sslPEMKeyFile",
"/etc/ssl/mongodb.pem"]  

