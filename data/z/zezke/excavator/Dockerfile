FROM nvidia/cuda:9.0-runtime-ubuntu16.04  
# Install dependencies  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y ocl-icd-opencl-dev  
ADD
https://github.com/nicehash/excavator/releases/download/v1.4.1a/excavator_1.4.1a-xenial0_amd64.deb
/excavator_1.4.1a-xenial0_amd64.deb  
RUN apt install /excavator_1.4.1a-xenial0_amd64.deb  
  
# Install nuxhashd  
RUN apt-get install -y python2.7 git  
RUN ln -sf /usr/bin/python2.7 /usr/local/bin/python2  
RUN git clone https://github.com/YoRyan/nuxhash.git /nuxhash  
RUN mkdir /nuxhash-config  
  
COPY configureAndMine.sh /  
RUN chmod +x /configureAndMine.sh  
  
ARG WALLET=3KAKffgMS6JzNA5oa6C19zGXJgQbZxSFo6  
ENV WALLET $WALLET  
ARG REGION=eu  
ENV REGION $REGION  
  
ENTRYPOINT /configureAndMine.sh

