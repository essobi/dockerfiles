FROM debian:jessie  
  
ENV SENTRY_VERSION 7.7.4  
RUN apt-get update -q && apt-get install -y \  
python python-dev python-pip \  
postgresql-client-common libpq-dev libxml2-dev libxslt-dev  
  
RUN pip install -U pip  
  
RUN pip install sentry[postgres]==${SENTRY_VERSION} \  
sentry-webhooks sentry-slack \  
dj-database-url dj-email-url  
  
EXPOSE 9000  
ADD sentry.conf.py /sentry.conf.py  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["/usr/local/bin/sentry", "--config=/sentry.conf.py"]  
CMD ["start"]  

