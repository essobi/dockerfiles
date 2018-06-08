FROM alpine:latest  
RUN apk add --update build-base  
COPY . /cc65  
WORKDIR /cc65  
RUN make bin  
  
FROM alpine:latest  
COPY \--from=0 /cc65/bin /bin  

