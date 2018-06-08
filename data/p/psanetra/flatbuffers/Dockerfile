FROM alpine:latest  
  
WORKDIR /usr/local/src/flatbuffers/  
  
COPY ./ ./  
  
ENV BUILD_TYPE=Release  
ENV BIICODE=false  
ENV CXX=g++  
ENV CC=gcc  
  
RUN apk add --no-cache gcc g++ make cmake  
  
RUN cmake -DCMAKE_BUILD_TYPE=$BUILD_TYPE . && make && make test  
  
FROM alpine:latest  
WORKDIR /app  
RUN apk add --no-cache libstdc++  
COPY \--from=0 /usr/local/src/flatbuffers/flatc ./flatc  
ENTRYPOINT ["/app/flatc"]  
  

