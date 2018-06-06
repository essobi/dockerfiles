FROM solr:latest  
  
LABEL io.openshift.non-scalable true  
  
USER root  
  
ADD nice2_index /opt/solr/server/solr/nice2_index  
ADD nice2-enterprisesearch-impl-1.0-SNAPSHOT.jar /opt/solr/server/solr/lib  
ADD tocco-solr.sh tocco-solr-config.py /usr/local/bin/  
  
RUN chgrp -R 0 /opt/solr \  
&& chmod -R g+rwX /opt/solr \  
&& chmod +x /usr/local/bin/tocco-solr.sh /usr/local/bin/tocco-solr-config.py \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y python3 \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/*  
  
ENTRYPOINT ["tocco-solr.sh"]  
CMD ["solr-foreground"]  

