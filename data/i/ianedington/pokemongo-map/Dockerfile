FROM python:2.7  
ADD /PokemonGo-Map /pg-map  
RUN pip install --no-cache-dir -r /pg-map/requirements.txt  
  
RUN ln -s /usr/local/bin/python /usr/bin/python  
RUN chmod +x /pg-map/runserver.py  
  
EXPOSE 80 433 5000  
ENTRYPOINT ["/pg-map/runserver.py"]  

