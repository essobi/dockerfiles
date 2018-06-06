FROM python:2.7.12  
RUN mkdir -p /data/web  
  
COPY requirements.txt /data/  
COPY sync.py /data/  
COPY web/ /data/web/  
COPY run.sh /data/  
  
RUN pip install -r /data/requirements.txt  
  
ENTRYPOINT ["/data/run.sh"]  

