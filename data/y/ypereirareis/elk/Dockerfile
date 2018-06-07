FROM sebp/elk  
  
MAINTAINER Yannick PEREIRA-REIS http://ypereirareis.github.io  
  
###############################################################################  
# CONFIGURATION  
###############################################################################  
  
# Override Logstash  
# ----------------------------------------------------------------------------  
ENV LOGSTASH_HOME /opt/logstash  
  
ADD ./init/logstash-init /etc/init.d/logstash  
RUN sed -i -e 's#^LS_HOME=$#LS_HOME='$LOGSTASH_HOME'#' /etc/init.d/logstash \  
&& chmod +x /etc/init.d/logstash  
  
  
# Override Kibana  
# ----------------------------------------------------------------------------  
ENV KIBANA_HOME /opt/kibana  
  
ADD ./init/kibana-init /etc/init.d/kibana  
RUN sed -i -e 's#^KIBANA_HOME=$#KIBANA_HOME='$KIBANA_HOME'#'
/etc/init.d/kibana \  
&& chmod +x /etc/init.d/kibana  
  
  
# Override Elasticsearch conf  
# ----------------------------------------------------------------------------  
ADD ./conf/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  
  
  
# Logstash - Cert/key  
# ----------------------------------------------------------------------------  
RUN if [ ! -d "/etc/pki/tls/certs" ]; then mkdir -p /etc/pki/tls/certs &&
mkdir /etc/pki/tls/private;fi  
ADD ./ssl/logstash-forwarder.crt /etc/pki/tls/certs/logstash-forwarder.crt  
ADD ./ssl/logstash-forwarder.key /etc/pki/tls/private/logstash-forwarder.key  
  
  
# Logstash - Filters  
# ----------------------------------------------------------------------------  
ADD ./filters/01-lumberjack-input.conf /etc/logstash/conf.d/01-lumberjack-
input.conf  
ADD ./filters/10-syslog.conf /etc/logstash/conf.d/10-syslog.conf  
ADD ./filters/11-nginx.conf /etc/logstash/conf.d/11-nginx.conf  
ADD ./filters/12-apache.conf /etc/logstash/conf.d/12-apache.conf  
ADD ./filters/13-mysql-slow.conf /etc/logstash/conf.d/13-mysql-slow.conf  
ADD ./filters/15-symfony.conf /etc/logstash/conf.d/15-symfony.conf  
ADD ./filters/30-lumberjack-output.conf /etc/logstash/conf.d/30-lumberjack-
output.conf  
  
  
# Logstash - Patterns  
# ----------------------------------------------------------------------------  
ADD ./patterns/nginx.pattern ${LOGSTASH_HOME}/patterns/nginx  
ADD ./patterns/apache.pattern ${LOGSTASH_HOME}/patterns/apache  
ADD ./patterns/symfony.pattern ${LOGSTASH_HOME}/patterns/symfony  
ADD ./patterns/mysql-slow.pattern ${LOGSTASH_HOME}/patterns/mysql-slow  
RUN chown -R logstash:logstash ${LOGSTASH_HOME}/patterns  
  
###############################################################################  
# START  
###############################################################################  
  
EXPOSE 5601 9200 9300 5000  
VOLUME /var/lib/elasticsearch  
  
CMD [ "/usr/local/bin/start.sh" ]

