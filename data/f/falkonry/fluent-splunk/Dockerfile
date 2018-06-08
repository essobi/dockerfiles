# This Dockerfile will build an image that is configured  
# to run Fluentd with a Splunk plug-in and the  
# provided configuration file.  
# TODO: Use a lighter base image, e.g. some form of busybox.  
# The image acts as an executable for the binary /usr/sbin/td-agent.  
# Note that fluentd is run with root permssion to allow access to  
# log files with root only access under /var/log/containers/*  
# Please see http://docs.fluentd.org/articles/install-by-deb for more  
# information about installing fluentd using deb package.  
FROM ubuntu:14.04  
# Ensure there are enough file descriptors for running Fluentd.  
RUN ulimit -n 65536  
  
# Disable prompts from apt.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install prerequisites.  
RUN apt-get update && \  
apt-get install -y -q curl make g++ && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Fluentd.  
RUN /usr/bin/curl -L https://td-toolbelt.herokuapp.com/sh/install-ubuntu-
trusty-td-agent2.sh | sh  
  
# Change the default user and group to root.  
# Needed to allow access to /var/log/docker/... files.  
RUN sed -i -e "s/USER=td-agent/USER=root/" -e "s/GROUP=td-agent/GROUP=root/"
/etc/init.d/td-agent  
  
# Install the Kubernetes and Splunk Fluentd plug-ins.  
# Note: net-http-persistent library is required by splunk plugin, but not
automatically installed  
RUN td-agent-gem install fluent-plugin-kubernetes_metadata_filter net-http-
persistent fluent-plugin-splunkapi  
  
# Copy the Fluentd configuration file.  
COPY td-agent.conf /etc/td-agent/td-agent.conf  
  
# Environment variables for configuration  
# FLUENTD_ARGS cannot be empty, so a placeholder is used. It should not have
any effect because it is a default.  
ENV SPLUNK_SERVER localhost:8089  
ENV SPLUNK_AUTH admin:changme  
ENV SPLUNK_INDEX main  
ENV FLUENTD_ARGS --use-v1-config  
ENV KUBE_VERIFY_SSL true  
  
# Run the Fluentd service.  
ENTRYPOINT "exec" "td-agent" "$FLUENTD_ARGS"  

