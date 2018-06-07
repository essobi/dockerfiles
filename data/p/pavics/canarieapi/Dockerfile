FROM nginx  
MAINTAINER David Byrns  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
python-dev \  
python-pip \  
cron \  
vim \  
sqlite3  
  
RUN pip install --upgrade pip setuptools  
RUN pip install gunicorn gevent  
  
# Add logparser cron job in the cron directory  
ADD canarieapi-cron /etc/cron.d/canarieapi-cron  
RUN chmod 0644 /etc/cron.d/canarieapi-cron  
  
# Install the canarie api package  
COPY requirements.txt /opt/local/src/CanarieAPI/requirements.txt  
RUN pip install -r /opt/local/src/CanarieAPI/requirements.txt  
COPY ./ /opt/local/src/CanarieAPI/  
RUN pip install /opt/local/src/CanarieAPI/  
  
WORKDIR /opt/local/src/CanarieAPI/canarieapi  
  
# cron job will inherit the current user environment  
# start cron service  
# start nginx service  
# start gunicorn  
CMD env >> /etc/environment && \  
cron && \  
nginx && \  
gunicorn -b 0.0.0.0:2000 --workers 1 --log-level=DEBUG --timeout 30 -k gevent
wsgi

