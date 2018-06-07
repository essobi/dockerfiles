FROM debian:jessie  
MAINTAINER Sébastien M-B <essembeh@gmail.com>  
  
ADD sources.list /etc/apt/  
RUN apt-get -q update  
RUN apt-get install -y -q build-essential git cmake libmpdclient-dev
libmpdclient2 && apt-get clean  
  
## Checkout projects  
WORKDIR /root/  
RUN git clone https://github.com/notandy/ympd  
WORKDIR /root/ympd  
RUN cmake .  
RUN make  
  
ENTRYPOINT ["/root/ympd/ympd"]  
EXPOSE 8080  

