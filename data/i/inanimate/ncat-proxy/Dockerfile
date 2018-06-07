FROM debian:stable  
  
ENV VERSION 6.47  
RUN apt-get update  
RUN apt-get -y install build-essential wget bzip2 libcap2-bin  
  
RUN wget http://nmap.org/dist/nmap-${VERSION}.tar.bz2 && \  
bzip2 -cd nmap-${VERSION}.tar.bz2 | tar xvf - && \  
cd nmap-${VERSION} && \  
./configure && \  
make && \  
make install && \  
cd && \  
rm -rf nmap-${VERSION}  
  
RUN apt-get -y purge wget build-essential bzip2  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
ADD run /etc/run  
  
RUN setcap 'cap_net_bind_service=+ep' $(which ncat)  
  
USER nobody  
  
CMD ["/etc/run"]  

