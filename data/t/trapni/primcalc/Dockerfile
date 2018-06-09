FROM alpine:3.7 AS build  
MAINTAINER Christian Parpart <christian@parpart.family>  
  
# get build dependencies  
RUN apk update  
RUN apk add g++ autoconf automake make  
COPY configure.ac Makefile.am autogen.sh /app/src/  
COPY src /app/src/src  
WORKDIR /app/src  
  
# compile binary (and test) statically  
ARG LDFLAGS=""  
ARG CXXFLAGS="-static -O2"  
RUN ./autogen.sh  
RUN ./configure  
RUN make  
  
# ensure unit tests pass  
RUN make check  
  
RUN strip primcalc  
  
# now build docker image from scratch with this binary in alone  
FROM scratch  
WORKDIR /  
COPY \--from=build /app/src/primcalc /primcalc  
ENTRYPOINT ["/primcalc"]  

