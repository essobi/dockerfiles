FROM python:3-alpine  
  
RUN pip install tox  
  
WORKDIR /src  
VOLUME ["/src"]  
  
ENTRYPOINT ["tox"]  

