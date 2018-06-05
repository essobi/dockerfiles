FROM aerospike:3.9.1-1  
  
RUN wget http://www.aerospike.com/download/tools/3.9.1.2/artifact/ubuntu16 -O
aerospike-tools.tgz\  
&& mkdir aerospike-tools \  
&& tar xzf aerospike-tools.tgz \--strip-components=1 -C aerospike-tools \  
&& dpkg -i aerospike-tools/aerospike-tools-*.deb \  
&& rm -r aerospike-tools  
  
  

