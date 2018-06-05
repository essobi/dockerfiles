FROM camerontaylor/postgres-plv8:9.6-2.1  
  
MAINTAINER Cameron Taylor <cameron.taylor@webfrontgears.com>  
  
RUN buildDependencies="make curl build-essential ca-certificates postgresql-
server-dev-$PG_MAJOR unzip" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends postgresql-$PG_MAJOR-mysql-fdw
${buildDependencies} \  
&& mkdir -p /tmp/build \  
&& curl -o /tmp/build/pg_datatype_password.zip -SL
"https://github.com/ozum/pg_datatype_password/archive/master.zip" \  
&& cd /tmp/build/ \  
&& unzip pg_datatype_password.zip \  
&& cd pg_datatype_password-master \  
&& make install \  
&& cd /tmp/build/ \  
&& curl -o /tmp/build/zson.zip -SL
"https://github.com/postgrespro/zson/archive/v1.1.zip" \  
&& unzip zson.zip \  
&& cd zson-1.1 \  
&& make \  
&& make install \  
&& cd / \  
&& apt-get clean \  
&& apt-get remove -y ${buildDependencies} \  
&& apt-get autoremove -y \  
&& rm -rf /tmp/build /var/lib/apt/lists/*  
  
COPY postgresql.conf /var/lib/postgresql/data/  

