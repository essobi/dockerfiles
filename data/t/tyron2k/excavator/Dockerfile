FROM nvidia/cuda:9.0-runtime-ubuntu16.04  
# Install dependencies  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y ocl-icd-opencl-dev  
ADD
https://github.com/nicehash/excavator/releases/download/v1.5.2a/excavator_1.5.2a_amd64.deb
/excavator.deb  
RUN apt install /excavator.deb  
  
# Install nuxhashd  
RUN apt-get install -y python2.7 git  
RUN ln -sf /usr/bin/python2.7 /usr/local/bin/python2  
RUN git clone https://github.com/YoRyan/nuxhash.git /nuxhash  
RUN mkdir /nuxhash-config  
  
COPY configureAndMine.sh /  
RUN chmod +x /configureAndMine.sh  
  
ARG WALLET=3Ab9JW9H27cNqWMjYRP9X8bAQBABPM1hW4  
ENV WALLET $WALLET  
ARG REGION=eu  
ENV REGION $REGION  
  
ENTRYPOINT /configureAndMine.sh  

