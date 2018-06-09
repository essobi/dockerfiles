FROM prom/prometheus:v1.5.0  
COPY prometheus.yml /etc/prometheus/prometheus.yml  
ENTRYPOINT [ "/bin/prometheus" ]  
CMD [ "-config.file=/etc/prometheus/prometheus.yml", \  
"-storage.local.path=/prometheus", \  
"-storage.local.retention=48h", \  
"-web.console.libraries=/usr/share/prometheus/console_libraries", \  
"-web.console.templates=/usr/share/prometheus/consoles" ]  

