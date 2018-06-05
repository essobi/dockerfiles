FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y \  
openjdk-7-jre-headless \  
curl \  
jq \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
# If we wanted the development version we could pull that instead but we want
to  
# run a production environment here.  
RUN export ES_PKG=elasticsearch-2.2.0.deb && \  
curl -LO
https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/2.2.0/${ES_PKG}
&& \  
dpkg -i ${ES_PKG} && \  
rm ${ES_PKG} && \  
rm /etc/elasticsearch/elasticsearch.yml  
  
# Add Containerpilot and set its configuration  
ENV CONTAINERPILOT_VER 2.7.3  
ENV CONTAINERPILOT file:///etc/containerpilot.json  
  
RUN export CONTAINERPILOT_CHECKSUM=2511fdfed9c6826481a9048e8d34158e1d7728bf \  
&& curl -Lso /tmp/containerpilot.tar.gz \  
"https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VER}/containerpilot-${CONTAINERPILOT_VER}.tar.gz"
\  
&& echo "${CONTAINERPILOT_CHECKSUM} /tmp/containerpilot.tar.gz" | sha1sum -c \  
&& tar zxf /tmp/containerpilot.tar.gz -C /usr/local/bin \  
&& rm /tmp/containerpilot.tar.gz  
  
RUN curl --fail -sL
https://github.com/justwatchcom/elasticsearch_exporter/releases/download/0.3.0/elasticsearch_exporter-0.3.0.linux-
amd64.tar.gz \  
| tar -C /usr/local/bin -xzf -  
  
# Create and take ownership over required directories  
RUN mkdir -p /var/lib/elasticsearch/data && \  
chown -R elasticsearch:elasticsearch /var/lib/elasticsearch/data && \  
chown -R root:elasticsearch /etc/elasticsearch && \  
chmod g+w /etc/elasticsearch  
  
USER elasticsearch  
  
# Add our configuration files and scripts  
COPY /etc/containerpilot.json /etc  
COPY /etc/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  
COPY /bin/manage.sh /usr/local/bin  
COPY /bin/metrics.sh /usr/local/bin  
  
# Expose the data directory as a volume in case we want to mount these  
# as a --volumes-from target; it's important that this VOLUME comes  
# after the creation of the directory so that we preserve ownership.  
VOLUME /var/lib/elasticsearch/data  
  
# We don't need to expose these ports in order for other containers on Triton  
# to reach this container in the default networking environment, but if we  
# leave this here then we get the ports as well-known environment variables  
# for purposes of linking.  
EXPOSE 9200  
EXPOSE 9300  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license="MPL-2.0" \  
org.label-schema.name="Autopilot Pattern Elasticsearc with Prometheus Metrics"
\  
org.label-schema.url="https://github.com/double16/autopilotpattern-
elasticsearch" \  
org.label-schema.docker.dockerfile="Dockerfile" \  
org.label-schema.vcs-ref=$SOURCE_REF \  
org.label-schema.vcs-type='git' \  
org.label-schema.vcs-url="https://github.com/double16/autopilotpattern-
elasticsearch.git"  
  

