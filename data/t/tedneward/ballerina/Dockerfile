FROM tedneward/java  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
ENV BALLERINA_VER=0.95.2  
RUN curl -fsSL -o /tmp/ballerina-tools-${BALLERINA_VER}.zip
https://ballerinalang.org/downloads/ballerina-tools/ballerina-
tools-${BALLERINA_VER}.zip && \  
unzip -d /usr/local /tmp/ballerina-tools-${BALLERINA_VER}.zip  
  
ENV BALLERINA_HOME=/usr/local/ballerina-tools-${BALLERINA_VER}  
ENV PATH=$BALLERINA_HOME/bin:$PATH  
  
EXPOSE 9090  
ENTRYPOINT ["/bin/bash"]  

