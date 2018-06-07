FROM python:2.7  
MAINTAINER Peter Salanki <peter@salanki.st>  
  
RUN pip install newrelic-plugin-agent  
RUN pip install newrelic-plugin-agent[postgresql]  
  
RUN mkdir -p /var/log/newrelic  
RUN mkdir -p /var/run/newrelic  
RUN mkdir -p /etc/newrelic/  
  
COPY newrelic-plugin-agent.tmpl /etc/newrelic/  
  
COPY init.sh /usr/bin/  
RUN chmod +x /usr/bin/init.sh  
  
ENTRYPOINT ["/usr/bin/init.sh"]  
  
CMD ["newrelic-plugin-agent", "-c", "/etc/newrelic/newrelic-plugin-agent.cfg",
"-f"]  

