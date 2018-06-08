FROM swift:4.0.3  
  
# Add MariaDB repository  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-key adv --recv-keys \--keyserver hkp://keyserver.ubuntu.com:80
0xF1656F24C74CD1D8 && \  
add-apt-repository 'deb [arch=amd64,i386,ppc64el]
http://ftp.yz.yamagata-u.ac.jp/pub/dbms/mariadb/repo/10.1/ubuntu xenial main'  
  
#  
RUN ln -fs /usr/share/zoneinfo/Etc/GMT /etc/localtime  
  
# Install dependency library  
RUN apt-get update && \  
apt-get install -y libxml2-dev libmariadbclient-dev git automake libtool
autoconf uuid-dev libssl-dev libz-dev unzip tzdata && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

