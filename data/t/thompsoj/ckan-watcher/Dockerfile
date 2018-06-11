FROM python:3-onbuild  
ENV SITE https://data.gov.au  
ENV APIKEY placeholder  
ENV USER_AGENT CKAN_AGENT/1.0 (+https://data.gov.au)  
ENV ORGANISATION primeministerandcabinet  
  
COPY ./watcher.py /src/watcher.py  
COPY ./docker-entrypoint.sh /src/docker-entrypoint.sh  
CMD ["bash", "/src/docker-entrypoint.sh"]  

