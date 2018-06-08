# Reference base image  
FROM ubuntu:16.04  
# Provide contact information  
MAINTAINER Loggly, Inc  
  
# Setup our collectd  
ADD ["files", "/tmp/"]  
  
# Add in startup scripts  
COPY ["files/scripts/*.sh", "/.docker/"]  
  
RUN echo "deb http://pkg.ci.collectd.org/deb xenial collectd-5.7" >>
/etc/apt/sources.list \  
&& gpg \--recv-keys \--keyserver pool.sks-keyservers.net 3994D24FB8543576 \  
&& gpg \--export -a 3994D24FB8543576 | apt-key add -  
  
# Install all apt-get utils and required repos  
RUN apt-get update && apt-get install -y \  
# Install collectd  
collectd \  
# Install helper packages  
git \  
jq \  
# Install pip  
python-pip \  
# Clean up existing configs  
&& rm -rf /etc/collectd \  
# Install default configs  
&& mv /tmp/collectd /etc/ \  
# Move the contrib directories in  
&& mv /tmp/contrib/rootfs_prefix /usr/src/ \  
## Build the contrib  
&& make -C /usr/src/rootfs_prefix/ \  
# Install the Docker plugin  
&& git clone \--branch v1.0.6 https://github.com/signalfx/docker-collectd-
plugin.git /usr/share/collectd/docker \  
# Install the Elasticsearch plugin  
&& git clone \--branch v1.3.2 https://github.com/signalfx/collectd-
elasticsearch.git /usr/share/collectd/elasticsearch \  
# Install the HAProxy plugin  
&& git clone \--branch v1.0.1 https://github.com/signalfx/collectd-haproxy.git
/usr/share/collectd/haproxy \  
# Install pip requirements for the docker-collectd-plugin  
&& pip install -r /usr/share/collectd/docker/requirements.txt \  
# Install the java types  
&& cp /tmp/plugins/java/jmx_types_db /usr/share/collectd/java \  
# Set correct permissions on startup scripts  
&& chmod +x /.docker/*.sh \  
# Uninstall helper packages  
&& apt-get \--purge -y remove git \  
# Clean up packages  
&& apt-get autoclean \  
&& apt-get clean \  
&& apt-get autoremove -y \  
# Remove extraneous files  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/share/man/* \  
&& rm -rf /usr/share/info/* \  
&& rm -rf /var/cache/man/* \  
# Clean up tmp directory  
&& rm -rf /tmp/*  
  
# Expose the statsd port  
EXPOSE 8125  
  
# Change work directory  
WORKDIR /.docker/  
# Execute commands when the container starts (ubuntu-run.sh)  
CMD /.docker/ubuntu-run.sh

