# usage: docker run mkell43/minerd -a cryptonight -o
stratum+tcp:miningpool.url:port -u username -p password  
FROM alpine:3.7 as build  
RUN apk --no-cache add autoconf automake build-base curl curl-dev make git  
RUN git clone https://github.com/OhGodAPet/cpuminer-multi.git  
RUN cd cpuminer-multi && ./autogen.sh && ./configure CFLAGS="-O3" && make  
  
FROM alpine:3.7  
RUN apk --no-cache add curl-dev  
COPY \--from=build cpuminer-multi/minerd /usr/bin  
ENTRYPOINT ["minerd"]  

