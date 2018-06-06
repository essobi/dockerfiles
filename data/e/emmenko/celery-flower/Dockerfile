FROM celery:3  
  
MAINTAINER Nicola Molinari <emmenko@gmail.com>  
  
USER root  
  
RUN apt-get update && apt-get install -y python-pip; \  
pip install flower  
  
ENTRYPOINT ["celery", "flower"]  

