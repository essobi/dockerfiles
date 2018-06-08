FROM python:alpine  
MAINTAINER Michael Housh <mhoush@houshhomeenergy.com>  
  
RUN pip install --no-cache-dir --upgrade \  
pip \  
sphinx  
  
VOLUME /mnt  
  
WORKDIR /mnt  
  
CMD ["sphinx-quickstart"]  

