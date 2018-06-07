FROM ccfoss/alpine-consul  
  
MAINTAINER Chaitanya Akkineni cakkinen@cisco.com  
  
# Install java and tini  
RUN apk add --update bash curl openjdk8-jre tini gosu@testing wget ca-
certificates && \  
rm -rf /var/cache/apk/*  
  
ENV ELASTIC 5.0.1  
RUN cd /tmp \  
&& wget -O elasticsearch-$ELASTIC.tar.gz
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-$ELASTIC.tar.gz
\  
&& tar -xzf elasticsearch-$ELASTIC.tar.gz \  
&& mv elasticsearch-$ELASTIC /usr/share/elasticsearch \  
&& adduser -DH -s /sbin/nologin elasticsearch \  
&& echo "Creating Elasticsearch Paths..." \  
&& for path in \  
/var/elasticsearch/data \  
/var/log/elasticsearch \  
/etc/elasticsearch/plugins \  
/etc/logrotate.d/elasticsearch \  
; do \  
mkdir -p "$path"; \  
done \  
&& chown -R elasticsearch:elasticsearch /usr/share/elasticsearch \  
&& chown -R elasticsearch:elasticsearch /var/log/elasticsearch \  
&& chown -R elasticsearch:elasticsearch /var/elasticsearch \  
&& rm -rf /tmp/*  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
#ENV ES_HOME /etc/elasticsearch  
WORKDIR /usr/share/elasticsearch  
  
# Install X-Pack plugin  
RUN elasticsearch-plugin install -b x-pack  
RUN elasticsearch-plugin install io.fabric8:elasticsearch-cloud-
kubernetes:5.0.1 --verbose  
  
RUN set \-- gosu elasticsearch /sbin/tini -- elasticsearch  
  
COPY elasticsearch.yml.ctmpl /usr/share/elasticsearch/config/  
COPY log4j2.properties /usr/share/elasticsearch/config/  
COPY consul-template.hcl /etc/consul.d/  
COPY logrotate /etc/logrotate.d/elasticsearch  
COPY run.sh /  
COPY es.service.json.ctmpl /tmp  
  
VOLUME ["/var/elasticsearch"]  
  
EXPOSE 9200 9300  
ENV NAMESPACE default  
ENV DISCOVERY_SERVICE elasticsearch-discovery  
  
CMD ["/run.sh"]

