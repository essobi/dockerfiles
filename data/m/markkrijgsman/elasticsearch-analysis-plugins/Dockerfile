FROM docker.elastic.co/elasticsearch/elasticsearch:6.1.3  
MAINTAINER mark.krijgsman@luminis.eu  
  
COPY healthcheck.sh /usr/local/bin/  
  
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu &&
\  
/usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-smartcn &&
\  
/usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-kuromoji &&
\  
/usr/share/elasticsearch/bin/elasticsearch-plugin install
https://s3.amazonaws.com/uploads.hipchat.com/139893/5052483/FZt21x5BAENNsXP/arirang-
analyzer-es-plugin-6.1.3.zip  
  
HEALTHCHECK CMD ["healthcheck.sh"]

