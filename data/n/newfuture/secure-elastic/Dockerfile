FROM elasticsearch:5.2.0  
  
LABEL Description="elasticsearch search-guard"  
# env  
ENV CLUSTER_NAME="elasticsearch" \  
HOSTS="[127.0.0.1]" \  
MINIMUM_MASTER_NODES=1 \  
ELASTIC_PWD="changeme" \  
HEAP_SIZE="1g" \  
CA_PWD="changeme" \  
TS_PWD="changeme" \  
KS_PWD="changeme"  
# install modules  
RUN bin/elasticsearch-plugin install -b com.floragunn:search-guard-5:5.2.0-10  
  
# retrieve conf  
COPY *.jar /usr/share/elasticsearch/plugins/search-guard-5/  
COPY ./elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
COPY ./searchguard/ /usr/share/elasticsearch/config/searchguard/  
COPY ./src/ /run/  
RUN chmod +x -R /run/  
  
RUN mkdir -p /.backup/elasticsearch/ \  
&& mv /usr/share/elasticsearch/config /.backup/elasticsearch/config  
  
  
VOLUME /usr/share/elasticsearch/config  
VOLUME /usr/share/elasticsearch/dara  
  
ENTRYPOINT ["/run/entrypoint.sh"]  
CMD ["elasticsearch"]

