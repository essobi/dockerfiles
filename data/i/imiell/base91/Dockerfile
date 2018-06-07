FROM ubuntu:18.04  
RUN apt-get update -y && apt-get install -y wget make gcc  
RUN wget -qO- http://downloads.sourceforge.net/base91/base91-0.6.0.tar.gz |
tar -zxvf -  
WORKDIR base91-0.6.0  
RUN make  
RUN mv base91 /usr/bin  
ENTRYPOINT ["base91"]  

