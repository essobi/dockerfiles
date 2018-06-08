FROM gyzpunk/readthedocs  
  
MAINTAINER gyzpunk "http://github.com/gyzpunk"  
  
ENV DJANGO_SETTINGS_MODULE="readthedocs.settings.postgres"  
  
USER root  
  
RUN pip install --no-cache-dir -r requirements/deploy.txt  
  
USER rtfd  
  
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8000", "--access-logfile=-", "
--error-logfile=-", "readthedocs.wsgi"]  

