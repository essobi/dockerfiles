FROM node:4  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main 9.4' >
/etc/apt/sources.list.d/pgdg.list && apt-key adv --keyserver ha.pool.sks-
keyservers.net --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 && apt-get
update && apt-get install -y \  
postgresql-client-9.4 \  
librsvg2-dev \  
postgresql-client-9.4 \  
libpq5 \  
libpq-dev \  
redis-tools  
  
RUN echo 'postgres:5432:*:wirehead:rm3test' > ~/.pgpass && chmod 0600
~/.pgpass  
  
RUN mkdir /src  
  
WORKDIR /src  
RUN npm install rm3@0.3.3  
  
ADD setup.sh setup.sh  
  
EXPOSE 4000  

