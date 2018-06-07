FROM docker:17.06.1-ce-dind  
  
RUN apk add --no-cache git curl make gcc g++ python linux-headers binutils-
gold gnupg libstdc++  
WORKDIR /  
RUN curl -sSLO https://nodejs.org/dist/v8.4.0/node-v8.4.0.tar.xz  
RUN tar -xf node-v8.4.0.tar.xz  
WORKDIR /node-v8.4.0  
RUN ./configure --prefix=/usr --fully-static --without-npm  
RUN make -j$(getconf _NPROCESSORS_ONLN)  
RUN make install  

