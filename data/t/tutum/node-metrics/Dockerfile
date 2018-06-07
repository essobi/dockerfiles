FROM tutum/curl:trusty  
MAINTAINER Feng Honglin <hfeng@tutum.co>  
  
RUN apt-get update && apt-get install -y sysstat bc  
  
ADD metrics.template /metrics.template  
ADD crontab.conf /crontab.conf  
ADD run.sh /run.sh  
ADD clean_metrics_data.sh /clean_metrics_data.sh  
ADD collect_node_metrics.sh /collect_node_metrics.sh  
RUN chmod +x /*.sh  
  
ENV DB_NAME nodemetrics  
ENV DB_USER root  
ENV DB_PASS root  
ENV SERIES_NAME stats  
  
ENV DATA_CLEAN_SINCE 1w  
  
CMD ["/run.sh"]  

