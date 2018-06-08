FROM ubuntu:trusty  
  
MAINTAINER Ozzy Johnson <oswald.johnson@gsa.gov>  
  
RUN \  
apt-get update \  
-qq \  
&& apt-get install \  
-qq \  
\--yes \  
\--no-install-recommends \  
\--no-install-suggests \  
curl \  
python-software-properties \  
software-properties-common \  
  
# Clean up packages.  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Borrow gosu setup code from the docker-library Elasticsearch image found
here:  
# https://github.com/docker-library/elasticsearch/blob/master/1.5/Dockerfile  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# Add Java.  
RUN \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update \  
-qq \  
&& apt-get install \  
-qq \  
-y oracle-java7-installer=7u80+7u60arm-0~webupd8~1 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/oracle-jdk7-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
# Install Elasticsearch.  
ENV ES_PKG_NAME elasticsearch-1.7.1  
RUN \  
cd / \  
&& wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/${ES_PKG_NAME}.tar.gz
\  
\--no-verbose \  
&& tar xvzf $ES_PKG_NAME.tar.gz \  
&& rm -f $ES_PKG_NAME.tar.gz \  
&& mv /$ES_PKG_NAME /elasticsearch  
  
# Set up default config.  
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
# Add custom scripts.  
ADD config/scripts /elasticsearch/config  
  
# http-basic plugin.  
ENV HB_VERSION=1.5.0  
ENV HTTP_BASIC_URL https://github.com/Asquera/elasticsearch-http-
basic/releases/download/v${HB_VERSION}/elasticsearch-http-
basic-${HB_VERSION}.jar  
RUN /elasticsearch/bin/plugin \  
\--url $HTTP_BASIC_URL \  
\--install http-basic \  
\--silent  
  
# mapper-attachments plugin.  
ENV MA_VERSION=2.7.0  
RUN /elasticsearch/bin/plugin \  
install elasticsearch/elasticsearch-mapper-attachments/${MA_VERSION} \  
\--silent  
  
# elasticsearch-cloud-aws plugin.  
ENV CA_VERSION=2.7.0  
RUN /elasticsearch/bin/plugin install \  
elasticsearch/elasticsearch-cloud-aws/${CA_VERSION} \  
\--silent  
  
# Set up prep script location.  
ADD scripts /scripts  
RUN chmod +x /scripts/*.sh \  
&& touch /.firstrun  
  
# Create the Elasticsearch user.  
RUN groupadd -r elasticsearch \  
&& useradd -r -g elasticsearch elasticsearch  
  
# Use a reasonable heap size.  
# https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html  
ENV ES_HEAP_SIZE=4g  
  
# Mount for persistent data.  
VOLUME ["/data"]  
  
# Expose Elasticsearch ports.  
EXPOSE 9200 9300  
# Entry commands.  
ENTRYPOINT ["/bin/bash", "/scripts/start.sh"]  
CMD [""]  

