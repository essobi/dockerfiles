FROM python:2.7.8  
  
RUN apt-get update && apt-get install -y \  
postgresql-client-common \  
libpq-dev  
  
RUN pip install psycopg2 sentry redis  
  
EXPOSE 9000  
ADD sentry.conf.py /sentry.conf.py  
  
RUN /usr/local/bin/sentry \--config=/sentry.conf.py upgrade  
  
ENTRYPOINT ["/usr/local/bin/sentry", "--config=/sentry.conf.py"]  
CMD ["start"]  

