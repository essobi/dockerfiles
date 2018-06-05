FROM python:3.4-slim  
  
RUN groupadd user && useradd --create-home --home-dir /home/user -g user user  
WORKDIR /home/user  
  
RUN pip install redis  
  
ENV CELERY_VERSION 3.1.18  
  
RUN pip install celery=="$CELERY_VERSION"  
  
COPY celeryconfig.py /home/user/  
  
USER user  
ENTRYPOINT ["celery", "beat", "--config=celeryconfig"]

