###### QNIBTerminal images  
FROM qnib/diamond:sensu  
  
# Refresh yum  
ENV TERM=xterm  
RUN echo "2015-09-27"; yum install -y bind-utils vim nmap  
  
# dependencies needed by costum scripts (e.g. osquery)  
RUN yum install -y libyaml-devel && \  
pip install envoy neo4jrestclient pyyaml docopt python-consul jinja2 && \  
pip install psutil graphitesend  
ADD opt/qnib/bin/watch_psutil.py /opt/qnib/bin/  
ADD etc/supervisord.d/watchpsutil.ini /etc/supervisord.d/  

