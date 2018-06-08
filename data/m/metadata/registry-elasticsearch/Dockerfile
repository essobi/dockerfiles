FROM elasticsearch:2.3.5  
MAINTAINER Vladimir Orany <vladimir@orany.cz>  
  
LABEL Description="This image is used to setup search server for Metadata
Registry inside Docker" Vendor="Metadata Consulting Ltd." Version="2.0"  
  
ENV KOPF_VERSION v2.1.2  
RUN set -x \  
&& ./bin/plugin install "lmenezes/elasticsearch-kopf/$KOPF_VERSION" \  
&& ./bin/plugin install "cloud-aws"  
  
EXPOSE 9300 9200  
CMD ["elasticsearch", "-Des.network.host=0.0.0.0",
"-Des.threadpool.bulk.queue_size=100000",
"-Des.action.auto_create_index=false", "-Des.index.mapper.dynamic=false"]  

