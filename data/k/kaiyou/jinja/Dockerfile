FROM python:3-alpine3.6  
RUN pip install docker-py Jinja2  
  
ADD run.py utils.py /  
  
VOLUME ["/docker.sock", "/src", "/dst"]  
  
ENTRYPOINT ["/run.py", "unix:///docker.sock"]  
  
CMD ["/srv", "/dst", "-t", "start", "die"]  
  

