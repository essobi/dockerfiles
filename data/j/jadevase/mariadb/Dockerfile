FROM ubuntu  
MAINTAINER Jadevase <jadevase@163.com>  
  
# Install MariaDB.  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xF1656F24C74CD1D8 && \  
add-apt-repository 'deb [arch=amd64,i386,ppc64el]
http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.1/ubuntu zesty main' && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y mariadb-server && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
sed -i 's/^\\(bind-address\s.*\\)/# \1/' /etc/mysql/my.cnf && \  
echo "mysqld_safe &" > /tmp/config && \  
echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \  
echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" IDENTIFIED by
\"Jason@101\" WITH GRANT OPTION;'" >> /tmp/config && \  
bash /tmp/config && \  
rm -f /tmp/config  
  
# Define mountable directories.  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["mysqld_safe"]  
  
# Expose ports.  
EXPOSE 3306  

