# VERSION 1.0  
FROM ubuntu:latest  
  
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
wget \  
unzip  
  
ENV FOLDER_NAME stockfish-7  
WORKDIR /root  
RUN wget https://stockfish.s3.amazonaws.com/$FOLDER_NAME-src.zip \  
&& unzip -q $FOLDER_NAME-src.zip \  
&& mv $FOLDER_NAME-src $FOLDER_NAME \  
&& rm $FOLDER_NAME-src.zip  
  
WORKDIR $FOLDER_NAME/src  
RUN make build ARCH=x86-64  
  
# Clean Up  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root  
COPY run.sh .  
ENTRYPOINT ["./run.sh"]  

