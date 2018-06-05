# alexindigo/couchdb  
FROM alexindigo/base-dev:ubuntu_12.04-1  
MAINTAINER Alex Indigo <iam@alexindigo.com>  
  
# CouchDB version  
ENV COUCHDB_VERSION 1.6.0  
# Distro URL  
ENV COUCHDB_URL
http://apache.tradebit.com/pub/couchdb/source/${COUCHDB_VERSION}/apache-
couchdb-${COUCHDB_VERSION}.tar.gz  
  
# Make DEBIAN_FRONTEND less chatty  
ENV DEBIAN_FRONTEND noninteractive  
  
# couchdb deps  
RUN apt-get install -y libmozjs185-dev libicu-dev libcurl4-gnutls-dev libtool
\  
erlang-base-hipe erlang-xmerl erlang-inets erlang-manpages erlang-dev erlang-
nox erlang-eunit  
  
# Fetch source code  
RUN mkdir -p /tmp/couchdb && \  
curl -s -o /tmp/couchdb.tar.gz ${COUCHDB_URL} && \  
tar -C /tmp/couchdb --strip-components 1 -xzf /tmp/couchdb.tar.gz && \  
rm /tmp/couchdb.tar.gz  
  
# Build  
RUN cd /tmp/couchdb && \  
./configure --prefix=/usr/local && \  
make && \  
make install && \  
rm -rf /tmp/couchdb  
  
# Configure  
RUN cp /usr/local/etc/logrotate.d/couchdb /etc/logrotate.d/couchdb && \  
cp /usr/local/etc/init.d/couchdb /etc/init.d/couchdb && \  
update-rc.d couchdb defaults && \  
sed -i'' '/COUCHDB_USER=/d' /usr/local/etc/default/couchdb && \  
sed -i'' 's/bind_address = 127.0.0.1/bind_address = 0.0.0.0/'
/usr/local/etc/couchdb/default.ini && \  
sed -i'' 's/secure_rewrites = true/secure_rewrites = false/'
/usr/local/etc/couchdb/default.ini  
  
# Reset DEBIAN_FRONTEND  
ENV DEBIAN_FRONTEND newt  
  
# Define mountable directories  
VOLUME ["/usr/local/var/log/couchdb", "/usr/local/var/lib/couchdb",
"/usr/local/etc/couchdb"]  
  
EXPOSE 5984  
# Reset DEBIAN_FRONTEND  
ENV DEBIAN_FRONTEND newt  
  
CMD ["/usr/local/bin/couchdb"]  

