FROM debian:jessie  
MAINTAINER Santiago Lizardo  
  
RUN apt-get -y update  
RUN apt-get install -y git  
RUN git clone https://github.com/santiagolizardo/plain-port-scanner.git  
RUN apt-get install -y automake make gcc  
  
WORKDIR plain-port-scanner  
RUN ./autogen.sh && ./configure  
RUN make install  
RUN ls -la /usr/local/bin/plain-port-scanner  
  
ENTRYPOINT ["/usr/local/bin/plain-port-scanner"]  
CMD ["-a", "localhost"]  
  

