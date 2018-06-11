# BUILD-USING: docker build .  
# RUN-USING: docker run -p 8585:8585 -v $SKY_DATA_DIR:/var/lib/sky:rw  
FROM ubuntu  
  
MAINTAINER Sky Contributors skydb.io  
  
RUN echo 'deb http://archive.ubuntu.com/ubuntu precise main universe' >
/etc/apt/sources.list && \  
echo 'deb http://archive.ubuntu.com/ubuntu precise-updates universe' >>
/etc/apt/sources.list && \  
apt-get update  
  
# Prevent daemon start during install  
RUN dpkg-divert --local \--rename --add /sbin/initctl && ln -s /bin/true
/sbin/initctl  
  
# Utilities  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential vim less
curl git wget  
  
RUN mkdir -p /usr/local/src  
  
# Go 1.2  
RUN cd /usr/local/src && \  
wget https://go.googlecode.com/files/go1.2.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf go1.2.linux-amd64.tar.gz  
  
ENV PATH $PATH:/usr/local/go/bin  
  
# Download and install sky-deps  
RUN cd /usr/local/src && \  
wget -O sky-deps.tar.gz https://github.com/skydb/sky-
deps/archive/unstable.tar.gz && \  
tar zxvf sky-deps.tar.gz && \  
cd sky-deps-unstable && \  
make && make install  
  
# Initialize environment variables.  
ENV GOPATH /go  
ENV GOBIN /go/bin  
ENV SKYDB_PATH /go/src/github.com/skydb  
ENV SKY_PATH /go/src/github.com/skydb/sky  
ENV SKY_BRANCH unstable_predupsort  
  
# Update linker configuration.  
RUN echo '/usr/local/lib' | tee /etc/ld.so.conf.d/sky.conf > /dev/null  
RUN ldconfig  
  
# Set up required directories.  
RUN mkdir -p $GOBIN  
RUN mkdir -p $SKYDB_PATH  
  
# Download Sky to its appropriate GOPATH location.  
RUN cd $SKYDB_PATH && \  
wget -O sky.tar.gz https://github.com/skydb/sky/archive/$SKY_BRANCH.tar.gz &&
\  
tar zxvf sky.tar.gz && \  
mv sky-$SKY_BRANCH sky && \  
cd sky  
  
# Retrieve Sky dependencies.  
RUN cd $SKY_PATH && make get  
  
# Build and install skyd into GOBIN.  
RUN cd $SKY_PATH && make build && mv skyd $GOBIN/skyd  
  
ENTRYPOINT /go/bin/skyd  
  
EXPOSE 8585  

