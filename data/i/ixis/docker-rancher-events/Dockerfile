FROM python:2.7.11  
#Create rancher-events folder structure  
RUN mkdir -p /srv/rancher-events/  
  
ADD ./listener.py /srv/rancher-events/listener.py  
ADD ./processor.py /srv/rancher-events/processor.py  
ADD ./requirements.txt /srv/rancher-events/requirements.txt  
  
WORKDIR /srv/rancher-events  
RUN pip install -r /srv/rancher-events/requirements.txt  
  
CMD ["/usr/local/bin/python", "/srv/rancher-events/listener.py"]

