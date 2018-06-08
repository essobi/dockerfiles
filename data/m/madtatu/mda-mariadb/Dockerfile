FROM mariadb:10.0.17  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -q -y; \  
apt-get upgrade -q -y; \  
apt-get dist-upgrade  
  
RUN apt-get install -q -y git \  
gcc \  
binutils \  
make \  
wget \  
autoconf \  
libmariadbclient-dev \  
libpcre3-dev \  
libtool  
  
RUN cd /tmp; \  
wget http://ftp.gnu.org/gnu/automake/automake-1.13.4.tar.gz; \  
tar -xvzf automake-1.13.4.tar.gz; \  
mv automake-1.13.4 /opt; \  
rm -f /tmp/automake-1.13.4.tar.gz  
  
RUN cd /opt/automake-1.13.4; \  
./configure; \  
make; \  
make install  
  
RUN mv /usr/local/share/aclocal /usr/local/share/aclocal.old; \  
ln -s /usr/share/aclocal /usr/local/share/aclocal  
  
RUN git clone \--depth=1 https://github.com/mysqludf/lib_mysqludf_preg
/opt/lib_mysqludf_preg/  
  
RUN cd /opt/lib_mysqludf_preg;\  
./configure ;\  
make ;\  
make install  
  
ADD scripts/startup.sh /startup.sh  
ADD etc/mysql/conf.d/mysqld_safe_syslog.cnf
/etc/mysql/conf.d/mysqld_safe_syslog.cnf  
ADD etc/mysql/conf.d/spinning.cnf /etc/mysql/conf.d/spinning.cnf  
  
CMD ["/bin/bash", "/startup.sh", "mysqld", "--local-infile", "--log-bin-trust-
function-creators=1", "--skip-name-resolve"]  

