FROM alpine:3.2  
RUN apk update && apk add make gcc musl-dev  
RUN wget -O - http://code.call-cc.org/releases/4.10.0/chicken-4.10.0.tar.gz |
tar xz  
  
WORKDIR /chicken-4.10.0  
  
RUN make PLATFORM=linux && make PLATFORM=linux install  
  
RUN rm -fr /chicken-4.10.0  
  
WORKDIR /  
  
CMD ["csi"]

