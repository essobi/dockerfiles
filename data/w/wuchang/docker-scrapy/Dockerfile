FROM python:3  
RUN apt-get update && apt-get install -y software-properties-common  
  
RUN apt-get install python python-pip libxml2-dev libxslt1-dev python-dev
zlib1g-dev \  
python3-dev python3-pip vim libffi-dev libssl-dev -y  
  
RUN pip install virtualenv  
  
RUN pip install readability-lxml scrapy pysolr  
RUN pip3 install readability-lxml scrapy pysolr  
  
WORKDIR /data  

