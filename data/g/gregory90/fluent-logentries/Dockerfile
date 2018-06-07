FROM ubuntu:14.04  
RUN ulimit -n 65536  
  
# Install prerequisites.  
RUN apt-get update && \  
apt-get install -y curl && \  
apt-get install -y -q libcurl4-openssl-dev make && \  
apt-get clean  
  
# Install Fluentd.  
RUN /usr/bin/curl -L http://toolbelt.treasuredata.com/sh/install-ubuntu-
trusty-td-agent2.sh | sh  
  
# Change the default user and group to root.  
# Needed to allow access to /var/log/docker/... files.  
RUN sed -i -e "s/USER=td-agent/USER=root/" -e "s/GROUP=td-agent/GROUP=root/"
/etc/init.d/td-agent  
  
COPY td-agent.conf /etc/td-agent/td-agent.conf  
COPY out_logentries.rb /etc/td-agent/plugin/out_logentries.rb  
  
# Copy a script that determines the name of the host machine  
# and then patch the Fluentd configuration files and then  
# run Fluentd in the foreground.  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
# Always run the this setup script.  
ENTRYPOINT ["/run.sh"]  

