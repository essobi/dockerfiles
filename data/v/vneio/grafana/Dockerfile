FROM grafana/grafana  
MAINTAINER Ivan Yaroslavov Stefanov <ivan.yaroslavov@vne.io>  
  
COPY ./dashboards /init/dashboards  
COPY ./grafana.ini /init/  
COPY ./grafana.db /init/  
COPY ./init-grafana.sh /init-grafana.sh  
  
ENTRYPOINT /init-grafana.sh && /run.sh  

