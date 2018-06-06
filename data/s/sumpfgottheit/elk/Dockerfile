FROM sebp/elk  
MAINTAINER Florian Sachs "florian.sachs@gmx.at"  
ENV LOGSTASH_PACKAGE logstash-2.3.0.tar.gz  
RUN rm -fr ${LOGSTASH_HOME} \  
&& mkdir ${LOGSTASH_HOME} \  
&& curl -O
https://download.elasticsearch.org/logstash/logstash/${LOGSTASH_PACKAGE} \  
&& tar xzf ${LOGSTASH_PACKAGE} -C ${LOGSTASH_HOME} \--strip-components=1 \  
&& rm -f ${LOGSTASH_PACKAGE} \  
&& chown -R logstash:logstash ${LOGSTASH_HOME} /var/log/logstash  
  
RUN /opt/logstash/bin/logstash-plugin install logstash-input-courier  
  
RUN sed -i -r 's/LS_OPTS=""/LS_OPTS=" --auto-reload "/' /etc/init.d/logstash  
  

