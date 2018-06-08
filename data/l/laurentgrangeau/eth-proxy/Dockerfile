FROM ubuntu:15.10  
WORKDIR /tmp/  
  
RUN apt-get update && apt-get -yy install python-twisted unzip wget  
RUN wget http://dwarfpool.com/static/eth-proxy.zip  
RUN unzip eth-proxy.zip  
  
COPY eth-proxy.conf /tmp/eth-proxy/  
  
WORKDIR /tmp/eth-proxy/  
  
EXPOSE 8080  
CMD python ./eth-proxy.py  

