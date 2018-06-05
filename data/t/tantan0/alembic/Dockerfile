FROM python:alpine  
  
RUN apk add \--no-cache  \--virtual build-deps gcc python3-dev musl-dev \  
&& apk add \--no-cache postgresql-dev \  
&& pip install \--no-cache-dir alembic psycopg2-binary \  
&& apk del build-deps gcc  
  
WORKDIR ["/data"]  

