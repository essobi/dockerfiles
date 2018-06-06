FROM ubuntu:15.10  
MAINTAINER Giacomo Tenaglia <Giacomo.Tenaglia@gmail.com>  
RUN apt-get update && apt-get install -y python python-requests python-
websocket  
ADD example-client.py /example-client.py  
CMD python /example-client.py  

