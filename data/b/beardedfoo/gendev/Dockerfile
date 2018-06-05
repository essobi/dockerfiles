ARG VERSION=v0.3.0  
# Build the gendev SDK  
FROM ubuntu:14.04 AS builder  
RUN apt-get update  
RUN apt-get install -y build-essential wget unzip unrar-free texinfo git
openjdk-7-jre-headless  
RUN git clone https://github.com/kubilus1/gendev.git  
WORKDIR gendev  
RUN git checkout $VERSION  
RUN make  
RUN mkdir /opt/gendev  
RUN make install  
  
# Install the gendev SDK into a new image  
FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jre-headless make  
ENV GENDEV /opt/gendev  
COPY \--from=builder /opt/gendev $GENDEV  
ENV PATH $GENDEV/bin:$PATH  
WORKDIR /src  
CMD make -f $GENDEV/sgdk/mkfiles/makefile.gen -C /src clean all  

