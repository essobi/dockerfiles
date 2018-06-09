FROM postgres:9.6  
  
# install plv8 extension, disabling V8 tests to shorten build time  
RUN apt-get -y update &&\  
apt-get -y \--no-install-recommends install wget ca-certificates curl git
python build-essential postgresql-server-dev-9.6 &&\  
mkdir -p /tmp/build &&\  
cd /tmp/build &&\  
wget https://github.com/plv8/plv8/archive/v2.1.0.tar.gz &&\  
tar -xvzf v2.1.0.tar.gz &&\  
cd plv8-2.1.0 &&\  
make -f Makefile.v8 build/v8-git-mirror-5.8.301 &&\  
sed -i '/\btest\b/d' build/v8-git-mirror-5.8.301/gypfiles/all.gyp &&\  
make static PG_CONFIG=/usr/lib/postgresql/9.6/bin/pg_config &&\  
make install PG_CONFIG=/usr/lib/postgresql/9.6/bin/pg_config &&\  
strip /usr/lib/postgresql/9.6/lib/plv8.so &&\  
rm -rf /tmp/build &&\  
apt-get -y remove wget curl git python build-essential postgresql-server-
dev-9.6 &&\  
apt-get clean  
  
# download dictionary files  
COPY fetch-dictionaries /usr/share/postgresql/9.6/tsearch_data  
RUN apt-get -y update &&\  
apt-get -y install wget &&\  
cd /usr/share/postgresql/9.6/tsearch_data &&\  
./fetch-dictionaries &&\  
apt-get -y remove wget &&\  
apt-get clean  
  
CMD ["postgres", "-c", "plv8.start_proc=public.plv8_init"]  

