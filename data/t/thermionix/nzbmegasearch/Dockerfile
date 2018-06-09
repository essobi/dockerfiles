FROM ubuntu  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get install -y python2.7 git python-openssl  
  
RUN git clone https://github.com/pillone/usntssearch.git usntssearch  
  
EXPOSE 5000  
#VOLUME /usntssearch  
WORKDIR /usntssearch/NZBmegasearch/  
  
ENTRYPOINT ["python", "mega2.py"]  
  

