FROM golang:1.4.2  
MAINTAINER larstobi  
  
ENV VERSION 0.8  
VOLUME /data  
EXPOSE 80 443 3179 8080  
ENV USER root  
ENV HOME /data  
WORKDIR /data  
CMD ["/bin/camlistored", "-listen", ":80"]  
  
RUN curl -sqLf
https://github.com/camlistore/camlistore/archive/${VERSION}.tar.gz | tar xzf -
-C /usr/src && \  
cd /usr/src/camlistore-${VERSION} && make && \  
mv bin/* /bin && rm -rf /usr/src/camlistore-${VERSION}  

