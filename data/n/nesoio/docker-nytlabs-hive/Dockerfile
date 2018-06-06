FROM golang:1.8-alpine  
  
ENV SRC_PATH /go/src/hive  
  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache bash git openssh make\  
&& mkdir -p $SRC_PATH \  
&& git clone https://github.com/neso-io/hive.git "$SRC_PATH"  
  
WORKDIR $SRC_PATH  
  
RUN git checkout -b 1.1.0  
  
RUN make \  
&& mv -f build / \  
&& rm -rf $SRC_PATH \  
&& apk del bash git openssh make  
  
WORKDIR /  
COPY start.sh /  
RUN chmod +x start.sh  
  
CMD '/start.sh'  

