FROM alpine:latest  
  
# fix library dependencies, otherwise 'not found' error may occur when
executing golang binary.  
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  
  
COPY stress-linux-amd64-1.0.4 /usr/local/bin/stress  
  
CMD ["tail","-f","/etc/hosts"]

