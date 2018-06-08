FROM ubuntu:trusty  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y cpanminus build-essential  
  
RUN cpanm install --force MogileFS::Server  
  
RUN mkdir -p /node/device/dev1  
WORKDIR /node  
ADD ./mogstored.conf /node/mogstored.conf  
EXPOSE 7500  
CMD ["mogstored", "-c", "./mogstored.conf"]  

