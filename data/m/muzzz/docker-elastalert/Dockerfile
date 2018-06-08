FROM python:2.7  
MAINTAINER Muz Ali "docker-elastalert@mustaqila.li"  
WORKDIR /opt/elastalert  
  
RUN wget -O- https://github.com/Yelp/elastalert/archive/v0.1.14.tar.gz \  
| tar -xz --strip-components=1  
  
RUN pip install -r requirements.txt \  
&& python ./setup.py install  
  
RUN mkdir -p /etc/elastalert  
  
CMD ["python", "-m", "elastalert.elastalert", "--config",
"/etc/elastalert/config.yaml", "--verbose"]  

