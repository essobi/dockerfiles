FROM python:2.7-alpine  
  
COPY /marathon-rabbit-autoscale.py /marathon-rabbit-autoscale.py  
  
RUN pip install requests marathon pyrabbit  
  
CMD python /marathon-rabbit-autoscale.py

