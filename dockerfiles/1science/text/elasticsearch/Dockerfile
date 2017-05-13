#
# Elasticsearch image
#
FROM 1science/java:oracle-jre-7
# Elasticsearch version
ENV ES_VERSION=1.6.0 ES_HOME=/usr/share/elasticsearch

# Set environment
ENV PATH=${PATH}:${ES_HOME}/bin

# Install Elasticsearch and plugins
RUN curl -Ls https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-$ES_VERSION.tar.gz | tar -xz -C /usr/share && \
    ln -s /usr/share/elasticsearch-$ES_VERSION $ES_HOME && \
    plugin -install lmenezes/elasticsearch-kopf/v1.5.4 && \
    plugin -install royrusso/elasticsearch-HQ && \
    plugin -install elasticsearch/elasticsearch-cloud-aws/2.6.0 && \
    echo -ne "- with Elasticsearch `elasticsearch -v`\n" >> /root/.built

# Define default configuration
COPY config /usr/share/elasticsearch/config

# Define a volume for indices
VOLUME /data

# Expose HTTP and transport ports
EXPOSE 9200 9300
CMD ["elasticsearch"]

