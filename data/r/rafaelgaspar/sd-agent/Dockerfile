FROM debian:jessie  
  
MAINTAINER ServerDensity <hello@serverdensity.com>  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y apt-transport-
https ca-certificates curl  
  
# Install the Agent and sd-agent-docker  
RUN echo "deb https://archive.serverdensity.com/ubuntu/ all main" >
/etc/apt/sources.list.d/sd-agent.list \  
&& curl -Ls https://archive.serverdensity.com/sd-packaging-public.key | apt-
key add - \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y sd-agent sd-agent-docker \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure the Agent  
RUN sed -i -e"s/^.*log_to_syslog:.*$/log_to_syslog: no/" /etc/sd-
agent/config.cfg \  
&& sed -i -e"s/^.*plugin_directory:.*$/plugin_directory: \/plugins/" /etc/sd-
agent/config.cfg \  
&& sed -i "/user=sd-agent/d" /etc/sd-agent/supervisor.conf \  
&& sed -i 's/AGENTUSER="sd-agent"/AGENTUSER="root"/g' /etc/init.d/sd-agent \  
&& chmod +x /etc/init.d/sd-agent  
  
# Configure Docker check  
RUN mv /etc/sd-agent/conf.d/docker_daemon.yaml.example /etc/sd-
agent/conf.d/docker_daemon.yaml \  
&& sed -i 's/#docker_root: \//docker_root: \/host/g' /etc/sd-
agent/conf.d/docker_daemon.yaml \  
&& service sd-agent restart  
  
COPY entrypoint.sh /entrypoint.sh  
  
# Extra conf.d and checks.d  
VOLUME ["/conf.d", "/checks.d", "/plugins"]  
  
# Expose supervisord port  
EXPOSE 9001/tcp  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["supervisord", "-n", "-c", "/etc/sd-agent/supervisor.conf"]  

