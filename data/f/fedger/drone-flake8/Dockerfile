FROM python:3.5-alpine  
  
RUN pip --no-cache-dir install \  
flake8 \  
flake8-import-order \  
pep8-naming  
  
COPY entrypoint.sh /usr/local/bin/drone-flake8  
ENTRYPOINT ["drone-flake8"]  

