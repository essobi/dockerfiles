FROM python:3  
WORKDIR /usr/src/schul_cloud_search_tests  
  
ADD requirements.txt ./  
ADD LICENSE ./  
ADD schul_cloud_search_tests/ ./  
  
RUN pip3 install -r requirements.txt  
WORKDIR /usr/src  
  
ENV PYTHONUNBUFFERED=1  
ENTRYPOINT python3 -m schul_cloud_search_tests.proxy  

