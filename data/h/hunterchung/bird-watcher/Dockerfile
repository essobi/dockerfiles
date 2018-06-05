FROM python:3  
MAINTAINER Hunter Chung <hchung@zymoresearch.com>  
  
RUN pip install -U \  
pip \  
jinja2 \  
flask \  
boto3 \  
pymongo \  
ipython \  
mongoengine \  
pandas \  
lxml \  
html5lib \  
BeautifulSoup4 \  
flask-mongoengine \  
humanize  
  
# RUN apt-get update && apt-get dist-upgrade -y -q && apt-get -y -q install \  
# rsync && \  
# apt-get clean autoclean && apt-get autoremove -y  
# ADD bird_watcher /scripts/bird_watcher  
VOLUME /data  
ENV PYTHONPATH=/scripts  
EXPOSE 5000  

