FROM alpine:latest  
  
MAINTAINER Peter Mikus <pmikus@gmail.com>  
  
# Install pre-requisities  
RUN apk add \--no-cache git make perl libgcc openssl build-base linux-headers
\  
&& git clone https://github.com/ayourtch/wrk \  
&& cd wrk \  
&& sed -i 's/no-idea/no-idea no-async/' Makefile \  
&& make all \  
&& mv wrk /bin/ \  
&& apk del git make perl openssl build-base linux-headers  
  
# Define default command  
ENTRYPOINT ["/bin/wrk"]  

