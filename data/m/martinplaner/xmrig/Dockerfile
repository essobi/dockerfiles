FROM alpine AS build-env  
MAINTAINER Martin Planer  
ENV VERSION 2.5.3  
RUN apk update && apk add gcc g++ musl-dev make cmake libuv-dev  
  
ADD https://github.com/xmrig/xmrig/archive/v$VERSION.tar.gz /  
RUN tar xzf v$VERSION.tar.gz  
  
WORKDIR /xmrig-$VERSION/build  
  
RUN cmake .. -DWITH_HTTPD=OFF  
RUN make  
RUN mv /xmrig-$VERSION/build/xmrig /xmrig  
  
FROM alpine  
  
RUN apk update && apk upgrade && apk add libuv  
  
COPY \--from=build-env /xmrig /xmrig  
  
ENTRYPOINT ["/xmrig"]  

