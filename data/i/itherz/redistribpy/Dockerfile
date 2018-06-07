FROM ubuntu  
  
RUN DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get install -y python python-pip && pip install
redis-trib  
  
ENTRYPOINT [ "/usr/bin/python2.7", "/usr/local/bin/redis-trib.py" ]  

