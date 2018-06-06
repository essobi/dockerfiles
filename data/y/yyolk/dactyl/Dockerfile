FROM python:3-slim-stretch  
MAINTAINER Joseph Yølk Chiocchi <joe@yolk.cc>  
  
ENV WORKSPACE /ws  
  
RUN pip install -U dactyl && mkdir -p $WORKSPACE  
WORKDIR $WORKSPACE  
VOLUME $WORKSPACE  
  
ENTRYPOINT ["dactyl_build"]  
  
CMD []  

