FROM resin/armv7hf-debian-qemu AS armBin  
  
FROM arm32v7/node  
MAINTAINER Marc Ammon <marc.ammon@fau.de>  
  
ENV DEFAULT_USER=root  
  
ADD . /app  
WORKDIR /app  
  
COPY \--from=armBin /usr/bin/cross-build-start /usr/bin/  
COPY \--from=armBin /usr/bin/cross-build-end /usr/bin/  
COPY \--from=armBin /usr/bin/qemu-arm-static /usr/bin/  
COPY \--from=armBin /usr/bin/resin-xbuild /usr/bin/  
RUN [ "cross-build-start" ]  
  
RUN npm install  
  
RUN [ "cross-build-end" ]  
  
EXPOSE 3000  
ENTRYPOINT ["./init"]  
  

