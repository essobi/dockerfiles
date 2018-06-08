# Reference base image  
FROM alpine:3.4  
  
MAINTAINER Loggly, Inc  
  
# Specify Versions  
ARG COLLECTD_STAGE=release  
ARG PLUGIN_STAGE=release  
ARG ALPINE_VERSION=3.4  
  
# Set repository urls  
ARG
COLLECTD_ADDR=https://dl.signalfx.com/apks/collectd/alpine/${ALPINE_VERSION}/${COLLECTD_STAGE}/collectd.tar.gz  
ARG PLUGIN_ADDR=https://dl.signalfx.com/apks/signalfx-collectd-
plugin/alpine/${ALPINE_VERSION}/${PLUGIN_STAGE}/signalfx-collectd-
plugin.tar.gz  
  
# Setup our collectd  
COPY ["files", "/tmp/"]  
  
# Add in startup scripts  
COPY ["files/scripts/*.sh", "/run/"]  
  
# Add public repository key  
COPY ["files/keys/support+apk@signalfx.com-57fbc71c.rsa.pub", "/etc/apk/keys"]  
  
# Install all apt-get utils  
RUN apk update \  
&& apk upgrade \  
&& apk add py-pip \  
jq  
  
  
# Fetch all collectd repos  
RUN apk add curl \  
&& mkdir -p /repo \  
&& cd /repo \  
# Curl down and unarchive the collectd repo  
&& curl -LOk ${COLLECTD_ADDR} \  
&& tar -xvzf /repo/collectd.tar.gz \  
&& rm /repo/collectd.tar.gz \  
&& ls -la /repo/collectd/x86_64 \  
&& echo /repo/collectd >> /etc/apk/repositories \  
# Curl down and unarchive the signalfx-plugin repo  
&& curl -LOk ${PLUGIN_ADDR} \  
&& tar -xvzf /repo/signalfx-collectd-plugin.tar.gz \  
&& rm /repo/signalfx-collectd-plugin.tar.gz \  
&& ls -la /repo/signalfx-collectd-plugin/x86_64 \  
&& echo /repo/signalfx-collectd-plugin >> /etc/apk/repositories \  
# Update apk repository data  
&& apk update \  
# Install collectd  
&& apk search -v -d 'collectd' \  
&& apk add --update collectd \  
collectd-java \  
collectd-mysql \  
collectd-python \  
collectd-write_http \  
&& apk del curl  
  
# Fetch all plugins and configure  
# Clean up existing configs  
RUN apk add git alpine-sdk \  
&& rm -rf /etc/collectd \  
# Install default configs  
&& mv /tmp/collectd /etc/ \  
# Move the contrib directories in  
&& mkdir -p /usr/src \  
&& mv /tmp/contrib/rootfs_prefix /usr/src/ \  
## Build the contrib  
&& make CFLAGS=-DALPINE -C /usr/src/rootfs_prefix/ \  
# Install the Docker plugin  
&& git clone --branch v1.0.6 https://github.com/signalfx/docker-collectd-
plugin.git /usr/share/collectd/docker \  
# Install the Elasticsearch plugin  
&& git clone --branch v1.3.2 https://github.com/signalfx/collectd-
elasticsearch.git /usr/share/collectd/elasticsearch \  
# Install the HAProxy plugin  
&& git clone --branch v1.0.1 https://github.com/signalfx/collectd-haproxy.git
/usr/share/collectd/haproxy \  
# Install pip requirements for the docker-collectd-plugin  
&& pip install -r /usr/share/collectd/docker/requirements.txt \  
# Install the java types  
&& cp /tmp/plugins/java/jmx_types_db /usr/share/collectd/java \  
# Set correct permissions on startup scripts  
&& chmod +x /run/*.sh \  
# Clean up tmp directory  
&& rm -rf /tmp/* \  
&& apk del git alpine-sdk  
  
# Expose the statsd port  
EXPOSE 8125  
  
# Change work directory  
WORKDIR /run/  
  
# Execute the script run.sh in the shell  
CMD /run/alpine-run.sh

