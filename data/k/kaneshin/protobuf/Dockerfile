FROM alpine:3.5  
MAINTAINER Shintaro Kaneko <kaneshin0120@gmail.com>  
  
ENV PROTOBUF_VERSION 3.1.0  
ENV PROTOBUF_REPOSITORY https://github.com/google/protobuf  
ENV PROTOBUF_DIR protobuf  
  
WORKDIR /tmp  
  
RUN apk add --update git curl build-base autoconf automake libtool libstdc++ \  
&& rm -rf /var/cache/apk/*  
  
RUN git clone ${PROTOBUF_REPOSITORY} -b v${PROTOBUF_VERSION} \--depth 1
./${PROTOBUF_DIR} \  
&& cd ./${PROTOBUF_DIR} \  
&& ./autogen.sh \  
&& ./configure --prefix=/usr \  
&& make -j 4 \  
&& make install  
  
RUN rm -rf ./${PROTOBUF_DIR}  
  
ADD . /proto  
WORKDIR /proto  
  
ENTRYPOINT ["protoc"]  

