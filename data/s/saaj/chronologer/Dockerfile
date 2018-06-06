FROM python:3.5-slim  
  
MAINTAINER saaj <mail@saaj.me>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
COPY setup.py /opt/chronologer/  
WORKDIR /opt/chronologer  
RUN set -ex; \  
apt-get update; \  
apt-get install --yes --no-install-recommends \  
build-essential libmysqlclient-dev libmysqlclient18; \  
touch README.rst; \  
pip install --no-cache-dir -e .[mysql]; \  
apt-get purge --yes --auto-remove build-essential libmysqlclient-dev; \  
rm -rf /var/lib/apt/lists/*;  
  
COPY chronologer chronologer  
  
EXPOSE 8080  
CMD ["python", "-m", "chronologer", "-e", "production", \  
"serve", "-u", "www-data", "-g", "www-data"]  

