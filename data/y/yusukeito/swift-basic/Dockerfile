FROM swift:4.1  
ENV PROTOC_VER 3.5.1  
# Add MariaDB repository  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xF1656F24C74CD1D8 && \  
add-apt-repository 'deb [arch=amd64,i386,ppc64el]
http://ftp.yz.yamagata-u.ac.jp/pub/dbms/mariadb/repo/10.1/ubuntu xenial main'  
  
#  
RUN ln -fs /usr/share/zoneinfo/Etc/GMT /etc/localtime  
  
# Install dependency library  
RUN apt-get update && \  
apt-get install -y libxml2-dev libmariadbclient-dev unzip tzdata && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install protoc  
RUN curl -s -O -L
https://github.com/google/protobuf/releases/download/v${PROTOC_VER}/protoc-${PROTOC_VER}-linux-x86_64.zip
&& \  
unzip protoc-${PROTOC_VER}-linux-x86_64.zip -d /usr && \  
rm protoc-${PROTOC_VER}-linux-x86_64.zip  
  
# Build and install the swiftgrpc plugin  
RUN git clone -b 0.4.3 --depth=1 https://github.com/grpc/grpc-swift && \  
cd grpc-swift && \  
make && \  
cp protoc-gen-swift /usr/bin && \  
cp protoc-gen-swiftgrpc /usr/bin && \  
cd ../ && rm -rf grpc-swift  
  

