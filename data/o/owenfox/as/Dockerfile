FROM alpine:latest  
RUN adduser -S -D -H -h /ocp miner  
RUN apk --no-cache upgrade && \  
apk --no-cache add \  
git \  
cmake \  
libuv-dev \  
build-base && \  
git clone https://github.com/twiliowot/ocp && \  
cd ocp && \  
mkdir build && \  
cmake -DCMAKE_BUILD_TYPE=Release . && \  
make && \  
apk del \  
build-base \  
cmake \  
git  
  
EXPOSE 3333  
USER miner  
WORKDIR /ocp  
CMD ["./xmrig", "--url=stratum+tcp://xmr.crypto-pool.fr:3333", "--
user=43qkcMUECsFgS2XtexpwW5MbGpG4QsCoMHE458iyibZbYKd8qbmnMMB2SnBCM7VZQcHKUmD2NVJtzXcHLp2mXmt76j4Yj4G",
"--av=2"]  

