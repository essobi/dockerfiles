FROM grafana/grafana:4.6.2  
USER root  
  
COPY ./grafana/datasources /etc/grafana/datasources  
COPY ./grafana/dashboards /etc/grafana/dashboards  
COPY ./grafana/alert-notifications /etc/grafana/alert-notifications  
COPY ./grafana/setup.sh /setup.sh  
  
RUN chmod +x /setup.sh  
  
ENTRYPOINT ["/setup.sh"]  

