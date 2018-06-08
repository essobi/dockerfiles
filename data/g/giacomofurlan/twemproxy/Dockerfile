FROM alpine:latest  
  
RUN apk add --no-cache --virtual .build git g++ make autoconf automake  
RUN apk add --no-cache libtool  
  
WORKDIR /src  
RUN git clone https://github.com/twitter/twemproxy.git .  
RUN autoreconf -fvi  
RUN CFLAGS="-O3 -fno-strict-aliasing" ./configure && make  
RUN make install  
  
# Clean-up the build packages  
RUN apk del .build  
RUN rm -rf /src/*  
  
WORKDIR /app  
VOLUME /usr/local/etc/nutcracker/nutcracker.yml  
EXPOSE 21121  
CMD ["nutcracker", "--conf-file", "/usr/local/etc/nutcracker/nutcracker.yml"]  

