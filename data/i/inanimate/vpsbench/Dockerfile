FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get -y install git time bzip2 build-essential  
  
RUN git clone https://github.com/mgutz/vpsbench.git  
RUN cd vpsbench && chmod +x vpsbench  
  
CMD ["./vpsbench -u"]  

