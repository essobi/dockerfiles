FROM codingwell/rpi-raspbian-qemu  
  
MAINTAINER J.P.C. Oudeman  
  
# Loosely based on instructions from
https://cwiki.apache.org/confluence/display/COUCHDB/Debian  
  
COPY assets/bin/entrypoint.sh /usr/local/bin  
RUN [ "cross-build-start" ]  
  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
curl \  
erlang-nox \  
erlang-dev \  
libmozjs185-1.0 \  
libmozjs185-dev \  
libnspr4 \  
libnspr4-0d \  
libnspr4-dev \  
libcurl4-openssl-dev \  
libicu-dev \  
sudo \  
wget \  
&& \  
# Set up a couchdb daemon account  
groupadd -r couchdb && \  
useradd -d /var/lib/couchdb -g couchdb couchdb && \  
mkdir -p /usr/local/lib/couchdb /usr/local/etc/couchdb \  
/usr/local/var/lib/couchdb /usr/local/var/log/couchdb
/usr/local/var/run/couchdb /var/lib/couchdb && \  
chown -R couchdb:couchdb /usr/local/lib/couchdb /usr/local/etc/couchdb \  
/usr/local/var/lib/couchdb /usr/local/var/log/couchdb
/usr/local/var/run/couchdb /var/lib/couchdb && \  
chmod -R g+rw /usr/local/lib/couchdb /usr/local/etc/couchdb \  
/usr/local/var/lib/couchdb /usr/local/var/log/couchdb
/usr/local/var/run/couchdb /var/lib/couchdb && \  
\  
# Install CouchDB  
wget --header="accept-encoding: gzip" http://www-
us.apache.org/dist/couchdb/source/1.6.1/apache-couchdb-1.6.1.tar.gz -O - | tar
-C /tmp -xz && \  
cd /tmp/apache-couchdb-* \  
&& ./configure --prefix=/usr/local --with-js-lib=/usr/lib --with-js-
include=/usr/include/mozjs --enable-init \  
&& make && make install && \  
\  
sed -e 's/^bind_address = .*$/bind_address = 0.0.0.0/' -i
/usr/local/etc/couchdb/default.ini && \  
\  
chmod +x /usr/local/bin/*.sh && \  
\  
# Cleanup  
apt-get purge -y libmozjs185-dev erlang-dev libnspr4-dev libcurl4-openssl-dev
curl libicu-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /tmp/apache-*  
  
RUN [ "cross-build-end" ]  
  
ENV COUCHDB_USER couchadmin  
ENV COUCHDB_PASSWORD couchpasswd  
ENV ERL_LIBS "/var/lib/couchdb/lib/erlang"  
  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["couchdb"]

