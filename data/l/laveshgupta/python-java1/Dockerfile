FROM ubuntu:14.04.2  
  
ENV ES_PKG_NAME elasticsearch-1.5.2  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
ENV ES_HEAP_SIZE 1g  
ENV LANG C.UTF-8  
  
RUN \  
cd / && \  
apt-get update && \  
apt-get purge -y python.* && \  
apt-get install -y --no-install-recommends autotools-dev blt-dev bzip2 dpkg-
dev gcc-multilib g++-multilib libbluetooth-dev libbz2-dev libexpat1-dev
libffi-dev libffi6 libffi6-dbg libgdbm-dev libgpm2 libncursesw5-dev
libreadline-dev libsqlite3-dev libssl-dev libssl-dev libtinfo-dev mime-support
netbase net-tools python-crypto python-mox3 python-pil python-ply quilt tk-dev
zlib1g-dev && \  
apt-get install -y --no-install-recommends autoconf automake bzr bzip2 ca-
certificates curl ecryptfs-utils file g++ gcc git imagemagick libbz2-dev
libc6-dev libcurl4-openssl-dev libevent-dev libffi-dev libglib2.0-dev libjpeg-
dev liblzma-dev libmagickcore-dev libmagickwand-dev libmysqlclient-dev
libncurses-dev libpq-dev libreadline-dev libsqlite3-dev libssl-dev libtool
libwebp-dev libxml2-dev libxslt-dev libyaml-dev make mercurial openssh-client
patch subversion wget xz-utils zlib1g-dev && \  
mkdir -p /usr/src/python && \  
curl -SL "https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz" -o
python.tgz && \  
tar -xzC /usr/src/python --strip-components=1 -f python.tgz && \  
rm python.tgz && \  
cd /usr/src/python && \  
apt-get update && \  
./configure --enable-shared --enable-unicode=ucs4 --enable-ipv6 && \  
make -j$(nproc) && \  
make install && \  
ldconfig && \  
curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python2 && \  
find /usr/local \\( -type d -a -name test -o -name tests \\) -o \\( -type f -a
-name '*.pyc' -o -name '*.pyo' \\) -exec rm -rf '{}' + && \  
cd / && \  
rm -rf /usr/src/python && \  
pip install cherrypy && \  
pip install pyyaml && \  
pip install elasticsearch && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get update && \  
apt-get install -yyq software-properties-common python-software-properties &&
\  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -qyy --no-install-recommends oracle-java8-installer oracle-
java8-set-default && \  
mkdir esdata && \  
mkdir esdata/encrypted && \  
mkdir esdata/decrypted && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
mkdir /es  
  
ADD es/ /es/  
  
ENV DATA_FLAG true  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
EXPOSE 9200  
EXPOSE 9300  
EXPOSE 80  
EXPOSE 8080  
  
CMD ["python2"]  
  

