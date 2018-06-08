#  
# Simple Dockerfile for running the faafo application.  
# API and worker run with the same container  
# they just need to start different binaries  
#  
FROM python:2.7  
ADD . /code  
  
WORKDIR /code  
  
RUN pip install -r requirements.txt  
RUN python setup.py install  
  
ENTRYPOINT ["/code/contrib/faafo-wrapper.sh"]  

