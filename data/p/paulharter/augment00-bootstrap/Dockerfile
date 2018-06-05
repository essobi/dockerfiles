FROM resin/rpi-raspbian:latest  
ENTRYPOINT []  
  
RUN apt-get update  
RUN apt-get -qy install curl build-essential python ca-certificates  
  
RUN mkdir -p /opt/augment00/bootstrap  
ADD main.py /opt/augment00/bootstrap/  
  
WORKDIR /opt/augment00/bootstrap  
  
CMD ["python", "main.py"]  
  

