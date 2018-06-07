FROM python:2.7-alpine  
RUN pip install boto3  
ADD invoke.py invoke.py  
entrypoint ["python", "/invoke.py"]  

