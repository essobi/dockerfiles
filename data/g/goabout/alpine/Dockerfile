FROM alpine  
  
MAINTAINER Go About <tech@goabout.com>  
  
RUN ln -sfn /lib /lib64 && \  
ln -sfn /lib/ld-musl-x86_64.so.1 /lib/ld-linux-x86-64.so.2  
  
ADD https://github.com/jcassee/parameterized-
entrypoint/releases/download/0.8.0/entrypoint_linux_amd64_alpine
/usr/local/bin/entrypoint  
RUN chmod +x /usr/local/bin/entrypoint  
  
ENTRYPOINT ["entrypoint", "--"]  

