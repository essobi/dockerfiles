FROM debian:wheezy  
  
MAINTAINER Krzysztof Kobrzak <chris.kobrzak@gmail.com>  
  
ENV COUCHDB_VERSION 1.6.1  
COPY scripts /usr/local/bin  
  
RUN \  
groupadd -r couchdb && \  
useradd -m -d /var/lib/couchdb -g couchdb couchdb && \  
chown -R couchdb:couchdb /usr/local/bin/* && \  
chmod -R +x /usr/local/bin/*  
  
# CouchDB dependencies, installation from source, required utilities etc.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive && \  
apt-get install -y -qq --no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
erlang-dev \  
erlang-nox \  
libcurl4-openssl-dev \  
libicu-dev \  
libmozjs185-1.0 \  
libmozjs185-dev \  
netcat \  
pwgen && \  
cd /usr/src && \  
curl -s -o apache-couchdb.tar.gz
http://mirror.ox.ac.uk/sites/rsync.apache.org/couchdb/source/$COUCHDB_VERSION/apache-
couchdb-$COUCHDB_VERSION.tar.gz && \  
tar -xzf apache-couchdb.tar.gz && \  
cd /usr/src/apache-couchdb-$COUCHDB_VERSION && \  
./configure --with-js-lib=/usr/lib --with-js-include=/usr/include/mozjs && \  
make --quiet && \  
make install && \  
apt-get purge -y \  
binutils \  
build-essential \  
cpp \  
libcurl4-openssl-dev \  
libnspr4-dev \  
make \  
perl && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /usr/src/apache* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
RUN \  
sed -e 's/^bind_address = .*$/bind_address = 0.0.0.0/' -i
/usr/local/etc/couchdb/default.ini && \  
# CORS support in CouchDB  
sed -i '/\\[httpd\\]/a enable_cors = true' /usr/local/etc/couchdb/local.ini &&
\  
echo '[cors] \  
\norigins = * \  
\ncredentials = true \  
\nheaders = accept, authorization, content-type, origin, referer \  
\nmethods = GET, PUT, POST, HEAD, DELETE' >> /usr/local/etc/couchdb/local.ini  
  
RUN \  
touch /var/lib/couchdb/couchdb-not-inited && \  
chown -R couchdb:couchdb \  
/usr/local/etc/couchdb \  
/usr/local/lib/couchdb \  
/usr/local/var/lib/couchdb \  
/usr/local/var/log/couchdb \  
/usr/local/var/run/couchdb && \  
chmod -R 0770 \  
/usr/local/etc/couchdb \  
/usr/local/var/lib/couchdb \  
/usr/local/var/log/couchdb \  
/usr/local/var/run/couchdb  
  
USER couchdb  
  
EXPOSE 5984  
WORKDIR /var/lib/couchdb  
  
# Expose our data, logs and configuration volumes  
VOLUME ["/var/lib/couchdb", "/usr/local/var/log/couchdb",
"/usr/local/etc/couchdb"]  
  
ENTRYPOINT ["start_couchdb"]  
CMD [""]  

