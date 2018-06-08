FROM postgres:9.6  
  
RUN buildDependencies="ca-certificates \  
libsybdb5 \  
freetds-dev \  
freetds-common \  
freetds-bin \  
wget \  
gcc \  
make \  
postgresql-server-dev-$PG_MAJOR" \  
&& apt-get update \  
&& apt-get install -y ${buildDependencies} \  
&& wget https://github.com/tds-fdw/tds_fdw/archive/v1.0.8.tar.gz \  
&& tar -xvzf v1.0.8.tar.gz \  
&& cd tds_fdw-1.0.8 \  
&& make USE_PGXS=1 \  
&& make USE_PGXS=1 install \  
&& sed -i '/# TDS protocol version/a \\ttds version=7.0'
/etc/freetds/freetds.conf  

