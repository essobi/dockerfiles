FROM nmirinagoyansaito/python-base  
  
USER root  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN pip install --upgrade pip && \  
pip install setuptools && \  
pip install cupy==3.0.0a1 chainer==4.0.0a1  
  
USER $USER_NAME  
WORKDIR /workdir  

