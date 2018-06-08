FROM phusion/baseimage:0.9.16  
MAINTAINER Ted Chen <ted@nephilagraphic.com>  
  
# Set correct environment variables.  
ENV HOME /root  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Install wget and install/updates certificates  
RUN apt-get update \  
&& apt-get install -y wget curl libcurl4-openssl-dev make \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Fluentd.  
RUN /usr/bin/curl -L http://toolbelt.treasuredata.com/sh/install-ubuntu-
trusty-td-agent2.sh | sh \  
&& /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-logentries -v
0.2.4 \  
&& /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-record-reformer
-v 0.4.0 \  
&& /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-jsonbucket -v
0.0.2  
  
ENV DOCKER_GEN_VERSION 0.3.6  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
COPY . /app/  
WORKDIR /app/  
  
COPY init_config.sh /etc/my_init.d/init_config.sh  
COPY run.dockergen.sh /etc/service/dockergen/run  
COPY run.td-agent.sh /etc/service/td-agent/run  
  
RUN chmod 750 /etc/my_init.d/init_config.sh \  
&& chmod 750 /etc/service/dockergen/run \  
&& chmod 750 /etc/service/td-agent/run  
  
# Listen socket to docker events  
ENV DOCKER_HOST unix:///tmp/docker.sock  

