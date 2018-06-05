FROM ubuntu  
RUN apt-get update && apt-get install -y wget libssl1.0.0 cmake g++ gdb git &&
\  
mkdir cass-deps && \  
mkdir scylla-src && \  
cd cass-deps && \  
wget http://downloads.datastax.com/cpp-
driver/ubuntu/16.04/cassandra/v2.7.1/cassandra-cpp-driver_2.7.1-1_amd64.deb &&
\  
wget http://downloads.datastax.com/cpp-
driver/ubuntu/16.04/cassandra/v2.7.1/cassandra-cpp-driver-
dev_2.7.1-1_amd64.deb && \  
wget http://downloads.datastax.com/cpp-
driver/ubuntu/16.04/dependencies/libuv/v1.18.0/libuv_1.18.0-1_amd64.deb && \  
wget http://downloads.datastax.com/cpp-
driver/ubuntu/16.04/dependencies/libuv/v1.18.0/libuv-dev_1.18.0-1_amd64.deb &&
\  
dpkg -i libuv_1.18.0-1_amd64.deb && \  
dpkg -i libuv-dev_1.18.0-1_amd64.deb && \  
dpkg -i cassandra-cpp-driver_2.7.1-1_amd64.deb && \  
dpkg -i cassandra-cpp-driver-dev_2.7.1-1_amd64.deb && \  
cd ../ && \  
rm -rf cass-deps && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
WORKDIR scylla-src  
ENTRYPOINT ["/bin/sh", "-c"]  

