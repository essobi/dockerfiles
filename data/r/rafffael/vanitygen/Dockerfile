FROM debian:jessie  
VOLUME ["/src"]  
WORKDIR /src  
RUN apt-get update && \  
apt-get install -y build-essential automake autoconf libtool libgmp3-dev && \  
rm -rf /var/lib/apt/lists/*  
ADD . /src  
RUN make && make install  
ENTRYPOINT ["vanitygen"]  
CMD ["--help"]  

