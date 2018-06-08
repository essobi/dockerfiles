FROM python:2.7.9  
RUN pip install supervisor  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  

