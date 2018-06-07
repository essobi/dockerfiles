FROM python:2-onbuild  
MAINTAINER Samuel Vandamme <samuel.vandamme@coscale.com>  
  
ENV PYTHONUNBUFFERED 0  
ENV DATABASE_HOST database  
ENV DATABASE_USER root  
ENV DATABASE_PASS secret  
ENV DATABASE_TABLE my_db  
ENV REDIS_HOST redis  
  
WORKDIR /usr/src/app/  
  
ADD . /usr/src/app/  
CMD [ "python", "/usr/src/app/main.py" ]  
  
LABEL
com.coscale.monitoring='[{"PluginType":"LOGPLUGIN","Configuration":{"MATCH":["\"/dev/stdout\"
\"COUNTER\" \"Log lines\" \".*\" \"#\""]}}]'  

