FROM docker.elastic.co/beats/metricbeat:5.6.3  
COPY metricbeat.yml /usr/share/metricbeat/metricbeat.yml  
USER root  
##RUN chown metricbeat /usr/share/metricbeat/metricbeat.yml && chmod go-w
/usr/share/metricbeat/metricbeat.yml  
RUN chown root /usr/share/metricbeat/metricbeat.yml && chmod go-w
/usr/share/metricbeat/metricbeat.yml  
##RUN addgroup docker --gid 999 && usermod --append --group docker metricbeat  
##USER metricbeat  

