FROM alpine:3.6  
RUN apk add --no-cache cmake ninja g++ protobuf-dev libev-dev libpcap-dev sed  
ADD https://github.com/gflags/gflags/archive/master.zip /gflags.zip  
RUN unzip /gflags.zip  
WORKDIR /gflags-master/build  
RUN cmake -GNinja -DCMAKE_INSTALL_PREFIX=/usr ..  
RUN ninja install  
RUN cp /usr/include/gflags/* /usr/include/google/  
ADD . /src  
WORKDIR /src/build  
RUN sed -i'' -e s/-Werror//g ../CMakeLists.txt  
RUN cmake -GNinja ..  
RUN ninja  
RUN ls -lt bin  
  
FROM alpine:3.6  
RUN apk add --no-cache protobuf-dev libev libpcap  
COPY \--from=0 /src/build/bin /bin  
# EXPOSE 55555/UDP  
CMD ["flow-disruptor", "-h"]  

