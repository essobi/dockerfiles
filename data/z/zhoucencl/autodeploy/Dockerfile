FROM ubuntu:12.04  
MAINTAINER zhoucen <zhoucencl@gmail.com>  
  
RUN \  
apt-get update && \  
apt-get install git -y  
  
VOLUME ["/data","/opt/src"]  
  
ADD deploy.py /opt/src/  
  
EXPOSE 22 5000  
WORKDIR /opt/src  
  
CMD ["python deploy.py"]  

