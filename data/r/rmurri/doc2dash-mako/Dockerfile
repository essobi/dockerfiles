FROM rmurri/doc2dash  
  
RUN pip install changelog \  
sphinx-paramlinks  
  
COPY entrypoint.sh /entrypoint  
ENTRYPOINT ["/bin/sh", "/entrypoint"]  

