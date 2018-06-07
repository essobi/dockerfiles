FROM logstash:2.3  
# Make .m2 accessible to logstash user, otherwise logstash won't start  
RUN mkdir -p /var/lib/logstash/.m2  
RUN ln -s /var/lib/logstash/.m2 /root/.m2  
  
ENV PATH /opt/logstash/vendor/jruby/bin/:$PATH  
RUN gem install logstash-input-dynamodb:'> 2' logstash-filter-dynamodb:'> 2'  
RUN plugin install logstash-input-dynamodb logstash-filter-dynamodb  
  
ENV ELASTICSEARCH_VERSION 2.3.5  
ENV ELASTICSEARCH_REPO_BASE
http://packages.elasticsearch.org/elasticsearch/2.x/debian  
ENV AWS_DEFAULT_REGION=ap-northeast-1 AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY= AWS_SENSORS_STREAM_VIEW_TYPE=new_and_old_images
AWS_SENSORS_TABLE_NAME=citus-iot-ecosystem.sensors
ELASTICSEARCH_INDEX=telemetry ELASTICSEARCH_TYPE=sensors  
  
RUN echo "deb $ELASTICSEARCH_REPO_BASE stable main" >
/etc/apt/sources.list.d/elasticsearch.list  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends
elasticsearch=$ELASTICSEARCH_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
  
WORKDIR /usr/share/elasticsearch  
  
COPY config ./config  
COPY logstash/dynamodb-stream-logstash.json /etc/logstash/  
COPY docker-entrypoint.sh /usr/sbin/  
  
RUN chmod +x /usr/sbin/docker-entrypoint.sh  
  
VOLUME /usr/share/elasticsearch/data  
VOLUME /opt/logstash/conf  
  
RUN set -ex \  
&& for path in \  
./data \  
./logs \  
./config \  
./config/scripts \  
; do \  
mkdir -p "$path"; \  
chown -R elasticsearch:elasticsearch "$path"; \  
done  
  
RUN /usr/share/elasticsearch/bin/plugin install delete-by-query  
  
# Add s6-overlay  
ENV S6_OVERLAY_VERSION=v1.17.2.0  
RUN curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz | tar xfz - -C /  
  
ADD s6-overlay /  
  
EXPOSE 9200 9300  
ENTRYPOINT ["/usr/sbin/docker-entrypoint.sh"]  
CMD ["elasticsearch"]

