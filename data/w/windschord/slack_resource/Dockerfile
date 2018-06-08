FROM python:3-alpine  
  
# install requirements  
ADD requirements*.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
# install asserts  
ADD assets/ /opt/resource/  

