FROM python:2.7-alpine  
  
ADD requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt  
ADD notify.py /bin/notify.py  
RUN chmod +x /bin/notify.py  
  
ENTRYPOINT /bin/notify.py  

