# This file creates a container that runs Database (Percona) with Galera
Replication.  
FROM phusion/baseimage:latest  
MAINTAINER Rick Stokkingreef "rickstokking@gmail.com"  
# Base Deps  
RUN \  
apt-get update && apt-get install -yq \  
make \  
ca-certificates \  
net-tools \  
sudo \  
wget \  
vim \  
strace \  
lsof \  
netcat \  
lsb-release \  
locales \  
socat \  
\--no-install-recommends  
  
# generate a local to suppress warnings  
RUN locale-gen en_US.UTF-8  
  
RUN \  
apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A || \  
apt-key adv --keyserver hkp://keys.gnupg.net:80 --recv-keys 1C4CBDCDCD2EFD2A  
  
RUN \  
echo "deb http://repo.percona.com/apt `lsb_release -cs` main" >
/etc/apt/sources.list.d/percona.list && \  
echo "deb-src http://repo.percona.com/apt `lsb_release -cs` main" >>
/etc/apt/sources.list.d/percona.list && \  
ln -fs /bin/true /usr/bin/chfn && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y percona-xtradb-cluster-
client-5.6 percona-xtradb-cluster-server-5.6 percona-xtrabackup rsync percona-
xtradb-cluster-garbd-3.x haproxy && \  
sed -i 's/^\\(bind-address\s.*\\)/# \1/' /etc/mysql/my.cnf  
  
RUN rm -rf /var/lib/mysql/*  
  
# download latest stable etcdctl  
ADD https://s3-us-west-2.amazonaws.com/opdemand/etcdctl-v0.4.5
/usr/local/bin/etcdctl  
RUN chmod +x /usr/local/bin/etcdctl  
  
# install confd  
ADD https://s3-us-west-2.amazonaws.com/opdemand/confd-v0.5.0-json
/usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
  
# Define mountable directories.  
VOLUME ["/var/lib/mysql"]  
  
ADD . /app  
  
# Define working directory.  
WORKDIR /app  
  
RUN chmod +x /app/bin/*  
  
RUN mkdir -p /etc/my_init.d  
ADD start.sh /etc/my_init.d/start.sh  
  
# Define default command.  
CMD ["/sbin/my_init"]  
  
# Expose ports.  
EXPOSE 3306 4444 4567 4568  

