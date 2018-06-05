FROM jpizarrom/osrm-data-prepare-docker:v5.2.6  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
luarocks \  
libpq-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN luarocks install luasql-postgres PGSQL_INCDIR=/usr/include/postgresql  
  
ADD profiles/bicycle.lua /opt/osrm/profiles/  

