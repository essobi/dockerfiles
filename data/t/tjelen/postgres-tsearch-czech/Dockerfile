FROM postgres:9.4  
MAINTAINER Tomas Jelen <tomas@delikates.org>  
  
RUN apt-get update && apt-get install -y curl  
  
RUN curl http://postgres.cz/data/czech.tar.gz \  
| tar -xzC /tmp/ \  
&& mv /tmp/fulltext_dicts/czech.* /usr/share/postgresql/9.4/tsearch_data/  
  
ADD add-tsearch-czech.sh docker-entrypoint-initdb.d/  

