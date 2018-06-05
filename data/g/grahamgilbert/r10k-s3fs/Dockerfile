FROM grahamgilbert/r10k  
ADD 00-mount_s3.sh /docker-entrypoint.d/00-mount_s3.sh  
RUN apt-get update && apt-get install -y wget automake autotools-dev g++ git
libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config && git
clone https://github.com/s3fs-fuse/s3fs-fuse && chmod 755 /docker-
entrypoint.d/00-mount_s3.sh  
WORKDIR s3fs-fuse  
RUN ./autogen.sh && ./configure --prefix=/usr --with-openssl && make && make
install  
WORKDIR /  
RUN rm -rf /s3fs-fuse  

