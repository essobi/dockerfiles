FROM python:alpine  
MAINTAINER Negash <i@negash.ru>  
  
WORKDIR /dist  
  
CMD ["python", "run.py"]  
  
RUN pip install --no-cache-dir \  
flask \  
flask-sqlalchemy \  
flask-apscheduler \  
flask-env \  
prometheus_client \  
requests  
  
ENV RESOLVE_TYPE=dns \  
DOMAIN='http://https.lb.rancher.internal:9000/?stats;csv' \  
RANCHER_METADATA='http://rancher-metadata.rancher.internal' \  
RANCHER_PATH='/2016-07-29/stacks/{stack}/services/{service}/containers'  
ADD ./run.py ./  
ADD ./server ./server

