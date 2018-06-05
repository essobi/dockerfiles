FROM prom/alertmanager  
  
COPY run.sh /etc/alertmanager  
COPY *.yml /etc/alertmanager/  
RUN chmod +x /etc/alertmanager/run.sh  
  
ENTRYPOINT []  
CMD ["/etc/alertmanager/run.sh"]  
  

