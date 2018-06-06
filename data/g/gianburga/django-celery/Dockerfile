FROM ubuntu:14.04  
MAINTAINER Gian Burga <franco.burga@gmail.com>  
  
ENV DATABASE_URL **NULL**  
ENV SECRET_KEY **NULL**  
ENV DJANGO_VERSION 1.8  
ENV BROKER_URL amqp://guest:guest@rabbitmq:5672//  
ENV FLOWER_PORT 5555  
ENV DJANGO_PROJECT_NAME **NULL**  
  
RUN useradd -ms /bin/bash celery  
  
RUN mkdir /app  
WORKDIR /app  
  
VOLUME /app  
  
RUN apt-get update && apt-get install -y libmysqld-dev python-dev python-
setuptools supervisor && easy_install pip  
# RUN pip install --upgrade pip  
COPY supervisor/celerycam.conf /etc/supervisor/conf.d/celerycam.conf  
COPY supervisor/celery-flower.conf /etc/supervisor/conf.d/celery-flower.conf  
COPY init.d/celerycam /etc/init.d/celerycam  
COPY init.d/celerybeat /etc/init.d/celerybeat  
COPY default/celerybeat /etc/default/celerybeat  
COPY init.d/celeryd /etc/init.d/celeryd  
COPY default/celeryd /etc/default/celeryd  
COPY run.sh /run.sh  
  
RUN mkdir /var/log/celery && chown -R celery /var/log/celery/ && chmod +x
/etc/init.d/celerybeat && chmod +x /etc/init.d/celeryd && chmod +x
/etc/init.d/celerycam && chmod +x /run.sh  
  
EXPOSE 5555  
CMD ["/run.sh"]

