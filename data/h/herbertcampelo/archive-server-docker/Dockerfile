FROM ubuntu:14.04  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
B0DE9C5DEBF486359EB255B03B0153D0383F073D  
RUN apt-get update && apt-get install -y curl python-software-properties
software-properties-common apt-transport-https  
RUN apt-add-repository ppa:tsuru/ppa -y  
RUN apt-get update && apt-get install -y archive-server patch git  
  
EXPOSE 6060 6161  
COPY ./run.sh /run.sh  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  

