# Docker file to create Elasticsearch container.  
FROM elasticsearch:2.3.4  
# Setup environment  
ENV ES_VERSION 2.3.4  
ENV ES_PLUGIN_KOPF_VERSION 2.0  
ENV ES_HOME /opt/elasticsearch  
ENV ES_VOL /var/lib/elasticsearch  
ENV ES_USER elasticsearch  
ENV ES_GROUP elasticsearch  
  
# Install requirements and Elasticsearch  
RUN plugin install analysis-icu &&\  
plugin install lang-javascript &&\  
plugin install lang-python &&\  
plugin install cloud-azure &&\  
plugin install cloud-aws &&\  
plugin install cloud-gce &&\  
plugin install delete-by-query  
RUN plugin install lmenezes/elasticsearch-kopf/${ES_PLUGIN_KOPF_VERSION} &&\  
plugin install royrusso/elasticsearch-HQ  
RUN plugin install
http://xbib.org/repository/org/xbib/elasticsearch/plugin/elasticsearch-
knapsack/2.3.4.0/elasticsearch-knapsack-2.3.4.0-plugin.zip  
RUN plugin install
http://xbib.org/repository/org/xbib/elasticsearch/plugin/elasticsearch-plugin-
bundle/2.3.4.0/elasticsearch-plugin-bundle-2.3.4.0-plugin.zip  
RUN plugin install org.codelibs/elasticsearch-dynarank/2.3.1  
#RUN plugin install
http://xbib.org/repository/org/xbib/elasticsearch/plugin/elasticsearch-
analysis-phonetic-eudex/2.3.2.2/elasticsearch-analysis-phonetic-
eudex-2.3.2.2-plugin.zip  
RUN plugin install https://github.com/jlinn/elasticsearch-analysis-
email/releases/download/v2.3.4/elasticsearch-analysis-email-2.3.4.zip  
RUN plugin install http://dl.bintray.com/content/imotov/elasticsearch-
plugins/org/elasticsearch/elasticsearch-analysis-
morphology/2.3.4/elasticsearch-analysis-morphology-2.3.4.zip  
RUN plugin install https://github.com/jlinn/elasticsearch-analysis-
url/releases/download/v2.3.4.3/elasticsearch-analysis-url-2.3.4.3.zip  
# plugin install org.codelibs/elasticsearch-dataformat/2.1.1 &&\  
# plugin install http://dl.bintray.com/yann-barraud/elasticsearch-entity-
resolution/org/yaba/elasticsearch-entity-resolution-
plugin/2.1.1/elasticsearch-entity-resolution-plugin-2.1.1.zip &&\  
# Configure environment  
COPY src/ /  
  
# Expose volumes  
#VOLUME ["${ES_VOL}"]  
# Define working directory.  
#WORKDIR ${ES_VOL}  
# Listen for 9200/tcp (HTTP) and 9300/tcp (cluster)  
#EXPOSE 9200 9300  
#RUN chmod +x /usr/local/bin/elasticsearch.sh  
# Start container  
#ENTRYPOINT ["/usr/local/bin/elasticsearch.sh"]  
#CMD [""]  

