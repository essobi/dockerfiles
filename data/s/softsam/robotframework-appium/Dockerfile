FROM debian:latest  
  
RUN apt-get update && \  
apt-get -y install python-pip && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install robotframework==2.9  
RUN pip install robotframework-appiumlibrary==1.3.3  
  
RUN mkdir /robot  
VOLUME /robot  
WORKDIR /robot  
  
ENTRYPOINT ["/usr/local/bin/pybot"]  

