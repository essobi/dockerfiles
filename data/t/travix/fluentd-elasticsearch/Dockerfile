FROM gcr.io/google_containers/fluentd-elasticsearch:1.23  
MAINTAINER Travix  
  
COPY ./td-agent.conf /etc/td-agent/td-agent.conf  
  
RUN chmod 500 /etc/td-agent/td-agent.conf  
  
# runtime environment variable  
ENV ELASTICSEARCH_HOST_NAME="elasticsearch-logging" \  
LOGSTASH_PREFIX="logstash" \  
LOGSTASH_DATEFORMAT="%Y.%m.%d"  
ENTRYPOINT []  
  
CMD sed -i -e "s|host elasticsearch-logging|host ${ELASTICSEARCH_HOST_NAME}|"
/etc/td-agent/td-agent.conf \  
&& sed -i -e "s|logstash_prefix logstash|logstash_prefix ${LOGSTASH_PREFIX}|"
/etc/td-agent/td-agent.conf \  
&& sed -i -e "s|logstash_dateformat %Y.%m.%d|logstash_dateformat
${LOGSTASH_DATEFORMAT}|" /etc/td-agent/td-agent.conf \  
&& /usr/sbin/td-agent 2>&1 >> /var/log/fluentd.log

