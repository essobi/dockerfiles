# consult: https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices  
# Forked: https://hub.docker.com/r/amancevice/pandas  
FROM phirov/pandas:0.19-2  
MAINTAINER phirov@163.com  
  
ENV PYMSSQL_BUILD_WITH_BUNDLED_FREETDS 1  
  
RUN apk add --no-cache \  
\--virtual .build-deps \  
gcc \  
g++ \  
musl-dev \  
python-dev \  
postgresql-dev \  
py-psycopg2 \  
freetds-dev \  
unixodbc-dev \  
git && \  
pip install pykafka \  
pymongo \  
redis \  
boto \  
boto3 \  
pyodbc \  
psycopg2 \  
setuptools_git \  
rarfile \  
xlrd && \  
pip install pymssql && \  
pip install -e
git+http://wangying:wangying28779@54.223.34.209:10080/cyan/pipo.git@dev#egg=pipo  
#apk del .build-deps  

