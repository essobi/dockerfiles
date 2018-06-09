FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y python python-pip curl  
  
RUN pip install mcstatus  
  
COPY entrypoint.sh /entrypoint.sh  
COPY simplestatus.py /simplestatus.py  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
  

