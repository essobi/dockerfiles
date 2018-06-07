FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.0.6 as tester  
MAINTAINER toolbox@cloudpassage.com  
  
RUN mkdir /app  
  
COPY app/ /app/  
  
RUN pip install -r /app/requirements-test.txt  
  
WORKDIR /app/  
  
RUN /usr/bin/python -mpy.test --cov=ehdlib --cov-report=term-missing /app/test
-s  
  
#######################  
FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.0.6 as downloader  
MAINTAINER toolbox@cloudpassage.com  
  
RUN mkdir /app  
  
COPY app/ /app/  
  
RUN pip install -r /app/requirements.txt  
  
WORKDIR /app/  
  
CMD ["/usr/bin/python", "/app/application.py"]  

