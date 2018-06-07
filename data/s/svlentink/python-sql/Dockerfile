FROM python:alpine  
  
RUN pip install pyyaml #requirements.txt  
  
RUN apk add --no-cache gcc g++ #requirements for db connectors  
RUN apk add --no-cache postgresql-dev \  
&& pip install psycopg2 #postgres  
RUN apk add --no-cache mariadb-dev \  
&& pip install mysqlclient  
  
# shared lib, which enable you to 'from dblib import db_sql'  
COPY dblib.py /tmp/dblib.py  
RUN mv /tmp/dblib.py '/usr/local/lib/python'${PYTHON_VERSION:0:3}/  
  
# container that uses this container (or docker-compose and volume)  
ENV DB_CONFIG_LOC /proj/config.yml  
ENTRYPOINT ["/proj/main.py"]  
VOLUME /proj  

