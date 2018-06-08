FROM elasticsearch:1.5  
ENV ANALYSIS_PHONETIC_VERSION 2.5.0  
ENV LICENCE_VERSION 1.0.0  
ENV SHIELD_VERSION 1.3.1  
ENV ES_JAVA_OPTS "-Des.path.conf=/etc/elasticsearch
-Des.default.path.logs=/var/log/elasticsearch/"  
RUN plugin -install mobz/elasticsearch-head  
  
COPY elasticsearch-analysis-phonetic-${ANALYSIS_PHONETIC_VERSION}.zip /tmp/  
RUN plugin --install analysis-phonetic --url file:/tmp/elasticsearch-analysis-
phonetic-${ANALYSIS_PHONETIC_VERSION}.zip && rm /tmp/elasticsearch-analysis-
phonetic-${ANALYSIS_PHONETIC_VERSION}.zip  
  
COPY license-${LICENCE_VERSION}.zip /tmp/  
RUN plugin --install license --url file:/tmp/license-${LICENCE_VERSION}.zip &&
rm /tmp/license-${LICENCE_VERSION}.zip  
  
COPY shield-${SHIELD_VERSION}.zip /tmp/  
RUN plugin --install shield --url file:/tmp/shield-${SHIELD_VERSION}.zip && rm
/tmp/shield-${SHIELD_VERSION}.zip  
RUN chmod +x /usr/share/elasticsearch/bin/shield/*  
  
VOLUME /var/log/elasticsearch  
RUN chown elasticsearch:elasticsearch /var/log/elasticsearch  
  
ENV PATH /usr/share/elasticsearch/bin/shield:$PATH  
RUN esusers useradd es_admin -r admin -p es_admin  
  
COPY docker-entrypoint.sh /  
  
RUN echo "shield.audit.enabled: true" >> /etc/elasticsearch/elasticsearch.yml  

