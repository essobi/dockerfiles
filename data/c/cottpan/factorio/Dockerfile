FROM frolvlad/alpine-glibc:alpine-3.3_glibc-2.23  
MAINTAINER munisystem  
  
ENV APP_VER 0.14.23  
RUN apk --update add wget && \  
wget --no-check-certificate -O /tmp/factorio.tar.gz
https://www.factorio.com/get-download/`echo $APP_VER`/headless/linux64 && \  
tar zxvf /tmp/factorio.tar.gz && \  
apk del wget && \  
rm -rf /var/cache/apk/* /tmp/*  
  
WORKDIR factorio  
COPY ./start.sh /factorio/start.sh  
  
EXPOSE 34197/udp  
  
ENTRYPOINT ["./start.sh"]  

