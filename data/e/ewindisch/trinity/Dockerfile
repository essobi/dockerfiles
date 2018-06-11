FROM ubuntu  
  
RUN apt-get update; \  
apt-get install -qy git build-essential  
  
RUN mkdir /opt; \  
git clone https://github.com/kernelslacker/trinity /opt/trinity  
  
WORKDIR /opt/trinity  
RUN ./configure.sh  
RUN make  
  
WORKDIR /tmp  
CMD ["--dangerous"]  
ENTRYPOINT ["/opt/trinity/trinity"]  

