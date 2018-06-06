FROM ubuntu:17.10  
RUN apt-get update; \  
apt-get install -y python python-pip; \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install python-vipaccess  
  
COPY ./generate.py /opt/generate.py  
  
CMD /opt/generate.py  

