FROM registry:0.9.1  
RUN apt-get update && apt-get install -y \  
libxml2-dev \  
libxslt1-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install docker-registry-driver-swift  
  
ENV SETTINGS_FLAVOR swift  
ENV OS_CONTAINER docker-registry  
ENV SEARCH_BACKEND sqlalchemy  
ENV SQLALCHEMY_INDEX_DATABASE sqlite:////tmp/docker-registry.db  
ENV GUNICORN_OPTS [--preload]  
ENV CACHE_LRU_REDIS_DB 1  
CMD sed -i -e "s/_env:OS_TENANT_NAME/\"$OS_TENANT_NAME\"/g" docker-
registry/config/config_sample.yml \  
&& export CACHE_REDIS_HOST=$REDIS_PORT_6379_TCP_ADDR \  
&& export CACHE_REDIS_PORT=$REDIS_PORT_6379_TCP_PORT \  
&& export CACHE_LRU_REDIS_HOST=$REDIS_PORT_6379_TCP_ADDR \  
&& export CACHE_LRU_REDIS_PORT=$REDIS_PORT_6379_TCP_PORT \  
&& docker-registry  

