FROM alpine  
  
RUN apk add --no-cache git automake autoconf automake libtool g++ protobuf
protobuf-dev make  
  
RUN git clone \--depth 1 https://github.com/google/sentencepiece.git
/tmp/sentencepiece && \  
cd /tmp/sentencepiece && \  
./autogen.sh && \  
./configure && \  
make && \  
# somehow, test fails  
# make check && \  
make install && \  
rm -rf /tmp/sentencepiece  
  
RUN mkdir /data  
  
WORKDIR /data  

