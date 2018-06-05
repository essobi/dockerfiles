FROM debian:latest  
ENV
METRICBEAT_SOURCE_URL=https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-5.4.1-linux-x86_64.tar.gz  
  
RUN apt-get update \  
&& apt-get -y install curl \  
&& mkdir /tmp/install \  
&& cd /tmp/install \  
&& curl $METRICBEAT_SOURCE_URL | tar xvz \  
&& mv metricbeat-*/scripts/import_dashboards / \  
&& rm -rf /tmp/install \  
&& apt-get remove -y curl \  
&& apt-get autoremove -y \  
&& apt-get clean -y  
  
ENTRYPOINT ["/import_dashboards"]

