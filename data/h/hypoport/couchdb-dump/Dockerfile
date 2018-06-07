FROM python:3.6.4-alpine3.7  
WORKDIR /couchdb_dump/lib  
COPY . .  
RUN pip install -r requirements.txt && \  
chmod +x *.py && \  
ln -s /couchdb_dump/lib/couchdb_dump.py /usr/local/bin/cdbdump && \  
ln -s /couchdb_dump/lib/couchdb_load.py /usr/local/bin/cdbload  

