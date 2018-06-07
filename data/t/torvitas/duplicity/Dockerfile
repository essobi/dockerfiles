FROM fedora:22  
RUN dnf install duplicity cronie procps-ng -y  
COPY crontab /etc/cron.d/duplicity-cron  
RUN chmod 644 /etc/cron.d/duplicity-cron  
RUN touch /var/log/cron.log  
COPY backup.sh /backup.sh  
COPY init.sh /init.sh  
VOLUME /var/log/cron/  
CMD ["/bin/bash", "/init.sh"]  

