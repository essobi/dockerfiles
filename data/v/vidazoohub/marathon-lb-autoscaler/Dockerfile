FROM python:2.7-alpine  
  
COPY /marathon-lb-autoscaler.py /marathon-lb-autoscaler.py  
  
RUN pip install requests boto3  
  
CMD python /marathon-lb-autoscaler.py

