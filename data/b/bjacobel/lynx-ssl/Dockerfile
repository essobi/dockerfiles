FROM alpine  
LABEL Brian Jacobel <bjacobel@gmail.com>  
RUN apk --update add \  
curl \  
build-base \  
ncurses-dev \  
openssl-dev \  
ca-certificates  
  
RUN curl -sSL https://invisible-
mirror.net/archives/lynx/tarballs/lynx2.8.9dev.16.zip > lynx.zip && \  
unzip lynx.zip && \  
cd lynx2.8.9dev.16 && \  
./configure --with-ssl --with-zlib --with-screen=ncurses && \  
make && \  
make install  
  
ENTRYPOINT ["lynx", "--cookies", "--term=linux", "--dump"]  

