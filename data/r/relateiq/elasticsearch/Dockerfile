FROM ingenieux/alpine-java8-supervisord:jdk-8u60-b27  
  
# elasticsearch  
RUN apk add --update wget  
  
RUN mkdir /data /logs /elasticsearch  
  
RUN wget --progress=dot:mega -O -
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.7.5.tar.gz
| tar -zx -C /elasticsearch --strip-components=1  
  
RUN echo "script.disable_dynamic: false" >>
/elasticsearch/config/elasticsearch.yml  
  
RUN /elasticsearch/bin/plugin -install mobz/elasticsearch-head  
RUN /elasticsearch/bin/plugin -install lukas-vlcek/bigdesk/2.5.0  
RUN /elasticsearch/bin/plugin -install elasticsearch/elasticsearch-mapper-
attachments/2.7.1  
#TODO check back the site when it's back available, for now build locally and
use our public readonly s3 bucket  
#RUN /elasticsearch/bin/plugin -install analysis-naturalsort -url
http://xbib.org/repository/org/xbib/elasticsearch/plugin/elasticsearch-
analysis-naturalsort/1.7.0.0/elasticsearch-analysis-
naturalsort-1.7.0.0-plugin.zip  
RUN /elasticsearch/bin/plugin -install analysis-naturalsort -url
https://s3-us-west-1.amazonaws.com/relateiq-build-resources/elasticsearch-
analysis-naturalsort-1.7.0.0-RIQ-plugin.zip  
RUN /elasticsearch/bin/plugin -install lmenezes/elasticsearch-kopf  
RUN /elasticsearch/bin/plugin -install polyfractal/elasticsearch-inquisitor  
RUN /elasticsearch/bin/plugin -install karmi/elasticsearch-paramedic  
RUN /elasticsearch/bin/plugin -install royrusso/elasticsearch-HQ  
  
VOLUME [ "/logs", "/data" ]  
  
EXPOSE 9200 9300  
ENV EXPOSED_HOST=127.0.0.1  
CMD ["/elasticsearch/bin/elasticsearch", "-f", "-D", "es.path.logs=/logs",
"-D", "es.path.data=/data", "-D", "es.network.publish_host=${EXPOSED_HOST}",
"-D", "es.cluster.name=search-localhost" ]  

