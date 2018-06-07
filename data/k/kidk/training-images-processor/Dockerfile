FROM python:2-onbuild  
MAINTAINER Samuel Vandamme <samuel.vandamme@coscale.com>  
  
ENV PYTHONUNBUFFERED 0  
ENV DATABASE_HOST database  
ENV DATABASE_USER root  
ENV DATABASE_PASS secret  
ENV DATABASE_TABLE my_db  
ENV RABBITMQ_HOST rabbitmq  
  
CMD [ "python", "./main.py" ]  
  
LABEL
com.coscale.monitoring='[{"PluginType":"GENERICSCRIPT","Configuration":{"SCRIPT":["python
/usr/src/app/stats.py"]}}]'  

