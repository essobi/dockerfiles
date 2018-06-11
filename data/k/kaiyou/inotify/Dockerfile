FROM python:3-alpine  
  
RUN pip install docker-py inotify pyaml  
  
ADD run.py /  
ADD empty.yaml /config.yaml  
  
VOLUME ["/docker.sock"]  
  
ENTRYPOINT ["/run.py", "unix:///docker.sock"]  
  
CMD ["/config.yaml"]  

