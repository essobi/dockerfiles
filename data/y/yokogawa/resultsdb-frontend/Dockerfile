FROM python:2.7  
WORKDIR /app  
RUN set -ex \  
&& git clone https://pagure.io/taskotron/resultsdb_frontend.git \  
&& cd resultsdb_frontend \  
&& pip install -r requirements.txt  
  
ENV DEV true  
EXPOSE 5002  
COPY ./settings.py /app/resultsdb_frontend/conf/settings.py  
  
WORKDIR /app/resultsdb_frontend  
CMD ["python", "runapp.py"]  

