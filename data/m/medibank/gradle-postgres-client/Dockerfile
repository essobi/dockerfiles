FROM niaquinto/gradle:2.13  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >>
/etc/apt/sources.list.d/pgdg.list \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add \- \  
&& apt-get update \  
&& apt-get install -y postgresql-client  
  
WORKDIR /app  

