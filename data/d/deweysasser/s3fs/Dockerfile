FROM ubuntu:trusty  
MAINTAINER Dewey Sasser <dewey@sasser.com>  
  
RUN apt-get update  
RUN apt-get install -y git  
RUN apt-get install -y build-essential  
RUN apt-get install -y libfuse-dev libcurl4-openssl-dev libxml2-dev mime-
support automake libtool pkg-config libssl-dev  
  
RUN mkdir /root/s3fs-fuse/  
COPY s3fs-fuse /root/s3fs-fuse/  
WORKDIR /root/s3fs-fuse/  
RUN ./autogen.sh  
RUN ./configure --prefix=/usr --with-openssl  
RUN make  
RUN make install  
  
COPY run /root/run  
  
ENTRYPOINT ["/root/run"]

