FROM java:openjdk-7-jdk  
  
MAINTAINER Michael Sevilla  
  
RUN echo "===> Installing jxio stuff..." && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y \  
libtool autoconf automake build-essential \  
ibverbs-utils rdmacm-utils infiniband-diags perftest \  
librdmacm-dev libibverbs-dev numactl libnuma-dev libaio-dev libevent-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64/  
ADD build /  
RUN chmod 755 /build  
  
ENTRYPOINT ["/build"]  
  

