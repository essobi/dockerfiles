FROM ubuntu:14.04.4  
ENV S3_LOCATION /s3data  
RUN apt-get update && apt-get install -y wget automake autotools-dev g++ git
libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config && git
clone https://github.com/s3fs-fuse/s3fs-fuse && wget
https://github.com/Yelp/dumb-init/releases/download/v1.0.1/dumb-
init_1.0.1_amd64.deb && dpkg -i dumb-init_*.deb && rm dumb-init_*.deb  
WORKDIR s3fs-fuse  
RUN ./autogen.sh && ./configure --prefix=/usr --with-openssl && make && make
install  
WORKDIR /  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh && rm -rf /s3fs-fuse && mkdir /s3data  
CMD dumb-init /run.sh  
VOLUME /s3data  

