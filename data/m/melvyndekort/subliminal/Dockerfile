FROM python:alpine  
  
RUN pip install --no-cache-dir schedule subliminal  
  
RUN mkdir /.cache /tvshows \  
&& chmod 777 /.cache /tvshows  
  
COPY startup.sh /  
COPY job.py /  
  
VOLUME /tvshows /.cache  
  
CMD ["/startup.sh"]  
  

