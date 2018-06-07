FROM debian:jessie  
WORKDIR /src  
RUN apt-get update && apt-get install -y python3-pandas python3-requests
python3-pip  
RUN pip3 install nameparser sseclient robobrowser docopt  
ADD fencing/*.py /src/  
CMD bash  

