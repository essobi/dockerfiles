FROM wonkywumpus/easy-sshd-ubuntu-1604:0.10  
  
RUN apt-get update  
  
# Boost package required as per MariaDB Installation prereqs  
RUN apt-get -y install libboost-all-dev  
  
# Other packages required as per MariaDB Installation prereqs  
RUN apt-get -y install tzdata libtcl8.6 expect perl openssl file sudo libdbi-
perl libboost-all-dev libreadline-dev rsync libsnappy1v5 net-tools libdbd-
mysql-perl  
  
# syslog required for logging  
RUN apt-get -y install rsyslog  
  
#RUN curl -o /root/mariadb-columnstore-1.0.11-1-xenial.x86_64.deb.tar.gz
https://downloads.mariadb.com/ColumnStore/1.0.11/ubuntu/dists/xenial/main/binary_amd64/mariadb-
columnstore-1.0.11-1-xenial.x86_64.deb.tar.gz  
  
#RUN curl -o /root/mariadb-columnstore-1.1.0-1-xenial.x86_64.deb.tar.gz
https://downloads.mariadb.com/ColumnStore/1.1.0/ubuntu/dists/xenial/main/binary_amd64/mariadb-
columnstore-1.1.0-1-xenial.x86_64.deb.tar.gz  
  
RUN curl -o /root/mariadb-columnstore-1.1.2-1-xenial.x86_64.deb.tar.gz
https://downloads.mariadb.com/ColumnStore/1.1.2/ubuntu/dists/xenial/main/binary_amd64/mariadb-
columnstore-1.1.2-1-xenial.x86_64.deb.tar.gz  

