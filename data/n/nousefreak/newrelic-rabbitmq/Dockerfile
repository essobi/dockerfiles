FROM python:2.7  
MAINTAINER Dries De Peuter <dries@depeuter.io>  
  
RUN pip install newrelic-plugin-agent  
  
RUN mkdir -p /var/log/newrelic  
RUN mkdir -p /var/run/newrelic  
RUN mkdir -p /etc/newrelic/  
  
WORKDIR /etc/newrelic  
COPY newrelic-plugin-agent.cfg /etc/newrelic/  
COPY start.sh ./start.sh  
  
ENTRYPOINT ["./start.sh"]  
CMD ["newrelic-rabbitmq"]  

