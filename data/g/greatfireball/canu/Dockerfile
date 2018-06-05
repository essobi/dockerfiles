FROM java:8  
LABEL maintainer="frank.foerster@ime.fraunhofer.de"  
LABEL description="Dockerfile providing the canu assembler for long reads"  
  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get -y install build-essential wget gnuplot  
  
RUN wget https://github.com/marbl/canu/archive/v1.5.tar.gz  
RUN tar -xzf v1.5.tar.gz && rm v1.5.tar.gz  
RUN cd canu-1.5/src && make -j8  
  
ENV PATH=/canu-1.5/bin:${PATH}  
  
VOLUME /data  

