FROM ubuntu:14.04  
MAINTAINER Huy TA <hlieuta@gmail.com>  
  
RUN apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential libfuse-
dev libcurl4-openssl-dev libxml2-dev mime-support automake libtool wget tar
openjdk-7-jdk  
  
RUN wget https://github.com/s3fs-fuse/s3fs-fuse/archive/v1.78.tar.gz -O
/usr/src/v1.78.tar.gz  
  
RUN tar xvz -C /usr/src -f /usr/src/v1.78.tar.gz  
RUN cd /usr/src/s3fs-fuse-1.78 && ./autogen.sh && ./configure --prefix=/usr &&
make && make install  
  
# Create a mount point for s3fs  
RUN mkdir /data  
  
ADD com.porcup.launchpad.jar /app/com.porcup.launchpad.jar  
  
ADD docker-entrypoint.sh /app/docker-entrypoint.sh  
RUN chmod u+x /app/docker-entrypoint.sh  
  
# Copy sling configuration directory  
ADD sling /app/sling  
  
# Set the working directory to /app  
WORKDIR /app  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
  
CMD ["java","-jar" , "/app/com.porcup.launchpad.jar","-p","80"]  
  
EXPOSE 80

