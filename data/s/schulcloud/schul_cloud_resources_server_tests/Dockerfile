FROM python:alpine  
  
RUN mkdir -p /app/schul_cloud_resources_server_tests/  
WORKDIR /app  
  
ADD requirements.txt /app/  
RUN pip install -r requirements.txt  
  
ADD schul_cloud_resources_server_tests/
/app/schul_cloud_resources_server_tests/  
  
EXPOSE 8080  
ENV PYTHONUNBUFFERED=1  
ENTRYPOINT python -m schul_cloud_resources_server_tests.app  

