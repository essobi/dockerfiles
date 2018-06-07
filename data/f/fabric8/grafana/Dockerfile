FROM grafana/grafana:4.1.1  
MAINTAINER Jimmi Dyson <jimmidyson@gmail.com>, Kamesh Sampath
<kamesh.sampath@hotmail.com>  
  
ENTRYPOINT ["/run.sh"]  
  
ENV GF_AUTH_ANONYMOUS_ENABLED true  
ENV GF_DASHBOARDS_JSON_ENABLED true  
ENV GF_DASHBOARDS_JSON_PATH /dashboards  
ENV GF_LOG_MODE console  
  
RUN apt-get update && \  
apt-get install -y curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
chmod 777 /var/lib/grafana /usr/share/grafana/  
  
ADD run.sh /run.sh  
ADD dashboards /dashboards  
RUN chmod 777 /dashboards && chmod 666 /dashboards/*  
  
USER grafana  

