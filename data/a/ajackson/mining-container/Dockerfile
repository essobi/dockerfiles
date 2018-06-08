FROM ubuntu  
  
# Volume for log output  
RUN mkdir -p /opt/mining-container/logs  
VOLUME ["/opt/mining-container/logs"]  
  
# Update Ubuntu and install dependancies  
RUN apt-get update -y  
RUN apt-get install -y git build-essential make automake screen
libcurl4-openssl-dev  
  
# Clone out application  
RUN cd /opt/mining-container/ && git clone
https://github.com/wolf9466/cpuminer-multi  
#RUN cd /opt/mining-container/cpuminer-multi && ./autogen.sh &&
CFLAGS="-march=native" ./configure --disable-aes-ni && make  
# Copy in run script  
COPY runMiner.sh /opt/mining-container/  
RUN chmod +x /opt/mining-container/runMiner.sh  
  
ENTRYPOINT /opt/mining-container/runMiner.sh "$POOL" "$ACCOUNT" "$AESNI"  

