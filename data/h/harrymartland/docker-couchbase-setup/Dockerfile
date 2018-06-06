FROM python:3-alpine  
  
RUN pip3 install requests  
  
ENV COUCHBASE_PORT 8091  
COPY setup_couchbase.py /opt/app/setup_couchbase.py  
  
RUN chmod +x /opt/app/setup_couchbase.py  
  
CMD [ "python", "/opt/app/setup_couchbase.py" ]

