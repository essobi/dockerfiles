FROM solr:5.5  
LABEL maintainer="daniel.baragan@eaudeweb.ro" \  
name="solr"  
  
USER root  
RUN apt-get update && apt-get -y --no-install-recommends install \  
vim \  
patch \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
USER solr  
RUN mkdir ecolex_initial_conf  
RUN cp -r ./server/solr/configsets/data_driven_schema_configs/conf
ecolex_initial_conf/conf  
ADD ./schema.xml \  
./solrconfig.xml.patch \  
ecolex_initial_conf/conf/  
  
ADD ./container-scripts/config-diff.sh \  
./container-scripts/entrypoint.sh \  
/opt/docker-solr/scripts/  
  
# Docker won't honor USER when COPY or ADD. Because. :-(  
USER root  
RUN chown $SOLR_UID:$SOLR_UID \  
./ecolex_initial_conf/conf/schema.xml \  
./ecolex_initial_conf/conf/solrconfig.xml.patch \  
/opt/docker-solr/scripts/config-diff.sh \  
/opt/docker-solr/scripts/entrypoint.sh \  
;  
  
USER solr  
RUN cd ecolex_initial_conf/conf/ && patch -p1 < solrconfig.xml.patch  
  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["solr-foreground"]  

