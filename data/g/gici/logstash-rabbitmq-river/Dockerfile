FROM logstash:2  
MAINTAINER Michael Gelfand <michael@senexx.com>  
  
# Install supervisor, curl, jq, supervisor_stdout  
RUN apt-get update && \  
apt-get install -y supervisor curl jq python-pip && \  
pip install supervisor-stdout && \  
rm -rf /var/lib/apt/lists/*  
  
# Instal custom elasticsearch output - till pull request is merged:
https://github.com/logstash-plugins/logstash-output-elasticsearch/pull/463  
RUN PLUGIN=logstash-output-elasticsearch && \  
BRANCH=2.7.1-update_action-new && \  
cd /tmp && \  
wget https://github.com/sxmichael/$PLUGIN/archive/$BRANCH.zip && \  
unzip $BRANCH.zip && \  
cd $PLUGIN-$BRANCH && \  
/opt/logstash/vendor/jruby/bin/jruby -S gem build $PLUGIN.gemspec && \  
/opt/logstash/bin/plugin install /tmp/$PLUGIN-$BRANCH/$PLUGIN-*.gem && \  
cd / && \  
rm -rf /tmp/$BRANCH.zip /tmp/$PLUGIN-$BRANCH  
  
ENV RIVER_INDEX river  
ENV LOGSTASH_CONF /etc/logstash/conf.d/13-rabbitmq-input.conf  
ENV LOGSTASH_ES_OUTPUT_CONF /etc/logstash/conf.d/30-elasticsearch_bulk-
output.conf  
ENV ES_EXTRA_HOSTS ""  
COPY logstash-conf.d/30-elasticsearch_bulk-output.conf
/etc/logstash/conf.d/30-elasticsearch_bulk-output.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY bin/* /usr/local/bin/  
  
CMD ["/usr/local/bin/bootstrap.sh"]  

