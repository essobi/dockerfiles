# VERSION 1.0  
FROM ubuntu:latest  
  
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
wget  
  
ENV FOLDER_NAME stress-ng  
ENV VERSION V0.07.00  
RUN mkdir /root/$FOLDER_NAME  
  
WORKDIR /root  
RUN wget https://github.com/ColinIanKing/stress-ng/archive/$VERSION.tar.gz \  
&& tar -xf $VERSION.tar.gz -C $FOLDER_NAME \--strip-components=1 \  
&& rm $VERSION.tar.gz  
  
RUN make -C $FOLDER_NAME  
  
# Clean Up  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY run.sh .  
ENTRYPOINT ["./run.sh"]  

