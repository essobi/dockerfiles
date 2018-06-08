FROM python:3-alpine  
  
WORKDIR /host  
  
RUN pip install -U pip && \  
pip install autopep8 isort  
  
ADD pyfix /  
  
ENTRYPOINT ["/pyfix"]  

