FROM python:3.5-slim  
  
USER root  
ENV CELERY_VERSION 4.0.2  
RUN pip install celery=="$CELERY_VERSION"  
  
RUN mkdir /myapp  
ADD tasks.py myapp/tasks.py  
ADD __init__.py myapp/__init__.py  
ENV C_FORCE_ROOT='true'  
VOLUME /home/user/myapp/tasks.py  
  
CMD celery worker -A myapp.tasks -B --loglevel=info  

