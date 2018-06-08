FROM registry:0.9.1  
ENV SEARCH_BACKEND sqlalchemy  
ENV SQLALCHEMY_INDEX_DATABASE sqlite:////opt/sqlitedb/reg.db  
ENV STORAGE_PATH /opt/registry  
  
ENV MIRROR_SOURCE https://registry-1.docker.io  
ENV MIRROR_SOURCE_INDEX https://index.docker.io  
ENV MIRROR_TAGS_CACHE_TTL 172800  
ADD ./config.yml /docker-registry/config/config_sample.yml  
  
CMD exec docker-registry  

