FROM frictionlessdata/datapackage-pipelines:latest  
  
RUN apk --update add postgresql-client openjdk7-jre build-base  
# Install this first so that we have shorted build times  
RUN pip install tabula-py  
  
ADD . /app  
WORKDIR /app  
RUN pip install .  
RUN python add_pipeline_dependencies.py  
  
CMD ["server"]  

