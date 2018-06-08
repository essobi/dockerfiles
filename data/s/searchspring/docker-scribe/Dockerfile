FROM debian:wheezy  
  
ENV DOCKERIZE_VERSION=v0.5.0 \  
PORT=1463 \  
MAX_MSG_PER_SECOND=2000000 \  
CHECK_INTERVAL=3 \  
REMOTE_HOST=ScribeEast-369094026.us-east-1.elb.amazonaws.com \  
REMOTE_PORT=1463 \  
FILE_PATH=/mnt/scribe \  
MASTERNODE=false \  
PYTHONPATH=/usr/lib/python2.7/site-packages  
  
  
  
RUN apt-get update -q && \  
apt-get install -q -y --no-install-recommends --no-install-suggests \  
autoconf \  
ca-certificates \  
build-essential \  
libcurl4-openssl-dev \  
libssl-dev \  
libevent-dev \  
unzip \  
libboost-dev \  
libboost-all-dev \  
python \  
flex \  
bison \  
libtool \  
pkg-config \  
automake \  
wget \  
tar \  
gzip && \  
wget -q http://archive.apache.org/dist/thrift/0.8.0/thrift-0.8.0.tar.gz && \  
echo "MD5 (thrift-0.8.0.tar.gz) = d29dfcd38d476cbc420b6f4d80ab966c" >
thrift-0.8.0.tar.gz.md5 && \  
md5sum -c thrift-0.8.0.tar.gz.md5 | grep OK && \  
tar -xzvf thrift-0.8.0.tar.gz && \  
cd thrift-0.8.0 && \  
./configure && \  
make install && \  
cd contrib/fb303 && \  
./bootstrap.sh && \  
./configure CPPFLAGS="-DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H" && \  
make install && \  
echo -e "/usr/local/lib64\n/usr/local/lib" > /etc/ld.so.conf.d/usrlocal.conf
&& \  
ldconfig && \  
wget https://github.com/facebookarchive/scribe/archive/master.zip && \  
unzip master.zip && \  
cd scribe-master && \  
./bootstrap.sh --with-boost-filesystem=boost_filesystem --with-boost-
system=boost_system && \  
./configure --with-boost-filesystem=boost_filesystem --with-boost-
system=boost_system CPPFLAGS="-DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H" && \  
make install && \  
mv examples/scribe_c* /usr/local/bin/  
  
RUN cd /root && \  
rm -rf thrift-0.8.0* scribe-master && \  
mkdir /templates /etc/scribed  
  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&
\  
rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
ADD templates/default.conf.tmpl /templates/default.conf.tmpl  
VOLUME /var/log  
CMD dockerize -template /templates/default.conf.tmpl:/etc/scribed/default.conf
-stdout /var/log/scribed.log /usr/local/bin/scribed -c
/etc/scribed/default.conf  

