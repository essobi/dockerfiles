FROM dedekj/docker-pgq:9.6  
  
MAINTAINER Jan Dedek <jan.dedek@datlowe.cz>  
  
RUN apt-get update && apt-get install -y curl  
  
RUN curl -L http://postgres.cz/data/czech.tar.gz \  
| tar -xzC /tmp/ \  
&& mv /tmp/fulltext_dicts/czech.*
/usr/share/postgresql/$PG_MAJOR/tsearch_data/ \  
&& rm -rf /tmp/fulltext_dicts/  
  
ADD czech.stop /usr/share/postgresql/$PG_MAJOR/tsearch_data/  
ADD dict_snowball.so /usr/lib/postgresql/$PG_MAJOR/lib/  
  
ADD add-tsearch-czech.sh docker-entrypoint-initdb.d/  
  
  
#RUM  
ADD RUM/lib/ /usr/lib/postgresql/$PG_MAJOR/lib/  
  
ADD RUM/extension/ /usr/share/postgresql/$PG_MAJOR/extension  

