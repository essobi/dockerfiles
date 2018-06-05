FROM centos:7  
WORKDIR /usr/local/bin  
  
RUN curl -fsSL
https://github.com/kelseyhightower/confd/releases/download/v0.7.1/confd-0.7.1-linux-
amd64 -o confd && \  
chmod a+x confd  
  
CMD confd  

