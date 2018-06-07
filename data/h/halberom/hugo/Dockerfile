FROM alpine:latest  
  
ENV VERSION=0.25.1  
ENV SRC=hugo_${VERSION}_Linux-64bit \  
EXTENSION=tar.gz \  
BINARY=hugo  
  
# pygments for syntax highlighting, python and py-pip included  
# as otherwise errors with no module 'pkg_resources'  
RUN apk add --no-cache --update py-pygments python py-pip  
  
ADD
https://github.com/gohugoio/hugo/releases/download/v${VERSION}/${SRC}.${EXTENSION}
/usr/local/  
  
RUN mkdir -p /usr/local/${SRC} && \  
tar xzf /usr/local/${SRC}.${EXTENSION} -C /usr/local/${SRC} && \  
ln -s /usr/local/${SRC}/${BINARY} /usr/local/bin/hugo && \  
rm /usr/local/${SRC}.${EXTENSION}  
  
WORKDIR /root  
EXPOSE 1313  
CMD ["hugo"]  

