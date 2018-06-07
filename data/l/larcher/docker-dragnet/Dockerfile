FROM python:3.4  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends libatlas-dev libatlas3gf-base  
  
RUN pip install numpy && \  
pip install --upgrade cython && \  
pip install lxml && \  
pip install dragnet  
  

