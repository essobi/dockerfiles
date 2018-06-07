# VERSION 1.1  
FROM ubuntu:latest  
  
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential  
  
ENV FOLDER_NAME himeno  
  
RUN mkdir /root/$FOLDER_NAME  
WORKDIR /root/$FOLDER_NAME  
  
COPY himenoBMTxpa.c himenoBMTxpa.c  
  
RUN gcc himenoBMTxpa.c -O3 -o himenoBMTxpa \  
&& rm himenoBMTxpa.c  
  
# Clean Up  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root  
COPY run.sh .  
ENTRYPOINT ["./run.sh"]  

