FROM milafrerichs/docker-tilestache  
  
RUN pip install gunicorn jinja2 redis newrelic  
  
RUN mkdir /nepal-tiles  
WORKDIR /nepal-tiles  
  
ADD tilestache.cfg /nepal-tiles/tilestache.cfg  
ADD wsgi.py /nepal-tiles/wsgi.py  
ADD app.ini /nepal-tiles/app.ini  
ADD gunicorn.py /nepal-tiles/gunicorn.py  
  
RUN newrelic-admin generate-config 64444f7964adea4ef24e2e7edcdf43adc3621866
newrelic.ini  
ENV NEW_RELIC_CONFIG_FILE=newrelic.ini  
  
EXPOSE 8080  
CMD newrelic-admin run-program gunicorn wsgi.py --bind 0.0.0.0:8080  

