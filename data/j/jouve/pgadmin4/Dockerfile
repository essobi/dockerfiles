FROM python:3.6-alpine3.7  
  
ARG PGADMIN_VERSION=3.0  
RUN apk add --no-cache libpq postgresql-dev gcc musl-dev && \  
pip install --no-cache-dir
https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v${PGADMIN_VERSION}/pip/pgadmin4-${PGADMIN_VERSION}-py2.py3-none-
any.whl gunicorn && \  
apk del --no-cache postgresql-dev gcc musl-dev && \  
mv /usr/local/lib/python3.6/site-packages/pgadmin4/docs/en_US/_build /tmp && \  
rm -rf /usr/local/lib/python3.6/site-packages/pgadmin4/docs/en_US && mkdir
/usr/local/lib/python3.6/site-packages/pgadmin4/docs/en_US && \  
mv /tmp/_build /usr/local/lib/python3.6/site-packages/pgadmin4/docs/en_US  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
EXPOSE 8000  
  
VOLUME /var/lib/pgadmin /var/log/pgadmin  
  
CMD [ "/docker-entrypoint.sh" ]  
  

