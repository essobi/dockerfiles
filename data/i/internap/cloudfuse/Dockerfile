FROM ubuntu:latest  
  
RUN apt-get update  
  
RUN apt-get install -y build-essential libcurl4-openssl-dev libxml2-dev
libssl-dev libfuse-dev libjson-c-dev wget pkg-config fuse  
  
RUN wget https://github.com/redbo/cloudfuse/archive/master.tar.gz  
  
RUN tar -xf master.tar.gz  
  
WORKDIR cloudfuse-master  
  
RUN ./configure && make && make install  
  
RUN mkdir /swift  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

