FROM python:3-alpine  
RUN pip install boto3  
ADD switch-role.py /switch-role.py  
ENTRYPOINT ["python", "/switch-role.py"]  

