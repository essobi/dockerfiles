FROM alpine:3.7 as build  
  
ENV XMRIG_BUILD_DIR /build  
  
RUN mkdir $XMRIG_BUILD_DIR && cd $XMRIG_BUILD_DIR  
COPY xmrig $XMRIG_BUILD_DIR  
RUN mv $XMRIG_BUILD_DIR/xmrig /usr/bin/  
  
FROM alpine:3.7  
COPY \--from=build /usr/bin/xmrig /usr/bin/  
RUN apk --no-cache add libuv-dev \  
&& chmod +x /usr/bin/xmrig  
ENTRYPOINT ["xmrig"]  

