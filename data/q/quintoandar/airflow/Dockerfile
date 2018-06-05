FROM python:2  
RUN adduser airflow  
  
ENV AIRFLOW_HOME /opt/current-app  
  
ADD requirements.txt ./  
  
RUN pip install -r requirements.txt  
  
WORKDIR /opt/current-app

