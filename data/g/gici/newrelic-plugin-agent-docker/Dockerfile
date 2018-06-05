FROM gici/python  
MAINTAINER Oded Lazar <odedlaz@gmail.com>  
  
# needed packages  
RUN apt-get update && apt-get install -y -qq supervisor libpq-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# newrelic-plugin-agent requirements  
RUN pip install psycopg2==2.6.2 \  
newrelic-plugin-agent==1.3.0 \  
docker-py==1.10.4 \  
fuzzywuzzy==0.12.0 \  
python-Levenshtein==0.12.0  
  
# supervisor  
RUN mkdir -p /etc/supervisor/conf.d/ && \  
mkdir -p /var/log/supervisor/  
  
ADD supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
ADD supervisor/supervisord-*.conf /etc/supervisor/conf.d/  
  
# newrelic-plugin-agent  
ADD newrelic-plugin-agent-discover.sh run.py /etc/newrelic/  
ADD config/newrelic-plugin-agent.cfg config/make.py /etc/newrelic/config/  
  
# add default configurations  
ADD defaults /etc/newrelic/defaults/  
ADD plugins /etc/newrelic/plugins/  
WORKDIR "/etc/newrelic"  
  
VOLUME ["/etc/newrelic/backends"]  
  
CMD ["supervisord"]  

