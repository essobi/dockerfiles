FROM python:3.6-slim  
MAINTAINER @germangb <germangb42@gmail.com>  
  
RUN pip install jupyter  
  
WORKDIR /workspace  
  
CMD [ "jupyter-notebook", "--no-browser", "--ip=0.0.0.0" ]  

