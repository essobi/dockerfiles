FROM python:3.6  
  
MAINTAINER MobydevTeam  
  
RUN apt-get update && apt-get install -y \  
gcc \  
gettext \  
postgresql-client libpq-dev \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
ENV DJANGO_VERSION 1.10.1  
  
RUN pip install psycopg2 django=="$DJANGO_VERSION"  

