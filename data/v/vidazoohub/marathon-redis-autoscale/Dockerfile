FROM python:2.7-alpine  
  
COPY /marathon-redis-autoscale.py /marathon-redis-autoscale.py  
  
RUN pip install requests redis marathon  
  
CMD python /marathon-redis-autoscale.py

