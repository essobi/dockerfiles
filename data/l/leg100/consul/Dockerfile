FROM ubuntu  
RUN apt-get update && apt-get install -y unzip  
ADD https://dl.bintray.com/mitchellh/consul/0.5.2_linux_amd64.zip
/tmp/consul.zip  
RUN cd /bin && unzip /tmp/consul.zip && chmod +x /bin/consul && rm
/tmp/consul.zip  
  
ENTRYPOINT ["/bin/consul"]  

