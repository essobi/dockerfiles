FROM alpine:latest  
RUN apk add --no-cache bash git alpine-sdk boost boost-dev clang llvm cmake
make libmicrohttpd libmicrohttpd-dev  
RUN git clone https://github.com/matt-42/silicon.git /root/silicon  
RUN cd /root/silicon && ./install.sh /usr/  
RUN rm -fr /root/silicon  
CMD /bin/sh  

