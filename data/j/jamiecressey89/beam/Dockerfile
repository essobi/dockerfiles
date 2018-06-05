FROM python:2.7-alpine  
COPY . /beam  
RUN cd /beam && pip install -r requirements.txt && python setup.py install  
  
ENTRYPOINT ["/usr/local/bin/run.py"]  

