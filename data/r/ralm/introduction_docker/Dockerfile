FROM ubuntu:16.04 as builder  
RUN apt-get update && \  
apt-get install -y build-essential  
WORKDIR /build  
COPY hello.c .  
RUN gcc --static -o hello hello.c  
  
FROM alpine  
WORKDIR /app  
COPY \--from=builder /build/hello .  
CMD ["./hello"]

