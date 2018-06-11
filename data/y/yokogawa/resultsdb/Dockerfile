FROM python:2.7  
WORKDIR /app  
  
ENV RESULTSDB_VERSION 2.0.5  
RUN set -ex \  
&& git clone https://pagure.io/taskotron/resultsdb.git \  
&& cd resultsdb \  
&& pip install -r requirements.txt \  
&& python setup.py develop  
  
ENV DEV true  
COPY ./settings.py /app/resultsdb/conf/settings.py  
  
RUN mkdir -p /resultsdb_data  
WORKDIR /app/resultsdb  
CMD ["python", "runapp.py"]  

