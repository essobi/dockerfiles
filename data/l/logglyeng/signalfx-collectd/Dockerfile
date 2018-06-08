# Reference base image  
FROM ubuntu:16.04  
# Provide contact information  
MAINTAINER Loggly, Inc  
  
# Setup our collectd  
ADD ["files", "/tmp/"]  
  
# Add in startup scripts  
COPY ["files/scripts/*.sh", "/.docker/"]  
  
# Install all apt-get utils and required repos  
RUN apt-get update \  
&& apt-get upgrade -y \  
# Install add-apt-repository  
&& apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:signalfx/collectd-release \  
&& add-apt-repository -y ppa:signalfx/collectd-plugin-release \  
&& apt-get update \  
# Install  
&& apt-get install -y \  
# Install SignalFx Plugin  
signalfx-collectd-plugin \  
# Install collectd  
collectd \  
# Install helper packages  
jq \  
curl \  
unzip \  
git \  
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
# Install the ZooKeeper plugin  
&& git clone \--branch v0.0.3 https://github.com/signalfx/collectd-
zookeeper.git /usr/share/collectd/zookeeper \  
# Install the Elasticsearch plugin  
&& git clone \--branch v1.3.2 https://github.com/signalfx/collectd-
elasticsearch.git /usr/share/collectd/elasticsearch \  
# Install the Redis plugin  
&& git clone \--branch v1.0.0 https://github.com/signalfx/redis-collectd-
plugin.git /usr/share/collectd/redis \  
# Install the HAProxy plugin  
&& git clone \--branch v1.0.1 https://github.com/signalfx/collectd-haproxy.git
/usr/share/collectd/haproxy \  
# Install pip requirements for the docker-collectd-plugin  
&& pip install -r /usr/share/collectd/docker/requirements.txt \  
# Install the java types  
&& cp /tmp/plugins/java/signalfx_types_db /usr/share/collectd/java \  
# Set correct permissions on startup scripts  
&& chmod +x /.docker/*.sh \  
# Uninstall helper packages  
&& apt-get \--purge -y remove \  
software-properties-common \  
curl \  
unzip \  
git \  
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

