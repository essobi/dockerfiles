FROM python:2.7-slim  
  
RUN groupadd celery && useradd --shell /bin/bash --create-home --home-dir
/home/celery -g celery celery  
WORKDIR /home/celery  
  
RUN pip install redis  
  
ENV CELERY_VERSION 3.1.18  
RUN pip install "celery==${CELERY_VERSION}"  
  
ENV BROKER_URL "amqp://guest:guest@localhost"  
ENV CELERY_RESULT_BACKEND "rpc://"  
ENV CELERY_RESULT_PERSISTENT 0  
ENV CELERY_IMPORTS "helloworld"  
ENV CELERYD_CONCURRENCY 4  
ENV CELERY_QUEUES "default"  
ENV CELERY_DEFAULT_QUEUE "default"  
ENV CELERY_DEFAULT_ROUTING_KEY "default"  
COPY celeryconfig.py celeryconfig.py  
  
COPY helloworld.py helloworld.py  
  
LABEL name="celery"  
  
USER celery  
ENTRYPOINT ["celery"]  
CMD ["worker", "--loglevel=INFO"]  
  

