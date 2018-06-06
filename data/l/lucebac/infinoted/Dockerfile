FROM alpine:3.6  
LABEL maintainer="lucebac <docker@lucebac.net>"  
  
ENV VERSION=0.7.1 \  
EXE_SUFFIX=0.7  
RUN apk add --update --no-cache glib-dev gnutls-dev libgsasl-dev libxml2-dev \  
gcc g++ git make tar wget && \  
adduser -D -H infinoted && \  
wget http://releases.0x539.de/libinfinity/libinfinity-$VERSION.tar.gz && \  
tar -xzf libinfinity-$VERSION.tar.gz && \  
rm libinfinity-$VERSION.tar.gz && \  
cd libinfinity-$VERSION && \  
./configure && \  
make && make install && \  
cd / && rm -rf libinfinity-$VERSION && \  
ln -s `which infinoted-$EXE_SUFFIX` /usr/local/bin/infinoted && \  
apk del gcc g++ git make tar wget  
  
COPY infinoted /etc/infinoted  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 6523  
CMD ["/run.sh"]  

