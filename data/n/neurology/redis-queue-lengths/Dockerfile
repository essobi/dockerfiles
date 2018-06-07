FROM python:3.6-alpine  
  
RUN pip install redis influxdb  
COPY "stats.py" "/stats.py"  
CMD ["python", "/stats.py"]  

