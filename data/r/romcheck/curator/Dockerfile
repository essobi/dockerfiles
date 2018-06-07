FROM python:alpine  
  
RUN pip install elasticsearch-curator  
  
COPY entrypoint.sh /opt/  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  
  
CMD ["crond", "-f"]  

