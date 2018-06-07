FROM mysql  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
git \  
wget \  
cmake \  
autoconf \  
libncurses5-dev \  
bison \  
libmysqlclient-dev \  
mysql-client  
  
RUN mkdir build && \  
cd build && \  
git clone https://github.com/infusion/udf_infusion.git && \  
cd udf_infusion && \  
./configure && \  
make && \  
make install  
  
RUN apt-get install -y libmysqlclient-dev libpcre3-dev && \  
apt-get install -y libtool automake autoconf autogen && \  
git clone https://github.com/mysqludf/lib_mysqludf_preg.git && \  
cd lib_mysqludf_preg && \  
aclocal && \  
automake --add-missing && \  
autoreconf --force --install && \  
./configure && \  
make && \  
make install && \  
echo "general_log_file = /var/log/query.log" >> /etc/mysql/conf.d/docker.cnf
&& \  
echo "general_log = 1" >> /etc/mysql/conf.d/docker.cnf && \  
service mysql start && \  
mysql -uroot -pcicero <./installdb.sql  

