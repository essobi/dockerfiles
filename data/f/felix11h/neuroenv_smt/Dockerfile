FROM neuralensemble/simulation  
MAINTAINER felix11h.dev@gmail.com  
  
USER root  
  
RUN $VENV/bin/pip install sumatra  
  
RUN apt-get -yq update && \  
apt-get install -qy screen  
  
EXPOSE 8000  
  
WORKDIR /home  

