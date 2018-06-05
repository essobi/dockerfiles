FROM mongo  
  
RUN mkdir -p /data/archive  
COPY archive/amelieoss.gz /data/archive/amelieoss.gz  
COPY archive/docclassifier.gz /data/archive/docclassifier.gz  
COPY archive/syncpipes.gz /data/archive/syncpipes.gz  
  
CMD mongorestore \--host mongo \--port 27017 \--drop \--gzip
\--archive=/data/archive/amelieoss.gz \--db amelie_oss; mongorestore \--host
mongo \--port 27017 \--drop \--gzip \--archive=/data/archive/docclassifier.gz
\--db docclassifier; mongorestore \--host mongo \--port 27017 \--drop \--gzip
\--archive=/data/archive/syncpipes.gz \--db syncpipes;

