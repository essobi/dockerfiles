FROM python:2.7  
RUN \  
pip install newrelic-plugin-agent && \  
mkdir -vp /var/log/newrelic && \  
mkdir -vp /var/run/newrelic  
  
ENTRYPOINT [ "newrelic-plugin-agent", "--foreground" ]  
CMD [ "--config", "/etc/newrelic/newrelic-plugin-agent.cfg" ]  

