FROM mwaaas/docker-airflow:latest  
  
ONBUILD COPY . /usr/src/app  
ONBUILD RUN pip install --no-cache-dir -r requirements.txt  
ONBUILD ENV AIRFLOW_HOME=/usr/src/app

