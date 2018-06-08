FROM python:2  
ENV PGADMIN_VERSION=1.0 \  
PGADMIN_SUFFIX=beta3 \  
PGADMIN_SUFFIX_MINI=b3  
  
RUN set -ex \  
&& buildDeps=' \  
postgresql-server-dev-all \  
' \  
&& runDeps=' \  
' \  
&& apt-get update && apt-get install -y $runDeps $buildDeps \--no-install-
recommends && rm -rf /var/lib/apt/lists/* \  
&& echo
"https://ftp.postgresql.org/pub/pgadmin3/pgadmin4/v${PGADMIN_VERSION}-${PGADMIN_SUFFIX}/pip/pgadmin4-${PGADMIN_VERSION}${PGADMIN_SUFFIX_MINI}-py2-none-
any.whl" > requirements.txt \  
&& pip install --upgrade pip \  
&& pip install --no-cache-dir -r requirements.txt \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /usr/src/python ~/.cache  
  
WORKDIR /usr/local/lib/python2.7/site-packages/pgadmin4/  
  
RUN cp config.py config_local.py \  
&& sed -i "s/SERVER_MODE = True/SERVER_MODE = False/g;s/DEFAULT_SERVER =
'localhost'/DEFAULT_SERVER = '0.0.0.0'/g" config_local.py  
  
EXPOSE 5050  
ENTRYPOINT [ "python", "./pgAdmin4.py" ]  

