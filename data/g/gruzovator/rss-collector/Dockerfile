FROM postgres:9.6-alpine  
  
RUN apk add -U git python3 \  
gcc g++ linux-headers musl-dev libpq python3-dev postgresql-dev py-lxml
supervisor && \  
pip3 --no-cache-dir install -U pip && \  
pip3 --no-cache-dir install gunicorn psycopg2-binary==2.7.4 asyncpg==0.15.0&&
\  
apk del gcc g++ linux-headers musl-dev python3-dev postgresql-dev && \  
ln -sf /usr/bin/python3 /usr/bin/python  
  
WORKDIR /rss-collector  
  
ENV PYTHONPATH /rss-collector  
  
COPY core ./core  
  
COPY housekeeper ./housekeeper  
RUN pip install -r ./housekeeper/requirements.txt  
  
COPY reader ./reader  
RUN pip install -r ./reader/requirements.txt  
  
COPY streamserver ./streamserver  
RUN pip install -r ./streamserver/requirements.txt  
  
COPY webadmin ./webadmin  
RUN pip install -r ./webadmin/requirements.txt  
  
COPY config.yml supervisord.conf ./  
  
EXPOSE 5432 8080 9000  
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/rss-
collector/supervisord.conf"]

