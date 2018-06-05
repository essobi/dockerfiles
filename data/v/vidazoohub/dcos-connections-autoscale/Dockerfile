FROM python:2.7-alpine  
  
COPY /dcos-connections-autoscale.py /dcos-connections-autoscale.py  
  
RUN pip install requests haproxy-stats dnspython  
  
CMD python /dcos-connections-autoscale.py

