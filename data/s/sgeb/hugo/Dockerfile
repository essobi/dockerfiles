FROM alpine:3.7  
MAINTAINER Serge Gebhardt <serge.gebhardt@gmail.com>  
  
ENV HUGO_VERSION 0.37.1  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_Linux-64bit  
ENV HUGO_TARBALL ${HUGO_BINARY}.tar.gz  
  
ADD
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_TARBALL}
/usr/local/  
RUN mkdir /usr/local/${HUGO_BINARY} \  
&& tar xzf /usr/local/${HUGO_TARBALL} -C /usr/local/${HUGO_BINARY} \  
&& ln -s /usr/local/${HUGO_BINARY}/hugo /usr/local/bin/hugo \  
&& rm /usr/local/${HUGO_TARBALL}  
  
VOLUME /src  
WORKDIR /src  
  
EXPOSE 1313  
ENTRYPOINT ["hugo"]  
CMD ["version"]  

