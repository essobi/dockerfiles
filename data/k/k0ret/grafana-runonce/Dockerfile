FROM grafana/grafana  
  
RUN apt-get update && \  
apt-get install supervisor -y && \  
rm -rf /var/lib/apt/lists/*  
  
COPY grafana_setup.sh /opt/grafana_setup.sh  
COPY grafana_supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ENV DOCKER_SECRET_NAME=  
RUN touch /opt/grafana_run_once.sh && \  
chmod +x /opt/grafana_setup.sh /opt/grafana_run_once.sh && \  
mkdir -p /var/log/supervisor  
  
ENTRYPOINT /usr/bin/supervisord  

