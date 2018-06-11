FROM debian:jessie-slim  
#FROM alpine  
WORKDIR /src  
#RUN apk add --update clang binutils gcc clang-libs libc-dev coreutils  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libc6-dev clang coreutils binutils gcc make \  
&& rm -rf /var/lib/apt/lists/*  
ADD ./src/* ./  
RUN make all  
RUN make install  
RUN cp start.sh /usr/local/bin/start.sh  
RUN chmod 755 /usr/local/bin/start.sh  
ENTRYPOINT ["start.sh"]  
  

