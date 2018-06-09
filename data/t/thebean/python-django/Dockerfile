FROM python:2.7-slim  
  
LABEL io.openshift.tags django,python,frontend \  
io.k8s.description The frontend container for the django application \  
io.openshift.wants mysql \  
io.openshift.expose-services 8080/tcp \  
io.openshift.min-memory 4Gi \  
io.openshift.min-cpu 2  
  
COPY docker-entrypoint.sh requirements.txt gunicorn_log.conf /  
  
RUN apt-get update && \  
apt-get -y install python-mysqldb libmysqlclient-dev gcc --no-install-
recommends && \  
pip install -r /requirements.txt && \  
apt-get -y purge wget curl git && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
apt list --installed  
  
VOLUME ['/data']  
  
EXPOSE 8080  
  
WORKDIR /data  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]

