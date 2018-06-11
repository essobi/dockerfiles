FROM postgres:10 AS build  
  
ENV PLV8_VERSION=v2.3.3  
  
RUN apt-get update && apt-get upgrade \  
&& apt-get install -y git curl glib2.0 libc++-dev python python-pip libv8-dev
postgresql-server-dev-$PG_MAJOR  
RUN pip install pgxnclient  
RUN pgxn install plv8  
  
  
FROM postgres:10 AS final  
  
RUN apt-get update && apt-get upgrade \  
&& apt-get install -y libc++-dev  
  
COPY \--from=build /usr/share/postgresql/10/extension/plcoffee*
/usr/share/postgresql/10/extension/  
COPY \--from=build /usr/share/postgresql/10/extension/plls*
/usr/share/postgresql/10/extension/  
COPY \--from=build /usr/share/postgresql/10/extension/plv8*
/usr/share/postgresql/10/extension/  
COPY \--from=build /usr/lib/postgresql/10/lib/plv8-2.3.3.so
/usr/lib/postgresql/10/lib/plv8-2.3.3.so  
COPY \--from=build /usr/lib/postgresql/10/lib/pgxs
/usr/lib/postgresql/10/lib/pgxs  
  
COPY \--from=build /usr/lib/postgresql/10/bin/pg_config
/usr/lib/postgresql/10/bin/pg_config  
  
RUN chmod -R 644 /usr/share/postgresql/10/extension/plcoffee*
/usr/share/postgresql/10/extension/plls*
/usr/share/postgresql/10/extension/plv8* \  
&& chmod 755 /usr/lib/postgresql/10/lib/plv8-2.3.3.so \  
&& chmod 755 /usr/lib/postgresql/10/bin/pg_config

