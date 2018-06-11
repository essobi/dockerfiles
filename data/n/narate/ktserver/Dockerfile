FROM alpine:3.4  
MAINTAINER Narate Ketram <rate@dome.cloud>  
  
RUN apk update && apk add git build-base lua5.1-dev lzo-dev zlib-dev  
RUN cd /tmp && \  
git clone https://github.com/alticelabs/kyoto.git && \  
cd kyoto && \  
make && \  
make install && \  
make clean && \  
cd && \  
rm -rf /tmp/kyoto  
RUN mkdir -p /data/db  
CMD ["ktserver", "-plsv", "/usr/local/libexec/ktplugservmemc.so", "-plex",
"port=11211#opts=f",
"/data/db/casket.kch#opts=l#bnum=20000000#msiz=4g#dfunit=8" ]  
EXPOSE 11211  

