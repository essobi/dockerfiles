# VERSION 1.1  
FROM ubuntu:latest  
  
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
wget  
  
ENV FOLDER_NAME ramsmp  
  
WORKDIR /root  
RUN wget http://www.alasir.com/software/ramspeed/ramsmp-3.5.0.tar.gz \  
&& tar -xf ramsmp-3.5.0.tar.gz \  
&& mv ramsmp-3.5.0 $FOLDER_NAME \  
&& rm ramsmp-3.5.0.tar.gz  
  
WORKDIR /root/$FOLDER_NAME  
RUN ./build.sh Linux x86_64  
  
# Clean Up  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root  
COPY run.sh .  
ENTRYPOINT ["./run.sh"]  

