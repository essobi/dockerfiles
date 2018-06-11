FROM postgres:9.6.1  
RUN buildDeps="git \  
build-essential \  
postgresql-server-dev-all \  
postgresql-common \  
protobuf-c-compiler \  
libprotobuf-c0-dev \  
libpq-dev \  
ca-certificates" \  
&& apt-get -yqq update \  
&& apt-get install -yq --no-install-recommends ${buildDeps} \  
&& git clone https://github.com/citusdata/cstore_fdw.git /cstore_fdw \  
&& cd /cstore_fdw \  
&& make \  
&& make install \  
&& removeDeps=" git \  
build-essential \  
protobuf-c-compiler \  
libprotobuf-c0-dev \  
libpq-dev \  
ca-certificates" \  
&& apt-get purge -y ${removeDeps} \  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& rm -rf /cstore_fdw  
  
ADD ./config/postgresql.conf.sample
/usr/share/postgresql/postgresql.conf.sample  
ADD ./example/tables2.sql /docker-entrypoint-initdb.d  

