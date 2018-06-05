# VERSION 1.1  
FROM ubuntu:latest  
  
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
wget  
  
ENV FOLDER_NAME blogbench-1.1  
WORKDIR /root  
RUN wget https://download.pureftpd.org/pub/blogbench/$FOLDER_NAME.tar.gz \  
&& tar -xf $FOLDER_NAME.tar.gz  
  
WORKDIR /root/$FOLDER_NAME  
RUN ./configure && make install-strip  
  
WORKDIR /root  
RUN rm -rf $FOLDER_NAME $FOLDER_NAME.tar.gz  
  
# Clean Up  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY run.sh .  
ENTRYPOINT ["./run.sh"]  

