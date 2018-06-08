# minimal runtime  
# without odbc and memcache support  
FROM python:3-alpine  
MAINTAINER Jack King  
  
WORKDIR /usr/src/app  
  
# install requirements  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
# copy code to work folder  
COPY . .  
  
# set env  
ENV LISTENING_ADDRESS='0.0.0.0'  
# entry  
CMD python start.py

