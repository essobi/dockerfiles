FROM python:2  
ENV MIRRORS=/var/mirrors/data MIRROR_CONFIG=/var/mirrors/config.txt SLEEP=5m  
  
VOLUME /var/mirrors  
COPY scripts/* /opt/scripts/  
  
CMD ["bash", "/opt/scripts/startup.sh"]  

