FROM grafana/grafana:3.0.1  
  
RUN mkdir -p /var/lib/grafana  
ADD grafana.db /var/lib/grafana/  
  
ENTRYPOINT ["/run.sh"]  

