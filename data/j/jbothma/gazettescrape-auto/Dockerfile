FROM jbothma/gazettescrape-base-auto:latest  
  
RUN mkdir /app  
COPY gazettescrape /app/gazettescrape  
COPY gazettes /app/gazettes  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /app  
  
ENV PYTHONPATH=/app  
VOLUME ["/scrapedcache"]  
ENV LOCAL_CACHE_STORE_PATH=/scrapedcache  
  
CMD ["python", "gazettes/archive.py"]  

