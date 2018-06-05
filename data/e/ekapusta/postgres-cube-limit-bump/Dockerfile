FROM postgres:9.5  
  
RUN apt-get update \  
&& apt-get install --assume-yes wget unzip gcc make zlib1g-dev libreadline-dev
postgresql-server-dev-$PG_MAJOR bison flex \  
&& rm --recursive --force /var/lib/apt/lists/* \  
&& export PG_RELEASE=$(postgres --version | grep \--only-matching '[^ ]*$' |
sed 's/\\./_/g' | awk '{print toupper($0)}' | sed 's/BETA/_BETA/') \  
&& export
PG_RELEASE_URL=https://github.com/postgres/postgres/archive/REL$PG_RELEASE.zip
\  
&& wget --quiet --output-document=postgres.zip $PG_RELEASE_URL \  
&& unzip -q postgres.zip \  
&& mv postgres-* src-postgres \  
&& rm --force postgres.zip \  
&& cd src-postgres \  
&& ./configure \  
&& cd contrib/cube \  
&& sed --in-place 's/define CUBE_MAX_DIM (100)/define CUBE_MAX_DIM (128)/'
cubedata.h \  
&& make USE_PGXS=1 \  
&& make USE_PGXS=1 install \  
&& cd ../../.. \  
&& rm --recursive --force src-postgres  

