FROM ubuntu:latest  
MAINTAINER David Manouchehri  
  
RUN apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install git libswitch-perl
libdatetime-perl libdigest-crc-perl libcompress-raw-lzma-perl libtext-glob-
perl libio-stringy-perl xz-utils libmarpa-r2-perl wget unzip  
  
RUN useradd -m uninno  
USER uninno  
WORKDIR /home/uninno  
ENV HOME /home/uninno  
  
RUN git clone https://github.com/onitake/uninno.git  
ENV PATH /home/uninno/uninno:$PATH  
  
CMD ["/bin/bash"]  

