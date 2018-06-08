FROM debian:jessie-slim  
  
MAINTAINER Robson Nascimento robsonvnasc@gmail.com  
ARG version=2.1.1  
ENV COUCHDB_VERSION=$version  
  
RUN adduser --system --no-create-home --shell /bin/bash --group --gecos
"CouchDB Administrator" couchdb  
  
RUN apt-get update -y && apt-get install -y --no-install-recommends \  
build-essential \  
pkg-config \  
libicu-dev \  
libmozjs185-dev \  
libcurl4-openssl-dev \  
git \  
tar \  
wget \  
curl \  
openssl \  
libssl-dev \  
ncurses-dev  
  
RUN cd /usr/src && wget http://www-
us.apache.org/dist/couchdb/source/$COUCHDB_VERSION/apache-
couchdb-$COUCHDB_VERSION.tar.gz && tar zxvf apache-
couchdb-$COUCHDB_VERSION.tar.gz  
RUN cd /usr/src && wget http://erlang.org/download/otp_src_18.2.tar.gz && tar
-xzvf otp_src_18.2.tar.gz  
RUN cd /usr/src/otp_src_18.2/ && ./configure && make && make install  
  
RUN erl -eval 'erlang:display(erlang:system_info(otp_release)), halt().'
-noshell  
  
RUN cd /usr/src/apache-couchdb-$COUCHDB_VERSION && ./configure --disable-docs
&& make release  
  
RUN cp -R /usr/src/apache-couchdb-$COUCHDB_VERSION/rel/couchdb /opt/ \  
&& apt-get purge -y --auto-remove \  
&& rm -rf /usr/src/otp_src_* \  
&& rm -rf /usr/src/apache-couchdb-$COUCHDB_VERSION* \  
&& mkdir /opt/couchdb/data  
  
COPY local.ini /opt/couchdb/etc/local.d/  
COPY startup.sh /opt/couchdb/startup.sh  
  
RUN chown -R couchdb:couchdb /opt/couchdb/ && chmod +x /opt/couchdb/startup.sh  
  
WORKDIR /opt/couchdb  
  
EXPOSE 5984 6984 4369 9100  
VOLUME ["/opt/couchdb/data"]  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["/opt/couchdb/startup.sh"]  

