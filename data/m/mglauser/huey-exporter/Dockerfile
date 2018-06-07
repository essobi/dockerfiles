FROM python:3.6-alpine  
  
ENV APPDIR=/app/  
WORKDIR $APPDIR  
  
COPY requirements.txt $APPDIR  
RUN pip install -r requirements.txt  
  
COPY . $APPDIR  
RUN python setup.py install  
  
CMD ["huey_exporter"]

