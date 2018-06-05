FROM python:3.5.2-slim  
  
RUN set -ex \  
&& apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
&& buildDeps=' \  
gcc \  
libpq-dev \  
' \  
&& apt-get install -y $buildDeps --no-install-recommends \  
&& pip install -U --no-cache-dir \  
pip \  
pymysql \  
psycopg2 \  
alembic \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /tmp/* ~/.cache /var/lib/apt/lists/*  
  
VOLUME /var/project  
WORKDIR /var/project  

