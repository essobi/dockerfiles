FROM alpine:latest AS builder  
  
RUN apk add --no-cache gcc make musl-dev  
  
COPY main.c Makefile /  
  
RUN make  
  
FROM scratch  
  
COPY \--from=builder hello hello  
  
CMD [ "/hello" ]  
  

