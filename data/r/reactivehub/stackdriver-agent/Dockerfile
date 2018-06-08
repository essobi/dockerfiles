FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV STACKDRIVER_AGENT_VERSION 5.5.0-228  
ENV STACKDRIVER_AGENT_DEBIAN_VERSION 5.5.0-228.jessie  
  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -qq --no-install-recommends curl ca-certificates \  
&& curl -sSL -o /etc/apt/sources.list.d/stackdriver.list
"https://repo.stackdriver.com/jessie.list" \  
&& ( curl -sSL https://app.stackdriver.com/RPM-GPG-KEY-stackdriver | apt-key
add - ) \  
&& apt-get update -qq \  
&& apt-get install -qq --no-install-recommends stackdriver-
agent=${STACKDRIVER_AGENT_DEBIAN_VERSION} \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD collectd.conf /opt/stackdriver/collectd/etc/collectd.conf  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["stackdriver-agent"]  

