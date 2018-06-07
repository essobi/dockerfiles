FROM python:3.5-alpine  
  
COPY scripts/ /opt/app-root/scripts  
  
WORKDIR /opt/app-root/  
  
RUN pip install requests  
  
RUN chown -R 1001:0 /opt/app-root  
  
USER 1001  
ENTRYPOINT ["scripts/hawkular-check.py"]

