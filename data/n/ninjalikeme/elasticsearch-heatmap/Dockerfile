FROM openjdk:8-jdk  
  
# es cant be runned by root  
RUN groupadd -g 1000 elasticsearch && useradd elasticsearch -u 1000 -g 1000  
  
RUN mkdir -p /usr/src/downloads  
WORKDIR /usr/src/downloads  
  
RUN wget "https://services.gradle.org/distributions/gradle-2.13-all.zip" \  
&& wget "https://github.com/elastic/elasticsearch/archive/v5.1.1.zip" \  
&& wget "https://github.com/boundlessgeo/elasticsearch-
heatmap/archive/5.1.1.zip" \  
&& unzip "gradle-2.13-all.zip" \  
&& unzip "v5.1.1.zip" \  
&& unzip "5.1.1.zip"  
  
WORKDIR /usr/src/downloads/elasticsearch-5.1.1  
RUN ../gradle-2.13/bin/gradle assemble  
  
RUN mkdir -p /opt/elasticsearch && \  
tar zxvf
distribution/tar/build/distributions/elasticsearch-5.1.1-SNAPSHOT.tar.gz -C
/opt/elasticsearch --strip-components=1  
  
WORKDIR /usr/src/downloads/elasticsearch-heatmap-5.1.1  
RUN ../gradle-2.13/bin/gradle assemble  
  
WORKDIR /opt/elasticsearch  
COPY config ./config  
RUN set -ex && for path in data logs config plugins config/scripts; do \  
mkdir -p "$path"; \  
chown -R elasticsearch:elasticsearch "$path"; \  
done  
  
RUN /opt/elasticsearch/bin/elasticsearch-plugin install \  
file:///usr/src/downloads/elasticsearch-
heatmap-5.1.1/build/distributions/aggs-geoheatmap-5.1.1-SNAPSHOT.zip  
  
RUN rm -rf /usr/src/downloads  
  
USER elasticsearch  
ENV PATH=$PATH:/opt/elasticsearch/bin  
CMD ["elasticsearch"]  
  
EXPOSE 9200 9300

