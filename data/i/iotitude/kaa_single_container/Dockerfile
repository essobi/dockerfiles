FROM ubuntu:14.04  
EXPOSE 22 8080 9888 9889 9997 9999  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
curl \  
software-properties-common \  
wget  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
apt-get install -y python-software-properties && \  
apt-get install -y iptables && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db  
RUN add-apt-repository 'deb http://mirror.jmu.edu/pub/mariadb/repo/5.5/ubuntu
trusty main'  
RUN apt-get update  
RUN apt-get install -y mariadb-galera-server galera  
RUN apt-get install -y rsync  
#RUN mysql -u root "CREATE USER 'sqladmin'@'localhost' IDENTIFIED BY
'admin';GRANT ALL PRIVILEGES ON *.* TO 'sqladmin'@'localhost' WITH GRANT
OPTION;FLUSH PRIVILEGES;CREATE DATABASE kaa;"  
RUN apt-get install -y zookeeperd  
RUN echo "deb http://www.apache.org/dist/cassandra/debian 35x main" | sudo tee
-a /etc/apt/sources.list.d/cassandra.sources.list  
RUN curl -L http://debian.datastax.com/debian/repo_key | sudo apt-key add -  
RUN apt-get update  
RUN apt-get install -y --force-yes cassandra=3.5  
RUN apt-get install -y libjna-java  
RUN wget https://github.com/kaaproject/kaa/releases/download/v0.9.0/kaa-
deb-0.9.0.tar.gz  
RUN tar -xvf kaa-deb-*.tar.gz  
RUN dpkg -i deb/kaa-node.deb  
RUN sed -i '3s/.*/nosql_db_provider_name=cassandra/' /etc/kaa-node/conf/nosql-
dao.properties  
RUN wget
https://raw.githubusercontent.com/kaaproject/kaa/master/server/containers/docker/node/config_listener.sh  
RUN chmod 777 config_listener.sh  
RUN service mysql start  
#RUN service cassandra start  
#RUN cqlsh localhost -f /etc/kaa-node/conf/cassandra.cql  
CMD bash -c "/config_listener.sh && /usr/bin/kaa-node start && while true; do
sleep 1; done"  

