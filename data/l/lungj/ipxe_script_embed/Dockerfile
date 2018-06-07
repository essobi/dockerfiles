FROM gcc:4.9  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties  
RUN git clone git://git.ipxe.org/ipxe.git  
RUN apt-get install -y genisoimage syslinux  
WORKDIR /ipxe/src  
RUN make  

